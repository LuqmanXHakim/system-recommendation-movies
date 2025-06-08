# Laporan Proyek Machine Learning - Luqman Hakim

## Daftar Isi

- [Project Overview](#project-overview)
- [Business Understanding](#business-understanding)
- [Data Understanding](#data-understanding)
- [Data Preprocessing](#data-preprocessing)
- [Data Preparation](#data-preparation)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Referensi](#referensi)
 
## Project Overview

Proyek ini membahas permasalahan pengembangan sistem yang mampu memberikan rekomendasi film kepada pengguna, berdasarkan ulasan dari pengguna lain serta kesesuaian profil atau preferensi pengguna terhadap film yang telah dinilai. Sistem rekomendasi tersebut berkaitan erat dengan kemajuan teknologi, khususnya di bidang ekonomi, bisnis, dan industri hiburan.

![dataset-card](https://github.com/user-attachments/assets/dccf83b8-56de-4193-9577-de5336e33cbf)
**Gambar 1. Ilustrasi Sistem Rekomendasi Film**

Di era digital saat ini, sebagian besar masyarakat global, termasuk di Indonesia, kerap menikmati tontonan film. Sejak ditemukannya jaringan kabel dan televisi, film telah menjadi bagian dari industri hiburan yang dinikmati secara komersial melalui siaran televisi. Perbedaannya terletak pada teknologi yang digunakan—jika dahulu penyiaran dilakukan menggunakan gelombang analog, kini telah bertransformasi menjadi penyiaran berbasis digital. [[1]](https://www.researchgate.net/publication/346898118_PERKEMBANGAN_DAN_TRANSFORMASI_TEKNOLOGI_DIGITAL)

Saat ini, industri film berkembang dengan sangat cepat, baik melalui siaran televisi tradisional maupun platform digital. Beragam jenis tayangan seperti serial, film pendek, dokumenter, dan fiksi ilmiah kini tersedia di televisi maupun bioskop. Umumnya, menonton film menjadi sarana hiburan untuk mengisi waktu luang atau bahkan menjadi hobi bagi sebagian orang. [[2]](https://dinastirev.org/JEMSI/article/download/3087/1859/12951)

Persaingan dalam industri ini semakin intens, terutama sejak munculnya pandemi COVID-19, yang mendorong banyak orang untuk beralih dari TV ke layanan streaming digital. Contohnya adalah platform seperti YouTube, Netflix, Disney+ Hotstar, Amazon Prime, dan lainnya. Layanan-layanan tersebut sangat bergantung pada pelanggan yang berlangganan, sehingga dibutuhkan sistem yang mampu meningkatkan pengalaman pengguna—salah satunya dengan memberikan rekomendasi film yang sesuai dengan minat atau riwayat tontonan pengguna. [[2]](https://dinastirev.org/JEMSI/article/download/3087/1859/12951)

Sistem yang mampu menyarankan film berdasarkan minat atau karakteristik pengguna disebut sistem rekomendasi. Sistem ini bekerja dengan memanfaatkan data yang dikumpulkan, baik dari sisi pengguna maupun dari atribut film itu sendiri. Sebagai contoh, jika seseorang menonton film dengan genre tertentu, maka sistem bisa menyarankan film lain dengan genre serupa. Selain itu, rekomendasi juga dapat diberikan berdasarkan penilaian dan preferensi dari pengguna lain yang memiliki profil atau karakteristik yang mirip. [[3]](https://e-journal.hamzanwadi.ac.id/index.php/infotek/article/view/26083?articlesBySimilarityPage)

## Business Understanding

### Problem Statements

Berdasarkan uraian pada latar belakang, maka perumusan masalah dalam proyek ini adalah sebagai berikut:

1. Bagaimana cara mengembangkan sebuah sistem yang mampu memprediksi peringkat atau preferensi pengguna terhadap film yang belum pernah ditonton, berdasarkan riwayat rating dan informasi tambahan seperti genre?

2. Bagaimana merancang algoritma atau model yang dapat memahami preferensi pengguna secara akurat dan memberikan rekomendasi film yang relevan guna meningkatkan pengalaman pengguna dalam menemukan film yang disukai?

### Goals

1. Merancang sistem rekomendasi film yang mampu memperkirakan minat pengguna terhadap film yang belum pernah mereka saksikan, serta menyajikan rekomendasi yang sesuai dengan selera pribadi pengguna untuk meningkatkan kepuasan mereka.
 
2. Mengoptimalkan ketepatan dan relevansi rekomendasi film yang disajikan kepada pengguna dengan memahami preferensi mereka secara lebih mendalam melalui pendekatan seperti collaborative filtering dan content-based filtering.

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

### Solution statements

Terdapat beberapa metode yang bisa diterapkan dalam membangun sistem rekomendasi film:

1. Content-Based Filtering (CBF): Metode ini menggunakan karakteristik dari film, seperti genre maupun ringkasan cerita, untuk mengidentifikasi kesukaan pengguna. Sistem akan menganalisis kesamaan antara atribut film dan preferensi pengguna, lalu merekomendasikan film yang memiliki kesamaan fitur dengan film yang disukai pengguna tersebut.

2. Collaborative Filtering (CF): Metode ini mengandalkan data rating atau penilaian yang diberikan oleh pengguna sebelumnya untuk memprediksi film yang mungkin disukai. Terdapat dua jenis utama: User-Based CF, yang memberikan rekomendasi berdasarkan kesamaan antar pengguna, dan Item-Based CF, yang merekomendasikan film berdasarkan kemiripan dengan film lain yang telah disukai pengguna.

## Data Understanding

*Dataset* yang digunakan dalam proyek ini adalah *dataset* yang diambil dari platform Kaggle. Berikut merupakan detail *dataset* yang digunakan.

**Tabel 1. Informasi Dataset**
|                         | Keterangan                                                                                                            |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Nama Dataset            | MovieLens                                                                                                             |
| Sumber                  | [Kaggle Dataset: MovieLens](https://www.kaggle.com/datasets/snehal1409/movielens)                                     |
| *Usability*             | 6.18                                                                                                                  |
| Jenis dan Ukuran Berkas | 4 csv (3.13 MB)                                                                                                       |

Berdasarkan dataset tersebut, diketahui jumlah data movies berdasarkan atribut movieId adalah sebanyak 9125 data, dan terdapat sebanyak 671 jumlah rating berdasarkan atribut userId dan dikumpulkan dari 9 Januari 1995 sampai dengan 16 Oktober 2016.

Variabel-variabel pada MovieLens dataset adalah sebagai berikut:

movieId : kode unik pengenal film
title : judul film
year : tahun film dirilis
genres : pengelompokan film berdasarkan konten/alur cerita
userId : kode unik pengguna/penonton
rating : penilaian pengguna atas film

- Movies

Berikut merupakan informasi deskripsi variabel kolom atau atribut dari dataset movies, yaitu banyak kolom, nama kolom, jumlah data masing-masing kolom, dan tipe datanya.

**Tabel 2. Deskripsi Variabel Dataset Movies**
| # | Column  | Non-Null Count | Dtype  |
| - | ------- | -------------- | ------ |
| 0 | movieId | 9125           | int64  |
| 1 | title   | 9125           | object |
| 2 | genres  | 9125           | object |

Berikut merupakan isi dari dataset movies yang menampilkan 5 data pertama film.

**Tabel 3. Isi Dataset Movies**
| movieId | title                              | genres                                          |
| ------- | ---------------------------------- | ----------------------------------------------- |
| 1       | Toy Story (1995)                   | Adventure\|Animation\|Children\|Comedy\|Fantasy |
| 2       | Jumanji (1995)                     | Adventure\|Children\|Fantasy                    |
| 3       | Grumpier Old Men (1995)            | Comedy\|Romance                                 |
| 4       | Waiting to Exhale (1995)           | Comedy\|Drama\|Romance                          |
| 5       | Father of the Bride Part II (1995) | Comedy                                          |

Berikut merupakan deskripsi statistik dari dataset movies yang menampilkan jumlah data, rata-rata, standar deviasi, nilai minimal, nilai kuartil bawah atau Q1, kuartil tengah atau Q2 atau median, kuartil atas atau Q3, dan nilai maksimum.

**Tabel 4. Deskripsi Statistik Dataset Movies**
| Statistik    | movieId       |
| ------------ | ------------- |
| count        | 9125.000000   |
| mean         | 31123.291836  |
| std          | 40782.633604  |
| min          | 1.000000      |
| 25%          | 2850.000000   |
| 50% (median) | 6290.000000   |
| 75%          | 56274.000000  |
| max          | 164979.000000 |

- Ratings

Berikut merupakan informasi deskripsi variabel kolom atau atribut dari dataset rating, yaitu banyak kolom, nama kolom, jumlah data masing-masing kolom, dan tipe datanya.

**Tabel 5. Deskripsi Variabel Dataset Ratings**
| No. | Kolom     | Non-Null Count | Dtype   |
| --- | --------- | -------------- | ------- |
| 0   | userId    | 100004         | int64   |
| 1   | movieId   | 100004         | int64   |
| 2   | rating    | 100004         | float64 |
| 3   | timestamp | 100004         | int64   |

Berikut merupakan isi dari dataset ratings yang menampilkan 5 data pertama film.

**Tabel 6. Isi Dataset Ratings**
| userId | movieId | rating | timestamp  |
| ------ | ------- | ------ | ---------- |
| 1      | 31      | 2.5    | 1260759144 |
| 1      | 1029    | 3.0    | 1260759179 |
| 1      | 1061    | 3.0    | 1260759182 |
| 1      | 1129    | 2.0    | 1260759185 |
| 1      | 1172    | 4.0    | 1260759205 |

Berikut merupakan deskripsi statistik dari dataset ratings yang menampilkan jumlah data, rata-rata, standar deviasi, nilai minimal, nilai kuartil bawah atau Q1, kuartil tengah atau Q2 atau median, kuartil atas atau Q3, dan nilai maksimum.

**Tabel 7. Deskripsi Statistik Dataset Ratings**
|       | userId     | movieId    | rating     | timestamp      |
| ----- | ---------- | ---------- | ---------- | -------------- |
| count | 100004.000 | 100004.000 | 100004.000 | 100004.000     |
| mean  | 347.011    | 12548.664  | 3.543      | 1129639000.000 |
| std   | 195.164    | 26369.199  | 1.058      | 191685800.000  |
| min   | 1.000      | 1.000      | 0.500      | 789652000.000  |
| 25%   | 182.000    | 1028.000   | 3.000      | 965847800.000  |
| 50%   | 367.000    | 2406.500   | 4.000      | 1110422000.000 |
| 75%   | 520.000    | 5418.000   | 4.000      | 1296192000.000 |
| max   | 671.000    | 163949.000 | 5.000      | 1476641000.000 |

- Pengecekan Missing Value

Proses pengecekan data yang hilang atau missing value dilakukan pada masing-masing dataset movies dan ratings. Berdasarkan hasil pengecekan, ternyata tidak ada data yang hilang atau missing value dari dataset tersebut.

- Pengecekan Data Duplikat

Proses pengecekan data yang hilang atau missing value dilakukan pada masing-masing dataset movies dan ratings. Berdasarkan hasil pengecekan, ternyata tidak ada data yang hilang atau missing value dari dataset tersebut.

Visualisasi Dataset

Grafik 1 : Visualisasi sebaran genre film

![genre film](https://github.com/user-attachments/assets/8b21346a-8690-4e60-a830-3fee439625ad)

Grafik 1 memperlihatkan bahwa genre terbanyak dalam daftar film adalah Drama dan Comedy, sedangkan posisi terendah adalah Film-Noir.

Grafik 2: Visualisasi Rating

![rating-distribusi](https://github.com/user-attachments/assets/70673d00-b584-489d-9297-546b94d4a701)

Grafik 2, bisa dilihat bahwa pengguna paling banyak memberikan rating 4.0 disusul rating 3.0 dan rating 5.0

## Data Preparation

Tahap data preparation merupakan proses pengolahan data mentah agar siap digunakan oleh model machine learning. Pada tahap ini, dilakukan beberapa langkah penting seperti penanganan missing value, pengecekan data duplikat, serta pemisahan atribut genre pada dataset film.

1. Penggabungan antara dataset movies dan ratings menggunakan fungsi merge dari library Pandas dengan mengacu pada kolom movieId yang terdapat pada kedua dataset tersebut.

**Tabel 8. Penggabungan Data Movies dan Ratings**
| movieId | genres                                             | title                                              | year | userId | rating |
| ------- | -------------------------------------------------- | -------------------------------------------------- | ---- | ------ | ------ |
| 1       | \[Adventure, Animation, Children, Comedy, Fantasy] | Toy Story                                          | 1995 | 7      | 3.0    |
| 1       | \[Adventure, Animation, Children, Comedy, Fantasy] | Toy Story                                          | 1995 | 9      | 4.0    |
| 1       | \[Adventure, Animation, Children, Comedy, Fantasy] | Toy Story                                          | 1995 | 13     | 5.0    |
| 1       | \[Adventure, Animation, Children, Comedy, Fantasy] | Toy Story                                          | 1995 | 15     | 2.0    |
| 1       | \[Adventure, Animation, Children, Comedy, Fantasy] | Toy Story                                          | 1995 | 19     | 3.0    |
| ...     | ...                                                | ...                                                | ...  | ...    | ...    |
| 161944  | \[Drama]                                           | The Last Brickmaker in America                     | 2001 | 287    | 5.0    |
| 162376  | \[Drama]                                           | Stranger Things                                    | NaN  | 73     | 4.5    |
| 162542  | \[Romance, Thriller]                               | Rustom                                             | 2016 | 611    | 5.0    |
| 162672  | \[Adventure, Drama, Romance]                       | Mohenjo Daro                                       | 2016 | 611    | 3.0    |
| 163949  | \[Documentary]                                     | The Beatles: Eight Days a Week - The Touring Years | 2016 | 547    | 5.0    |



2. Pengecekan Missing Value

Proses pengecekan data yang hilang atau missing value dilakukan pada masing-masing dataset movies dan ratings. Berdasarkan hasil pengecekan, ternyata tidak ada data yang hilang atau missing value dari dataset tersebut.

3. Pengecekan Data Duplikat

Proses pengecekan data yang hilang atau missing value dilakukan pada masing-masing dataset movies dan ratings. Berdasarkan hasil pengecekan, ternyata tidak ada data yang hilang atau missing value dari dataset tersebut.

4. Eksplorasi Data
Eksplorasi data bertujuan untuk menggali informasi yang lebih dalam dari dataset melalui analisis statistik dan visualisasi.
Langkah ini mencakup pembuatan grafik seperti histogram, scatter plot, dan boxplot untuk melihat distribusi data serta hubungan antar variabel.

5. Pembagian Data
Supaya model machine learning bisa belajar dan diuji dengan baik, data harus dipisahkan menjadi data pelatihan dan data pengujian.
Biasanya pembagian dilakukan secara acak dengan rasio tertentu seperti 80:20 atau 70:30, untuk memastikan evaluasi model yang adil dan menghindari overfitting.

## Modeling

1. **Collaborative Filtering (CF)**:
   Metode ini memanfaatkan informasi interaksi antar pengguna dan item, seperti riwayat aktivitas pengguna. CF terbagi menjadi dua tipe utama: pendekatan berbasis pengguna (User-Based) dan berbasis item (Item-Based).

   **Kelebihan CF**:
   - Cocok untuk item tanpa atribut: CF dapat bekerja dengan baik dalam merekomendasikan item baru karena sistem ini lebih fokus pada pola perilaku pengguna daripada karakteristik item.
   
   - Mampu menghasilkan rekomendasi beragam: CF mampu menemukan rekomendasi yang unik atau tidak terduga, karena sistem mengenali pola dari perilaku pengguna yang tidak selalu terlihat dari atribut item secara langsung.
   
   - Tidak tergantung pada deskripsi item: CF tidak memerlukan informasi fitur atau atribut dari item, sehingga dapat digunakan pada beragam domain produk atau layanan.
   
   **Kekurangan CF**:
   - Memerlukan data pengguna yang cukup: Untuk bekerja secara optimal, CF membutuhkan data interaksi pengguna yang memadai. Ketika data pengguna masih minim, kualitas rekomendasi bisa menurun.
   
   - Masalah kelangkaan data (sparsity): Pada sistem dengan jumlah pengguna dan item yang besar, banyak interaksi yang tidak tercatat, sehingga matriks interaksi menjadi sangat jarang terisi dan membuat rekomendasi menjadi kurang akurat.
   
   - Efek filter bubble: CF cenderung memberikan rekomendasi berdasarkan popularitas atau kecenderungan pengguna sebelumnya, yang bisa membatasi keragaman konten yang ditampilkan.

Proyek ini memanfaatkan pendekatan Neural Network dalam sistem Collaborative Filtering dengan parameter sebagai berikut:
```
loss = Binary Crossentropy, optimizer = Adam, metric = Root Mean Squared Error (RMSE)
```
RecommenderNet adalah algoritma rekomendasi berbasis jaringan saraf tiruan (neural network), yang dirancang untuk menangkap interaksi kompleks antara pengguna dan item. Model ini dilatih menggunakan data preferensi pengguna untuk mengidentifikasi pola mendalam. Setelah pelatihan selesai, model dapat memprediksi peringkat atau rekomendasi berdasarkan input profil pengguna atau fitur item.

  **Kelebihan**:
  - Mampu memahami struktur data yang kompleks dan non-linier.
  
  - Dapat belajar dari banyak fitur sekaligus untuk menghasilkan rekomendasi yang lebih akurat.
  
  - Efektif dalam menangani dataset besar dengan variabel tinggi.z
  
  **Kekurangan**:
  - Proses pelatihan dan implementasi lebih kompleks dibandingkan algoritma tradisional.
  
  - Membutuhkan perangkat keras dan waktu komputasi yang lebih besar.
  
  - Kinerja model sangat bergantung pada jumlah dan kualitas data pelatihan yang tersedia.

2. **Content-Based Filtering (CBF)**:
Content-Based Filtering bekerja dengan memanfaatkan informasi atau karakteristik dari item untuk memberikan rekomendasi kepada pengguna. Dalam konteks sistem rekomendasi film, CBF akan mempertimbangkan atribut film seperti genre, sinopsis, atau pemeran utama untuk menentukan film mana yang sesuai dengan preferensi pengguna.

   **Keunggulan Content-Based Filtering** :
   
     - Rekomendasi yang Personal: Sistem CBF mampu memberikan hasil yang disesuaikan dengan minat masing-masing pengguna berdasarkan karakteristik item yang pernah disukai.
     
     - Penjelasan yang Jelas: Karena berdasarkan fitur item, pengguna dapat mengetahui alasan mengapa suatu item direkomendasikan.
     
     - Tidak Butuh Data dari Pengguna Lain: Sistem ini tidak membutuhkan riwayat interaksi dari pengguna lain sehingga tetap bisa bekerja secara individual.
   
   **Kelemahan Content-Based Filtering** :
   
     - Kurang Variasi: Rekomendasi yang diberikan seringkali terlalu mirip dengan preferensi sebelumnya, sehingga tidak banyak memberikan eksplorasi item baru.
     
     - Ketergantungan pada Fitur Item: Jika atribut item tidak lengkap atau tidak merepresentasikan minat pengguna dengan baik, rekomendasi bisa menjadi tidak akurat.
     
     - Masalah Cold Start: CBF kesulitan memberikan rekomendasi untuk item yang benar-benar baru karena belum ada informasi kontennya yang bisa digunakan.

   Pendekatan yang digunakan dalam proyek ini adalah menggunakan algoritma K-Nearest Neighbors (KNN) dalam implementasi Content-Based Filtering. Pengaturan parameter yang digunakan adalah:
   ```
   metric='cosine', algorithm='brute', n_neighbors=30, n_jobs=-1
   ```
   Algoritma KNN dengan cosine similarity digunakan untuk mengukur kemiripan antar item berdasarkan fitur mereka. Cosine similarity sangat cocok digunakan untuk data berbentuk vektor seperti representasi teks. Proses KNN melibatkan penghitungan tingkat kesamaan antara item yang dicari dengan item lainnya dalam dataset. Kemudian, K item yang paling mirip dipilih untuk menghasilkan rekomendasi.
   
   **Keunggulan KNN Cosine**:
   
   - Sederhana dan mudah untuk diimplementasikan.
   
   - Tidak memerlukan tahap pelatihan yang kompleks.
   
   **Kekurangan KNN Cosine**:
   
   - Kurang efisien pada dataset berukuran besar karena harus menghitung kesamaan untuk semua item.
   
   - Memilih nilai K dan jenis metrik yang optimal bisa menjadi tantangan tersendiri.
   
   Sistem ini memberikan rekomendasi film berdasarkan masukan pengguna. Sebagai contoh, ketika pengguna mengetikkan kata kunci "Ant-Man", sistem akan menampilkan film-film yang memiliki kemiripan konten dengan film tersebut.

   | No. | Title                               | Genres                                       | Rating |
   | --- | ----------------------------------- | -------------------------------------------- | ------ |
   | 1   | Man of Steel                        | \[Action, Adventure, Fantasy, Sci-Fi, IMAX]  | 3.0    |
   | 2   | Pacific Rim                         | \[Action, Adventure, Sci-Fi, IMAX]           | 2.0    |
   | 3   | Avengers: Age of Ultron             | \[Action, Adventure, Sci-Fi]                 | 3.5    |
   | 4   | Oblivion                            | \[Action, Adventure, Sci-Fi, IMAX]           | 4.0    |
   | 5   | Edge of Tomorrow                    | \[Action, Sci-Fi, IMAX]                      | 3.0    |
   | 6   | Captain America: The First Avenger  | \[Action, Adventure, Sci-Fi, Thriller, War]  | 4.0    |
   | 7   | Iron Man 2                          | \[Action, Adventure, Sci-Fi, Thriller, IMAX] | 4.5    |
   | 8   | World War Z                         | \[Action, Drama, Horror, IMAX]               | 3.0    |
   | 9   | Captain America: The Winter Soldier | \[Action, Adventure, Sci-Fi, IMAX]           | 4.0    |
   | 10  | Thor                                | \[Action, Adventure, Drama, Fantasy, IMAX]   | 3.5    |


## Evaluation

Proyek ini memakai Root Mean Squared Error (RMSE) sebagai metrik evaluasi dan Binary Cross Entropy sebagai fungsi loss untuk model Collaborative Filtering, sedangkan Precision digunakan sebagai ukuran evaluasi dalam metode Content-Based Filtering.

1. Root Mean Squared Error (RMSE)
  RMSE merupakan salah satu metrik evaluasi yang digunakan untuk menghitung seberapa jauh hasil prediksi model menyimpang dari nilai aslinya secara rata-rata. Rumus perhitungannya adalah:
  
  ```RMSE = √(Σ(yi - ŷi)² / n)```
  dengan keterangan:
  
  yi adalah nilai aktual
  
  ŷi adalah hasil prediksi
  
  Σ menunjukkan penjumlahan dari seluruh data
  
  n adalah jumlah total sampel
  
  Cara kerja RMSE dapat dijelaskan sebagai berikut:
  Model melakukan prediksi terhadap setiap data (ŷi), lalu menghitung perbedaan antara nilai aktual (yi) dan prediksi. Selisih ini dikuadratkan agar nilai negatif tidak saling meniadakan. Semua hasil kuadrat kemudian dijumlahkan dan dibagi dengan jumlah data. Akhirnya, hasil tersebut diakarkan untuk mendapatkan nilai RMSE.
  
  Dengan kata lain, RMSE mengukur rata-rata kesalahan kuadrat antara nilai sebenarnya dan hasil prediksi, lalu mengambil akar kuadrat dari nilai tersebut.
  
  Karakteristik RMSE:
  - Seluruh perbedaan antara nilai prediksi dan aktual diperhitungkan secara merata, namun dikuadratkan agar hasil negatif tidak mengurangi total.
  
  - RMSE menekankan kesalahan besar karena kuadratnya memberi bobot lebih tinggi pada error yang besar.
  
  - Skor RMSE dinyatakan dalam satuan yang sama seperti data target, sehingga memudahkan dalam interpretasi.
  
  Nilai RMSE yang lebih kecil menandakan performa model yang lebih baik. Oleh karena itu, model dengan RMSE lebih rendah umumnya dianggap lebih akurat dibandingkan model dengan nilai RMSE yang tinggi.

  Grafik 3 Validation RMSE vs Train RMSE
  ![RMSE model](https://github.com/user-attachments/assets/617725a1-2e7c-4012-b284-30c07920f141)

2. **Binary Cross Entropy (BCE)**, juga dikenal sebagai Logistic Loss, merupakan fungsi loss yang umum digunakan dalam permasalahan klasifikasi dua kelas (biner). Metrik ini mengevaluasi seberapa akurat model memprediksi kelas sebenarnya dan seberapa besar tingkat keyakinan model terhadap prediksi tersebut.

   Cara Kerja Binary Cross Entropy
   BCE memanfaatkan logaritma natural (log) untuk menghitung tingkat kesalahan prediksi terhadap target biner. Rumus perhitungannya adalah:
   
   ```Binary Cross-Entropy Loss = -Σ(y * log(p) + (1 - y) * log(1 - p))```
   
   Keterangan:
   
   y adalah label sebenarnya (0 atau 1)
   
   p adalah probabilitas hasil prediksi model
   
   Σ menyatakan penjumlahan dari seluruh data
   
   Langkah kerjanya sebagai berikut:
   Untuk setiap data, dibandingkan antara label asli (y) dengan probabilitas hasil prediksi (p).
   
   Jika y = 1, maka yang dihitung adalah log(p)
   
   Jika y = 0, maka yang dihitung adalah log(1 - p)
   Hasil log tersebut diakumulasi untuk seluruh data, kemudian diberikan tanda negatif agar kesalahan yang besar menjadi lebih tampak dan memiliki kontribusi lebih besar terhadap nilai loss.
   
   Tujuan dan Karakteristik
   Binary Cross Entropy berfungsi untuk mengukur kedekatan antara prediksi dan label aktual, sekaligus mencerminkan ketidakpastian prediksi. Semakin mendekati nilai aktual (0 atau 1), semakin kecil nilai loss-nya.
   Nilai BCE yang rendah menunjukkan bahwa model mampu memberikan probabilitas yang tinggi terhadap kelas positif (jika label = 1), dan probabilitas rendah terhadap kelas negatif (jika label = 0).
   Tujuan dari pelatihan model dengan fungsi loss ini adalah meminimalkan nilai BCE agar model menghasilkan prediksi yang lebih akurat dan meyakinkan.

   Grafik 4 Validation Loss vs Train Loss
   ![Loss Model](https://github.com/user-attachments/assets/108eda1b-1411-49eb-9f14-4ce377868835)


## Referensi

[1] M. Danuri, "Perkembangan dan Transformasi Teknologi Digital", *INFOKAM*, no. 2, pp. 116-123, Sep. 2019, Retrieved from: https://www.researchgate.net/publication/346898118_PERKEMBANGAN_DAN_TRANSFORMASI_TEKNOLOGI_DIGITAL.

[2] Pergeseran Preferensi Menonton dan Transformasi Media Digital 
di Indonesia Akibat Dominasi Netflix https://dinastirev.org/JEMSI/article/download/3087/1859/12951

[3] Prototipe Sistem Rekomendasi Film Indonesia Menggunakan Pendekatan Content Based Filtering dan Metode Vector Space Model https://e-journal.hamzanwadi.ac.id/index.php/infotek/article/view/26083?articlesBySimilarityPage
