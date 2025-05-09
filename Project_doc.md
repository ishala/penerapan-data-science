# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang sudah berdiri sejak tahun 2000. Meskipun sudah mencetak banyak lulusan dengan reputasi baik, namun masih terdapat banyak siswa yang tidak menyelesaikan pendidikannya alias *dropout*. Jumlah *dropout* yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

Jaya Jaya Institut terkendala pada banyaknya jumlah siswanya yang tidak menyelesaikan pendidikannya hingga akhir alias *dropout*. Terdapat beberapa parameter yang dapat dipertimbangkan untuk mitigasi atau minimalisir adanya siswa yang ter-*dropout*. 

Dari sini perlu adanya analisa lebih lanjut terhadap kondisi siswa-siswa yang masih maupun pernah menjadi siswa di Jaya Jaya Institut.

### Cakupan Proyek

Proyek ini akan menjawab pertanyaan-pertanyaan bisnis sebagai berikut:

1. Berapa banyak jumlah siswa berdasarkan kategori perkawinan? Marital_status
2. Bagaimana hubungan prioritas pilihan kelas pada kelas yang dipilih? Application_order, Course
3. Seberapa banyak siswa yang melakukan *drop out* berdasarkan kelas yang dipilih dengan waktu dilaksanakannya kelas? Course, Status,daytime_evening_attendace
4. Berapa nilai minimum, rata-rata, dan maksimum nilai masuk ke kelas yang dipilih terhadap status kelulusan siswa? Admission_grade (feature engineering hitung selisih batas atas dan batas bawah) Course, Status
5. Berapa presentase *debtor* pada setiap kategori status siswa? Debtor, Status
6. Berapa rata-rata umur siswa pada saat mengambil kelas terhadap kategori status siswa? Age_at_enrollment, Status
7. Berapa tingkat *unemployment rate* pada setiap kategori kelas? Unemployment_rate, Course
8. Berapa total *units* dengan status *enrolled* terhadap status mahasiswa berdasarkan nilai modusnya? Total_units_enrolled = 1st_sem_enrolled + 2nd_sem_enrolled -> mod metabase (sql), Status
9. Berapa total *units* dengan status *approved* terhadap status mahasiswa berdasarkan nilai modusnya? Total_units_approved = 1st_sem_approved + 2nd_sem_approved -> mod metabase (sql), Status
10. Berapa rata-rata *approval rate* dari *total units approved* dan *total units enrolled* terhadap status mahasiswa? Approval_rate = Total_units_approved / Total_units_enrolled -> mean, Status
11. Berapa rata-rata *grade* siswa dengan *enrolled units* terhadap status siswa? Total_credits = 1st_sem_enrolled + 2nd_sem_enrolled -> Weighted_avg_grade = ((1st_sem_grade * 1st_sem_enrolled) + (2nd_sem_grade * 2nd_sem_enrolled)) / Total_credits
12. Berapa banyak *units* yang tidak memiliki status *evaluation* pada setiap siswa terhadap status siswa? Total_units_without_eval = 1st_sem_without_evaluations + 2nd_sem_without_evaluations, Status
13. Berapa rata-rata beban tekanan ekonomi dari segi *unemployment rate*, *inflation rate* dan *marital status* setiap siswa terhadap statusnya? Econ_pressure = (Unemployment_rate × Inflation_rate) * 2 if marital_status != 'single'

**Hal Yang Akan Dikerjakan**

Membentuk model data berdasarkan wawasan yang ditemukan dari hasil eksplorasi dan analisis data. Data yang digunakan dikategorikan menjadi dua jenis: data demografis siswa, data kualifikasi siswa, dan data kurikulum siswa.

**Apa yang Dituju?**

Mengelompokkan data ke dalam kategori yang mudah dipahami sehingga memudahkan ketika proses visualisasi dan pengambilan makna data dalam rangka memahami pengaruh performa siswa yang mempengaruhi tingkat *Dropout*.

**Batasan dalam Proyek**

Proyek ini hanya mencakup penggalian informasi, pembuatan model prediksi, serta pembuatan produk *Website* yang mengimplementasikan model prediksi. Proyek tidak mencakup pengambilan keputusan kebijakan secara langsung maupun pengumpulan data lanjutan di luar dataset yang telah disediakan. Semua *insight* dan rekomendasi yang diberikan merupakan hasil dari analisis terhadap data historis yang tersedia.

**Output Pekerjaan**

Visualisasi interaktif berbentuk *Business Dashboard* yang menampilkan beberapa metrik, serta produk *Website* prediksi yang mengimplementasikan model yang sudah dibuat berbasis Streamlit.
### Persiapan

Sumber data: [Students Performance Data](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

**Setup environment:**

**1. Python Environment**

- Buat sebuah *virtual environment* seperti venv atau conda. Disini penulis menggunakan conda dari miniconda. Buat dengan perintah:

```
conda create --name myvenv python=3.11
```
- Lalu aktifkan venv yang sudah dibuat dengan perintah:

```
conda activate myenv
```
- Setelah mengaktifkan venv yang dibuat, maka dilanjutkan dengan menginstall *library* atau dependensi yang digunakan untuk mengolah data. Berikut contoh *library*-*library* yang penulis gunakan:

```
pip install pandas sqlalchemy psycopg2 python-dotenv scikit-learn tensorflow streamlit
```
**2. Streamlit**

- Buka terminal dari VSCode atau dengan terminal dari PC. Arahkan direktori menuju direktori dimana **app.py** berada.
- Lalu jalankan perintah pada terminal dengan perintah berikut:

```
streamlit run app.py
```
- Setelah itu klik Local URL atau akses di browser dengan url http://localhost:8501

**3. Dashboard (Metabase)**

- Untuk menjalankan dashboard menggunakan **Metabase**, pertama pastikan file metabase.db.mv.db sudah tersedia. Selain itu, juga Docker sudah terpasang pada device. Lalu jalankan perintah berikut:

```
docker run -d \
  -p 3000:3000 \
  -v /path/ke/metabase.db:/metabase.db \
  -e "MB_DB_FILE=/metabase.db/metabase.db.mv.db" \
  --name metabase metabase/metabase
```

- Perintah di atas akan membuat sebuah docker container yang berisi image **Metabase**. Dikarenakan container berjalan pada port 3000 secara lokal. Maka untuk mengaksesnya dilakukan dengan cara membuat web browser lalu tuliskan alamat url seperti berikut:

```
http://localhost:3000
```

- Seharusnya saat ini **Metabase** sudah terbuka di dalam browser anda.
## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
