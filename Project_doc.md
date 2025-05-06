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


### Persiapan

Sumber data: [Students Performance Data](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

Setup environment:
```

```

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
