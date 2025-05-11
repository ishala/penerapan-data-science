# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang sudah berdiri sejak tahun 2000. Meskipun sudah mencetak banyak lulusan dengan reputasi baik, namun masih terdapat banyak siswa yang tidak menyelesaikan pendidikannya alias *dropout*. Jumlah *dropout* yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

Jaya Jaya Institut terkendala pada banyaknya jumlah siswanya yang tidak menyelesaikan pendidikannya hingga akhir alias *dropout*. Terdapat beberapa parameter yang dapat dipertimbangkan untuk mitigasi atau minimalisir adanya siswa yang ter-*dropout*. 

Dari sini perlu adanya analisa lebih lanjut terhadap kondisi siswa-siswa yang masih maupun pernah menjadi siswa di Jaya Jaya Institut.

### Cakupan Proyek

Proyek ini akan menjawab pertanyaan-pertanyaan bisnis sebagai berikut:

1. Berapa banyak jumlah siswa berdasarkan kategori perkawinan?
2. Bagaimana hubungan prioritas pilihan kelas pada kelas yang dipilih? What is the Course Prioritize Correlations by Their Min-Max Application Order Category?
3. Seberapa banyak siswa yang melakukan *drop out* berdasarkan kelas yang dipilih?
4. Berapa banyak siswa yang melakukan *drop out* berdasarkan waktu pengambilan kelas?
5. Berapa nilai minimum, rata-rata, dan maksimum nilai masuk ke kelas yang dipilih terhadap status kelulusan siswa?
6. Berapa presentase *debtor* pada setiap kategori status siswa?
7. Berapa rata-rata umur siswa pada saat mengambil kelas terhadap kategori status siswa? 
8. Berapa tingkat *unemployment rate* pada setiap kategori kelas?
9. Berapa total *units enrolled* terhadap status mahasiswa berdasarkan nilai kumulatifnya?
10. Berapa total *units approved* terhadap status mahasiswa berdasarkan nilai kumulatifnya?
11. Berapa rata-rata *approval rate* dari *total units approved* dan *total units enrolled* terhadap status mahasiswa?
12. Berapa rata-rata *grade* siswa dengan *enrolled units* terhadap status siswa?
13. Berapa banyak setiap status siswa terhadap nilai *total units* tidak dievaluasi?
14. Berapa rata-rata beban tekanan ekonomi dari segi *unemployment rate*, *inflation rate* dan *marital status* setiap siswa terhadap statusnya?

**Hal Yang Akan Dikerjakan**

Membentuk model data berdasarkan wawasan yang ditemukan dari hasil eksplorasi dan analisis data. Data yang digunakan dikategorikan menjadi dua jenis: data demografis siswa, data kualifikasi siswa, dan data kurikulum siswa.

**Apa yang Dituju?**

Mengelompokkan data ke dalam kategori yang mudah dipahami sehingga memudahkan ketika proses visualisasi dan pengambilan makna data dalam rangka memahami pengaruh performa siswa yang mempengaruhi tingkat *Dropout*.

**Batasan dalam Proyek**

Proyek ini hanya mencakup penggalian informasi, pembuatan model prediksi, serta pembuatan *prototype* yang mengimplementasikan model prediksi. Proyek tidak mencakup pengambilan keputusan kebijakan secara langsung maupun pengumpulan data lanjutan di luar dataset yang telah disediakan. Semua *insight* dan rekomendasi yang diberikan merupakan hasil dari analisis terhadap data historis yang tersedia.

**Output Pekerjaan**

Visualisasi interaktif berbentuk *Business Dashboard* yang menampilkan beberapa metrik, serta *prototype* prediksi yang mengimplementasikan model yang sudah dibuat berbasis Streamlit.
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

**2. Dashboard (Metabase)**

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
*Business Dashboard* yang dibuat saat ini terdapat satu halaman, yang mana terbagi menjadi dua *section* yang berisi informasi *students performance* terhadap korelasinya dengan nilai *status*. Section pertama bernama **Student's Background** yang berisi mengenai informasi latar belakang siswa dan yang kedua bernama **Student's Curricular Things** yang berisi mengenai informasi performa siswa terhadap kurikulum yang diberikan. Untuk informasi lebih detail adalah sebagai berikut:

### *Section* Pertama: Student's Background

**1. Student Count By Marital Status**

Berdasarkan visualisasi diagram donat, mayoritas siswa berada dalam kategori status perkawinan **Single** dengan proporsi sebesar 88,6%, menunjukkan bahwa hampir seluruh populasi siswa belum menikah. Sementara itu, siswa yang sudah menikah hanya mencakup 8,6% dari total, dan sisanya 2,8% berada dalam kategori **Other**. Data ini mengindikasikan bahwa sebagian besar siswa masih lajang, yang kemungkinan berkaitan dengan usia mereka yang relatif muda atau fokus pada pendidikan sebelum membangun rumah tangga. Pernyataan ini menjawab pertanyaan "Berapa banyak jumlah siswa berdasarkan kategori perkawinan?".

**2. Average of Age at Enrollment by Student Status**

Berdasarkan visualisasi diagram batang, terlihat bahwa rata-rata usia saat pendaftaran bervariasi berdasarkan status siswa. Siswa dengan status tertentu memiliki usia rata-rata pendaftaran tertinggi, sekitar 26 tahun, sementara dua kelompok lainnya memiliki rata-rata usia sekitar 22 hingga 23 tahun. Hal ini menunjukkan bahwa kelompok siswa tertentu mungkin terdiri dari individu yang kembali menempuh pendidikan setelah periode tertentu di luar dunia akademik, sedangkan kelompok lainnya didominasi oleh siswa yang melanjutkan pendidikan segera setelah menyelesaikan jenjang sebelumnya. Pernyataan ini menjawab pertanyaan "Berapa rata-rata umur siswa pada saat mengambil kelas terhadap kategori status siswa?".

**3. Debtor's Percentage by Student Status**

Berdasarkan visualisasi diagram donat bertingkat, dapat disimpulkan bahwa sebagian besar siswa yang lulus (graduate) tidak memiliki utang (debtor) dengan persentase yang dominan. Sebaliknya, pada kelompok siswa yang dropout, proporsi yang memiliki utang jauh lebih besar dibandingkan yang tidak, menunjukkan korelasi antara status sebagai debitur dan kemungkinan putus studi. Untuk siswa yang masih terdaftar (enrolled), proporsi antara yang memiliki dan tidak memiliki utang tampak lebih seimbang. Temuan ini mengindikasikan bahwa masalah finansial, yang tercermin dari status debitur, dapat berpengaruh terhadap kelulusan atau putusnya studi mahasiswa. Pernyataan ini menjawab pertanyaan "Berapa presentase *debtor* pada setiap kategori status siswa?".

**4. Average of Economic Pressure By Student Status**

Berdasarkan visualisasi diagram donat tersebut, terlihat bahwa tekanan ekonomi rata-rata paling tinggi dialami oleh siswa yang putus studi (*dropout*) dengan persentase sebesar 40%. Sementara itu, siswa yang masih terdaftar (*enrolled*) mengalami tekanan ekonomi sebesar 31%, dan yang paling rendah adalah siswa yang telah lulus (*graduate*) dengan tekanan ekonomi sebesar 29%. Data ini mengindikasikan bahwa semakin tinggi tekanan ekonomi yang dirasakan oleh siswa, semakin besar kemungkinan mereka untuk tidak menyelesaikan studi atau mengalami kesulitan dalam mempertahankan status akademiknya. Pernyataan ini menjawab pertanyaan "Berapa rata-rata beban tekanan ekonomi dari segi *unemployment rate*, *inflation rate* dan *marital status* setiap siswa terhadap statusnya?".

### *Section* Kedua: Student's Curricular Things

**1. Average of Approval Rate by Student Status**

Berdasarkan diagram batang tersebut, terlihat bahwa rata-rata tingkat persetujuan (approval rate) tertinggi dimiliki oleh mahasiswa yang telah lulus (graduate) dengan nilai 0,9, diikuti oleh mahasiswa yang masih aktif (enrolled) sebesar 0,67, dan yang terendah adalah mahasiswa yang putus studi (dropout) dengan nilai hanya 0,34. Hal ini menunjukkan adanya hubungan positif antara status kelulusan dengan tingkat approval rate, di mana mahasiswa yang berhasil menyelesaikan studinya cenderung mendapatkan tingkat persetujuan yang lebih tinggi dibandingkan dengan yang belum atau tidak menyelesaikan studi. Pernyataan ini menjawab pertanyaan "Berapa rata-rata *approval rate* dari *total units approved* dan *total units enrolled* terhadap status mahasiswa?".

**2. Average of Weighted Avg Grade by Student Status**

Grafik batang ini menunjukkan bahwa terdapat hubungan kuat antara performa akademik dan status mahasiswa, di mana mahasiswa **Graduate** memiliki rata-rata nilai tertinggi sebesar **93.71**, disusul oleh mahasiswa yang masih **Enrolled** dengan nilai **74.96**, dan yang **Dropout** mencatat nilai paling rendah yaitu **50.19**. Pola ini mengindikasikan bahwa semakin tinggi nilai akademik mahasiswa, semakin besar kemungkinan mereka untuk menyelesaikan studi, sementara nilai rendah cenderung berasosiasi dengan risiko putus studi yang lebih tinggi, sehingga prestasi akademik terbukti menjadi faktor krusial dalam keberhasilan pendidikan mahasiswa. Pernyataan ini menjawab pertanyaan "Berapa rata-rata *grade* siswa dengan *enrolled units* terhadap status siswa?".

**3. Cumulative Count of Total Units Approved by Student Status**

Grafik ini menunjukkan akumulasi jumlah mahasiswa berdasarkan total unit yang berhasil disetujui, dan memperlihatkan bahwa mahasiswa **Graduate** secara konsisten menyelesaikan lebih banyak unit dibandingkan dua kelompok lainnya. Kurva hijau (**Graduate**) naik tajam hingga sekitar 15 unit, kemudian stabil di angka tertinggi sekitar 2.300 mahasiswa, menandakan bahwa mayoritas mahasiswa yang lulus telah menyelesaikan banyak unit. Sebaliknya, kurva merah (**Dropout**) dan kuning (**Enrolled**) mulai melambat jauh lebih awal, masing-masing berhenti di sekitar 1.400 dan 800 mahasiswa, menunjukkan bahwa **dropout** dan mahasiswa aktif cenderung menyelesaikan unit dalam jumlah lebih sedikit, yang dapat mencerminkan tantangan akademik atau administratif yang mereka hadapi. Pernyataan ini menjawab pertanyaan "Berapa total *units approved* terhadap status mahasiswa berdasarkan nilai kumulatifnya?".

**4. Cumulative Count of Total Units Enrolled by Student Status**

Grafik ini menunjukkan akumulasi jumlah mahasiswa berdasarkan total unit yang diambil (**enrolled**), dan memperlihatkan bahwa mahasiswa **Graduate** cenderung mengambil lebih banyak unit dibandingkan mahasiswa Dropout maupun Enrolled. Kurva hijau (**Graduate**) mengalami peningkatan tajam hingga sekitar 15 unit dan kemudian melandai, menunjukkan bahwa sebagian besar mahasiswa yang lulus telah mengambil banyak unit. Sementara itu, kurva merah (**Dropout**) dan kuning (**Enrolled**) meningkat secara lebih moderat dan berhenti pada level yang lebih rendah, yaitu sekitar 1.400 dan 800 mahasiswa. Hal ini menunjukkan bahwa dropout dan mahasiswa yang masih aktif cenderung belum atau tidak mengambil jumlah unit sebanyak mahasiswa yang sudah lulus, yang bisa berkaitan dengan faktor seperti keterbatasan waktu, kendala akademik, atau keputusan untuk berhenti sebelum menyelesaikan program. Pernyataan ini menjawab pertanyaan "Berapa total *units enrolled* terhadap status mahasiswa berdasarkan nilai kumulatifnya?".

**5. Count of Student Status and Total Units With No Evaluation**

Grafik ini menunjukkan distribusi status mahasiswa berdasarkan jumlah unit tanpa evaluasi, dan memperlihatkan bahwa semakin banyak unit yang tidak dievaluasi, semakin besar proporsi mahasiswa yang berstatus dropout. Pada kategori 0 unit tanpa evaluasi, mahasiswa graduate mendominasi dengan jumlah 2.170, sementara dropout berjumlah 1.345 dan enrolled 757. Namun, ketika jumlah unit tanpa evaluasi meningkat, proporsi mahasiswa dropout meningkat tajam, bahkan menjadi satu-satunya status yang muncul pada beberapa kategori tengah seperti 9 dan 11 unit. Sebaliknya, mahasiswa graduate nyaris tidak muncul pada kategori unit tanpa evaluasi di rentang menengah, dan hanya muncul kembali di kategori 25 unit. Hal ini menunjukkan adanya kecenderungan bahwa mahasiswa dengan lebih banyak unit tanpa evaluasi memiliki kemungkinan lebih besar untuk dropout, sementara mereka yang lulus umumnya memiliki lebih sedikit atau tidak ada unit tanpa evaluasi sama sekali. Pernyataan ini menjawab pertanyaan "Berapa banyak setiap status siswa terhadap nilai *total units* tidak dievaluasi?".

**6. Percentage Count of Student Status by Their Time Attendance Choice**

Grafik ini menggambarkan persentase status mahasiswa berdasarkan waktu kehadiran mereka (Attendance Time), dengan total 4.424 mahasiswa yang terbagi menjadi tiga kategori: Graduate (49,9%), Dropout (32,1%), dan Enrolled (17,9%). Lingkaran dalam menunjukkan status mahasiswa, sementara lingkaran luar menggambarkan distribusi waktu kehadiran, yakni daytime (kelas siang) dan evening (kelas malam). Mahasiswa lulusan (Graduate) mayoritas berasal dari kelas siang, yang juga berlaku untuk mahasiswa aktif (Enrolled), sedangkan mahasiswa yang dropout memiliki sebaran yang lebih merata antara kelas siang dan malam. Temuan ini mengindikasikan bahwa mahasiswa kelas siang cenderung memiliki peluang kelulusan lebih tinggi dibandingkan dengan mahasiswa kelas malam, yang tampaknya memiliki risiko dropout lebih besar. Pernyataan ini menjawab pertanyaan "Berapa banyak siswa yang melakukan *drop out* berdasarkan waktu pengambilan kelas?".

**7. Min, Avg, and Max of Admission Grade by Student Status**

Grafik ini menggambarkan nilai-nilai statistik yaitu *Minimal*, *Average*, dan *Maximal* pada data nilai masuk ke institut di setiap siswa. Grafik menunjukkan bahwa tidak ada perbedaan signifikan di antara status siswa baik **dropout**, **enrolled** maupun **graduate** pada sisi minimal dan maksimalnya. Namun, ada perbedaan sedikit pada bagian rata-rata. Nilai tertinggi diperoleh siswa dengan status **graduate** dan yang terendah diperoleh siswa dengan status **dropout**. Hal ini memvalidasi bahwa siswa dengan keambisan bawaan sebelum masuk ke ranah pembelajaran menjadi bekal penting dalam menjalani proses pengajaran, dan mendukung untuk mengantar siswa hingga lulus. Pernyataan ini menjawab pertanyaan "Berapa nilai minimum, rata-rata, dan maksimum nilai masuk ke kelas yang dipilih terhadap status kelulusan siswa?".

**8. Count of Student By Status at Course Category**

Grafik ini menunjukkan banyaknya siswa yang mendaftar pada setiap jenis jurusan atau *course* siswa yang terkategorikan berdasarkan statusnya. Hasil grafik menunjukkan siswa dengan ketiga status (**dropout**, **enrolled**, dan **graduate**) tertinggi diperoleh jurusan perawatan atau *Nursing* dengan total *dropout* **118**, *enrolled* **100**, dan *graduate* **548** siswa. Lalu, untuk yang terendah diperoleh jurusan *Biofuel Production Technologies* dengan total *dropout* **8**, *enrolled* **3**, dan *graduate* **1** siswa. Hal ini menunjukkan bahwa pemerataan kualitas kurikulum di Jaya Jaya Institut masih belum semua tertata, baik dari segi materi maupun prospek kerja yang dapat dijanjikan. Sehingga peminat disetiap jurusan masih belum di angka yang rata. Pernyataan ini menjawab pertanyaan "Seberapa banyak siswa yang melakukan *drop out* berdasarkan kelas yang dipilih?".

**9. Average of Unemployed Rate by Course**

Grafik ini memaparkan informasi tingkat kelemahan lapangan kerja berdasarkan jurusan atau *course*-nya. Dari hasil grafik, menunjukkan bahwa tingkat kelemahan paling rendah ada pada *course* *Informatics Engineering* yang hanya memiliki *rating* **10.72%**. Dengan tingkat kelemahan tertinggi dipegang oleh *course* *Agronomy* yang memiliki *rating* **13.97%**. Meskipun *unemployed rating* pada *Informatics Engineering* masih terbilang lebih sedikit daripada *Agronomy*, namun hasilnya peminatnya masih sedikit lebih banyak *Agronomy* (Hasil pertanyaan ke-8). Hal ini mengindikasikan tingkat kesulitan pada *Informatics Engineering* dalam proses pembelajarannya masih terbilang sulit untuk siswa yang masuk. Pernyataan ini menjawab pertanyaan "Berapa tingkat *unemployment rate* pada setiap kategori kelas?".

## Menjalankan Sistem Machine Learning

Untuk menjalankan *prototype* sistem *Machine Learning* berbasis Streamlit, berikut adalah langkah-langkahnya:

- Buka terminal dari VSCode atau dengan terminal dari PC. Arahkan direktori menuju direktori dimana **app.py** berada.
- Lalu jalankan perintah pada terminal dengan perintah berikut:

```
streamlit run app.py
```
- Setelah itu klik Local URL atau akses di browser dengan url http://localhost:8501

- Atau, karena sudah dilakukan *deployment* pada prototype, anda dapat mengaksesnya melalui link berikut
## Conclusion

Berdasarkan hasil analisis visual dari Business Dashboard yang terbagi dalam dua bagian utama, yaitu **Student’s Background** dan **Student’s Curricular Things**, dapat disimpulkan beberapa poin penting terkait performa mahasiswa dan faktor-faktor yang memengaruhi status mereka, khususnya terhadap kemungkinan dropout atau kelulusan:

1. Faktor Demografis dan Ekonomi:

Sebagian besar siswa masih berstatus lajang (88,6%) dan berusia muda ketika mendaftar, khususnya bagi yang graduate dan enrolled. Namun, siswa dengan usia lebih tua saat mendaftar cenderung memiliki risiko dropout lebih tinggi. Selain itu, tekanan ekonomi seperti status sebagai debtor dan tingginya economic pressure secara signifikan berhubungan dengan status dropout, menandakan bahwa masalah finansial merupakan faktor utama yang perlu diintervensi sejak awal.

2. Kehadiran dan Waktu Pengambilan Kelas:

Mahasiswa yang mengambil kelas siang (daytime) memiliki kemungkinan lebih besar untuk lulus dibandingkan dengan mahasiswa malam (evening), yang tampaknya lebih rentan terhadap dropout. Hal ini dapat berkaitan dengan kondisi kerja atau komitmen waktu mahasiswa malam yang lebih berat.

3. Performa Akademik sebagai Faktor Kunci Kelulusan:

Tingginya approval rate, weighted average grade, serta jumlah units approved dan units enrolled sangat berkorelasi dengan keberhasilan mahasiswa. Mahasiswa lulusan secara konsisten menunjukkan performa akademik yang lebih baik dan lebih konsisten dalam menyelesaikan unit dibanding kelompok lainnya. Sebaliknya, mahasiswa dropout cenderung gagal dalam mempertahankan nilai dan jumlah unit yang disetujui.

4. Tingkat Evaluasi dan Komitmen Mahasiswa:

Mahasiswa dengan banyak unit yang tidak dievaluasi (tidak mendapat nilai akhir) memiliki risiko tinggi menjadi dropout. Fakta bahwa hampir seluruh kategori unit tanpa evaluasi didominasi oleh mahasiswa dropout menunjukkan adanya kurangnya keterlibatan atau hambatan serius dalam menyelesaikan kewajiban akademik.

5. Kualitas Input dan Relevansi Jurusan:

Meski nilai masuk (admission grade) tidak menunjukkan perbedaan ekstrem antar status, rata-rata nilai masuk mahasiswa lulusan tetap lebih tinggi, memperkuat pentingnya kesiapan awal akademik. Selain itu, distribusi mahasiswa per jurusan masih belum merata. Beberapa jurusan populer seperti Nursing mencatat jumlah mahasiswa yang sangat tinggi, sementara jurusan seperti Biofuel Production Technologies nyaris tidak diminati. Relevansi dengan prospek kerja juga menjadi faktor, sebagaimana ditunjukkan oleh perbedaan unemployment rate per jurusan.

### Rekomendasi Action Items

Dari pernyataan dan kesimpulan yang sudah dituliskan, berikut adalah hal-hal yang dapat dilakukan Jaya Jaya Institusi untuk mendukung dan mengoptimalkan hasil dari temuan:

**Student's Background**

- Buat program orientasi khusus untuk siswa muda/lajang.
- Tawarkan mentoring bagi siswa yang kembali belajar.
- Berikan edukasi finansial & konsultasi pinjaman.
- Sediakan subsidi/bantuan keringanan biaya bagi siswa rentan.

**Student's Curricular Things**

- Terapkan sistem peringatan dini & kelas remedial.
- Tawarkan program tutoring dan dukungan akademik.
- Lakukan monitoring dan pastikan evaluasi berjalan baik.
- Berikan opsi jadwal fleksibel atau hybrid.
- Lakukan placement test & penyesuaian kurikulum.
- Promosikan jurusan minim peminat berbasis prospek kerja.
- Revisi kurikulum & perkuat koneksi industri.