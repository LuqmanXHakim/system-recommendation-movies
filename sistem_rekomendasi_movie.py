# -*- coding: utf-8 -*-
"""sistem-rekomendasi-movie.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P99bNkC8tiVgqawUA7berl1m-BZHukXC

# **Proyek Machine Learning Terapan**

Proyek System Recommendations: **Movie**
- Nama: **Luqman Hakim**
- Email: luqmanxhakim22042002@gmail.com
- Id Dicoding:2608610

# Data Loading
"""

from google.colab import files
files.upload()  # Pilih file 'kaggle.json' yang telah diunduh

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d snehal1409/movielens

!unzip movielens.zip

"""# Data Understanding"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from keras import layers
import tensorflow as tf
from tensorflow import keras

"""## Jumlah Data dari Masing-masing Dataset"""

movies = pd.read_csv('/content/movies.csv')
ratings = pd.read_csv('/content/ratings.csv')

print('Jumlah data movies: ', len(movies.movieId.unique()))
print('Jumlah data ratings: ', len(ratings.userId.unique()))

"""# Univariate Exploratory Data Analysis (EDA)

## Dataset Movies
"""

movies.info()

print('Banyak data: ', len(movies.movieId.unique()))
print('Genre: ', movies.genres.unique())

movies.head()

movies.describe()

#Menampilkan jumlah baris dan kolom dalam dataset
movies.shape

# Menampilkan nilai unik pada kolom 'title'
movies.title.nunique()

# Menampilkan nilai duplikat pada kolom 'title'
duplicate_titles = movies[movies['title'].duplicated(keep=False)]
print(duplicate_titles['title'])

# Drop nilai duplikat pada kolom 'title'
movies.drop_duplicates(subset='title', keep='first', inplace=True)
movies

# Mengubah nama kolom 'title'
movies.rename(columns={'title':'title_year'}, inplace=True)
movies

# Extract kolom 'title' untuk memisahkan dengan 'year'
def extract_title(title_year):
    import re
    match = re.search(r'\((\d{4})\)$', title_year)
    if match:
        return title_year[:match.start()].strip()
    else:
        return title_year

def extract_year(title_year):
    if '(' in title_year and ')' in title_year:
        year = title_year.split('(')[-1].split(')')[0]
        if year.isdigit():
            return year
    return np.nan

# Hapus spasi di kolom 'title_year'
movies.loc[:, 'title_year'] = [val.strip() for val in movies['title_year']]

# Ekstrak kolom 'title' dan 'year' menggunakan fungsi yang telah dibuat
movies['title'] = [extract_title(val) for val in movies['title_year']]
movies['year'] = [extract_year(val) for val in movies['title_year']]

# Hapus kolom 'title_year'
del movies['title_year']

movies.head()

# Memisahkan nilai-nilai pada kolom "genres"
movies['genres'] = [genre.split('|') for genre in movies['genres']]
movies.head()

# Menghitung jumlah film per genre
movies2 = movies.copy()
movies2 = movies2.explode('genres')

genre_counts = movies2['genres'].value_counts().reset_index()
genre_counts.columns = ['Genre', 'Count']

# Visualisasi dengan palet dan gaya yang berbeda
plt.style.use('ggplot')
plt.figure(figsize=(12, 6))
colors = sns.color_palette("Set2", len(genre_counts))

plt.bar(genre_counts['Genre'], genre_counts['Count'], color=colors)
plt.xlabel('Genre')
plt.ylabel('Jumlah')
plt.title('Distribusi Genre Film')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Menampilkan jumlah missing value pada dataset\
movies.isna().sum()

"""## Dataset Ratings"""

ratings.info()

# Menampilkan banyaknya data ratings, jumlah user, dan rating film.
print('Jumlah user: ', len(ratings.userId.unique()))
print('Jumlah rating: ', len(ratings))
print('Rating: ', ratings.rating.unique())

# menampilkan 5 baris pertama dari dataset "Ratings"
ratings.head()

# Pengecekan deskripsi statistik dataset ratings dengan fungsi describe().
ratings.describe()

# Menampilkan jumlah kolom dan baris dalam dataset
ratings.shape

# Menampilkan data duplikat pada dataset
ratings.duplicated().sum()

# menampilkan jumlah missing value pada dataset
ratings.isna().sum()

# Drop kolom "timestamp"
ratings = ratings.drop('timestamp', axis=1)
ratings.head()

# Menampilkan nilai unik dari variable "rating"
ratings['rating'].value_counts().sort_index(ascending=True)

rating_counts = ratings['rating'].value_counts().sort_index(ascending=True)
rating_counts.plot(kind='bar', figsize=(8, 6), color=sns.color_palette("Purples", n_colors=len(rating_counts)))
plt.xlabel('Rating')
plt.ylabel('Count')
plt.title('Rating Distribution')
plt.show()

"""# Data Preparation"""

movie_rating = pd.merge(movies, ratings, on='movieId')
movie_rating

user_ids = list(set(movie_rating["userId"]))
user_encoded = dict(zip(user_ids, range(len(user_ids))))
userencoded_ = {v: k for k, v in user_encoded.items()}
num_users = len(user_encoded)
num_users

movie_ids = list(set(movie_rating["movieId"]))
movie_encoded = dict(zip(movie_ids, range(len(movie_ids))))
movieencoded_ = {v: k for k, v in movie_encoded.items()}
num_movies = len(movie_encoded)
num_movies

movie_rating = movie_rating.assign(
    user=movie_rating["userId"].apply(lambda x: user_encoded[x]),
    movie=movie_rating["movieId"].apply(lambda x: movie_encoded[x])
)

movie_rating

movie_rating["rating"] = movie_rating["rating"].apply(np.float32)

min_rating = movie_rating["rating"].min()
max_rating = movie_rating["rating"].max()

print(f"Number of users: {num_users}, Number of Movies: {num_movies}, Min rating: {min_rating}, Max rating: {max_rating}")

from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler

# Acak urutan baris
movie_rating = shuffle(movie_rating, random_state=42)

# Ekstraksi fitur dan target
x = movie_rating.loc[:, ["user", "movie"]].to_numpy()

# Normalisasi rating dengan MinMaxScaler
scaler = MinMaxScaler()
y = scaler.fit_transform(movie_rating[["rating"]]).flatten()

train_indices = int(0.75 * movie_rating.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:],
)

embedding_size = 50

class RecommenderNet(keras.Model):
    def __init__(self, num_users, num_movies, embedding_size, **kwargs):
        super(RecommenderNet, self).__init__(**kwargs)
        self.user_embedding = layers.Embedding(
            input_dim=num_users,
            output_dim=embedding_size,
            embeddings_initializer=keras.initializers.he_normal(),
            embeddings_regularizer=keras.regularizers.l2(1e-6)
        )
        self.user_bias = layers.Embedding(input_dim=num_users, output_dim=1)

        self.movie_embedding = layers.Embedding(
            input_dim=num_movies,
            output_dim=embedding_size,
            embeddings_initializer=keras.initializers.he_normal(),
            embeddings_regularizer=keras.regularizers.l2(1e-6)
        )
        self.movie_bias = layers.Embedding(input_dim=num_movies, output_dim=1)

    def call(self, inputs):
        user_idx, movie_idx = inputs[:, 0], inputs[:, 1]

        user_vector = self.user_embedding(user_idx)
        user_bias = self.user_bias(user_idx)
        movie_vector = self.movie_embedding(movie_idx)
        movie_bias = self.movie_bias(movie_idx)

        interaction = tf.reduce_sum(user_vector * movie_vector, axis=1, keepdims=True)
        result = interaction + user_bias + movie_bias

        return tf.keras.activations.sigmoid(result)

model = RecommenderNet(num_users, num_movies, embedding_size)

model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(),
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

history = model.fit(
    x_train,
    y_train,
    batch_size=64,
    epochs=5,
    verbose=2,
    validation_data=(x_val, y_val),
)

fig, ax = plt.subplots()

ax.plot(history.history["loss"], label="train")
ax.plot(history.history["val_loss"], label="validation")
ax.set_title("Loss Model")
ax.set_ylabel("loss")
ax.set_xlabel("epoch")
ax.legend(loc="upper right")

plt.show()

plt.plot(history.history["root_mean_squared_error"])
plt.plot(history.history["val_root_mean_squared_error"])
plt.title("RMSE Model")
plt.ylabel("RMSE")
plt.xlabel("epoch")
plt.legend(["train", "validation"], loc="upper right")
plt.show()

"""# Modeling

Tahap pengembangan model machine learning atau modeling sistem rekomendasi dilakukan untuk memberikan hasil rekomendasi movie terbaik kepada pengguna tertentu berdasarkan rating atau penilaian pengguna terhadap movie tersebut. Tahap modeling yang dilakukan menggunakan teknik pendekatan content-based filtering recommendation dan collaborative filtering recommendation.

## Model Development - Collaborative Filtering
"""

user_id = movie_rating['userId'].sample(1, random_state=42).iloc[0]

movies_watched_ids = movie_rating[movie_rating['userId'] == user_id]['movieId'].values

all_movie_ids = set(movie_encoded.keys())

movies_notwatched_ids = list(all_movie_ids - set(movies_watched_ids))

user_encoder = user_encoded.get(user_id)

user_tensor = tf.constant([user_encoder] * len(movies_notwatched_ids), dtype=tf.int32)

movies_notwatched_encoded = [movie_encoded.get(movie_id) for movie_id in movies_notwatched_ids]
movie_tensor = tf.constant(movies_notwatched_encoded, dtype=tf.int32)

user_movie_array_tf = tf.stack([user_tensor, movie_tensor], axis=1)

ratings_tf = model.predict(user_movie_array_tf).flatten()

top_ratings_indices = np.argsort(ratings_tf)[-10:][::-1]

recommended_movie_ids = [
    movieencoded_.get(movies_notwatched_encoded[index]) for index in top_ratings_indices
]

print("Tampilkan Rekomendasi Film untuk {} Penonton ".format(num_users))

print("====" * 9)

print("Top 5 Film dengan Rating Tertinggi")

print("====" * 9)

user_watched_movies = movie_rating[movie_rating['userId'] == user_id].drop_duplicates(subset=['movieId'])

top_movies_user = user_watched_movies.sort_values(by="rating", ascending=False).head(5)

for index, row in top_movies_user.iterrows():
    print(row.title, ":", row.genres)

print("====" * 6)

print("Top 10 Rekomendasi Film")

print("====" * 6)

recommended_movie_ids = []
for x in top_ratings_indices:
    encoded_movie_id = movies_notwatched_encoded[x]
    movie_id = movieencoded_.get(encoded_movie_id)
    if movie_id not in recommended_movie_ids:
        recommended_movie_ids.append(movie_id)

movie_rating_unique = movie_rating.drop_duplicates(subset="movieId")
recommended_movies = movie_rating_unique[movie_rating_unique["movieId"].isin(recommended_movie_ids)].head(10)
for index, row in recommended_movies.iterrows():
    print(row.title, ":", row.genres)

recommended_movies_sorted = recommended_movies.sort_values(by='rating', ascending=False)

titles = recommended_movies_sorted['title']
ratings = recommended_movies_sorted['rating']

palette = sns.color_palette("Greens", n_colors=len(titles))

plt.figure(figsize=(6, 4))

plt.barh(titles, ratings, color=palette)

plt.xlabel('Rating', fontsize=12)
plt.ylabel('Title', fontsize=12)
plt.title('Rating of Recommended Movies')

# Invert the y-axis
plt.gca().invert_yaxis()

plt.xlim(0, 5)
plt.xticks(np.arange(0, 5.5, 0.5), fontsize=8)

y_axis_labels = [' '.join(title.split()[:2]) for title in titles]
plt.yticks(range(len(titles)), y_axis_labels, fontsize=8)

plt.show()

"""## Model Development - Content Based Filtering"""

no_user_voted = movie_rating.groupby('movieId')['rating'].agg('count')
no_movies_voted = movie_rating.groupby('userId')['rating'].agg('count')

final_dataset = movie_rating.pivot(index='movieId',columns='userId',values='rating')
final_dataset.fillna(0,inplace=True)
final_dataset.head()

final_dataset = final_dataset.loc[no_user_voted[no_user_voted > 10].index,:]
final_dataset

sns.set(style="whitegrid")

f, ax = plt.subplots(1, 1, figsize=(16, 4))

# Convert the Series to a DataFrame with column names 'MovieId' and 'No_of_users_voted'
no_user_voted_df = no_user_voted.reset_index()
no_user_voted_df.columns = ['MovieId', 'No_of_users_voted']

# Use the DataFrame as the data source and the column names for x and y
sns.scatterplot(data=no_user_voted_df, x='MovieId', y='No_of_users_voted', color='red')

plt.axhline(y=10, color='b')
plt.xlabel('MovieId')
plt.ylabel('No. of users voted')
plt.title('Jumlah Pengguna yang Memberikan Rating per Film (Threshold = 10)')
plt.show()

final_dataset = final_dataset.loc[:,no_movies_voted[no_movies_voted > 50].index]
final_dataset

sns.set(style="whitegrid")

f, ax = plt.subplots(1, 1, figsize=(16, 4))

# Convert the Series to a DataFrame with column names 'UserId' and 'No_of_votes_by_user'
no_movies_voted_df = no_movies_voted.reset_index()
no_movies_voted_df.columns = ['UserId', 'No_of_votes_by_user']

# Use the DataFrame as the data source and the column names for x and y
sns.scatterplot(data=no_movies_voted_df, x='UserId', y='No_of_votes_by_user', color='orange')

plt.axhline(y=50, color='g')
plt.xlabel('UserId')
plt.ylabel('No. of votes by user')
plt.title('Jumlah Rating yang Diberikan oleh Setiap Pengguna (Threshold = 50)')
plt.show()

csr_data = csr_matrix(final_dataset.values)
final_dataset.reset_index(inplace=True)

knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=30, n_jobs=-1)
knn.fit(csr_data)

def recommend_movies_by_title(query_title):
    top_n = 10
    matched_movies = movie_rating[movie_rating['title'].str.contains(query_title, case=False, na=False)]

    if not matched_movies.empty:
        target_movie_id = matched_movies.iloc[0]['movieId']
        target_index = final_dataset.index[final_dataset['movieId'] == target_movie_id][0]

        distances, indices = knn.kneighbors(csr_data[target_index], n_neighbors=top_n + 1)

        recommendations = []
        for idx, dist in sorted(zip(indices.flatten(), distances.flatten()), key=lambda x: x[1])[1:]:
            rec_movie_id = final_dataset.iloc[idx]['movieId']
            movie_info = movie_rating[movie_rating['movieId'] == rec_movie_id].iloc[0]
            recommendations.append({
                'Title': movie_info['title'],
                'Genres': movie_info['genres'],
                'Rating': movie_info['rating']
            })

        return pd.DataFrame(recommendations, index=range(1, top_n + 1))

    return "No movies found. Please check your input"

rec = recommend_movies_by_title('Ant-Man')
rec

movie_relevant = 10
movie_recommendation = len(rec)
precision_score = movie_relevant / movie_recommendation

print("Precision: {:.2f}".format(precision_score))