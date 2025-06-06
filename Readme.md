# Laporan Proyek Machine Learning - Nama Anda

## Daftar Isi

- [Project Overview](#project-overview)
- [Business Understanding](#business-understanding)
- [Data Understanding](#data-understanding)
- [Data Preparation](#data-preparation)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Kesimpulan](#kesimpulan)
- [Referensi](#referensi)
 
## Project Overview

Proyek ini membahas permasalahan pengembangan sistem yang mampu memberikan rekomendasi film kepada pengguna, berdasarkan ulasan dari pengguna lain serta kesesuaian profil atau preferensi pengguna terhadap film yang telah dinilai. Sistem rekomendasi tersebut berkaitan erat dengan kemajuan teknologi, khususnya di bidang ekonomi, bisnis, dan industri hiburan.

![dataset-card](https://github.com/user-attachments/assets/dccf83b8-56de-4193-9577-de5336e33cbf)
**Gambar 1. Ilustrasi Sistem Rekomendasi Film**

Di era digital saat ini, sebagian besar masyarakat global, termasuk di Indonesia, kerap menikmati tontonan film. Sejak ditemukannya jaringan kabel dan televisi, film telah menjadi bagian dari industri hiburan yang dinikmati secara komersial melalui siaran televisi. Perbedaannya terletak pada teknologi yang digunakan—jika dahulu penyiaran dilakukan menggunakan gelombang analog, kini telah bertransformasi menjadi penyiaran berbasis digital.

Saat ini, industri film berkembang dengan sangat cepat, baik melalui siaran televisi tradisional maupun platform digital. Beragam jenis tayangan seperti serial, film pendek, dokumenter, dan fiksi ilmiah kini tersedia di televisi maupun bioskop. Umumnya, menonton film menjadi sarana hiburan untuk mengisi waktu luang atau bahkan menjadi hobi bagi sebagian orang. [[2]](https://dinastirev.org/JEMSI/article/download/3087/1859/12951)

Persaingan dalam industri ini semakin intens, terutama sejak munculnya pandemi COVID-19, yang mendorong banyak orang untuk beralih dari TV ke layanan streaming digital. Contohnya adalah platform seperti YouTube, Netflix, Disney+ Hotstar, Amazon Prime, dan lainnya. Layanan-layanan tersebut sangat bergantung pada pelanggan yang berlangganan, sehingga dibutuhkan sistem yang mampu meningkatkan pengalaman pengguna—salah satunya dengan memberikan rekomendasi film yang sesuai dengan minat atau riwayat tontonan pengguna. [[2]](https://dinastirev.org/JEMSI/article/download/3087/1859/12951)

Sistem yang mampu menyarankan film berdasarkan minat atau karakteristik pengguna disebut sistem rekomendasi. Sistem ini bekerja dengan memanfaatkan data yang dikumpulkan, baik dari sisi pengguna maupun dari atribut film itu sendiri. Sebagai contoh, jika seseorang menonton film dengan genre tertentu, maka sistem bisa menyarankan film lain dengan genre serupa. Selain itu, rekomendasi juga dapat diberikan berdasarkan penilaian dan preferensi dari pengguna lain yang memiliki profil atau karakteristik yang mirip. [[3]](https://e-journal.hamzanwadi.ac.id/index.php/infotek/article/view/26083?articlesBySimilarityPage)

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
| Sumber                  | [Kaggle Dataset: MovieLens](https://www.kaggle.com/datasets/snehal1409/movielens)                                     |
| *Usability*             | 6.18                                                                                                                  |
| Jenis dan Ukuran Berkas | 4 csv (3.13 MB)                                                                                                       |

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
