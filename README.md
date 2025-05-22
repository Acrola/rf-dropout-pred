# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

Jaya Jaya Institut telah meminta bantuan kita sebagai data scientist dalam menyelesaikan permasalahannya, menyediakan dataset mengenai performa siswa yang belajar di institut mereka untuk membuat sistem prediksi dropout. Selain itu, mereka juga meminta sebuah dashboard agar mereka mudah dalam memahami data dan memonitor performa siswa. Dataset tersebut dapat diakses pada link berikut: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

### Permasalahan Bisnis
Permasalahan bisnis utama yang dihadapi Jaya Jaya Institut adalah **tingginya dropout**. Angka dropout yang tinggi ini mencerminkan tantangan operasional, finansial, dan reputasi yang signifikan bagi institusi.

Tingginya angka dropout secara langsung menimbulkan beberapa kerugian dan risiko bisnis bagi Jaya Jaya Institut, antara lain:

1.  **Penurunan Pendapatan:** Mahasiswa yang dropout berhenti membayar biaya kuliah, yang berdampak langsung pada penurunan pendapatan institusi.
2.  **Peningkatan Biaya Operasional:** Mengganti mahasiswa yang dropout memerlukan biaya untuk proses menarik dan menerima mahasiswa baru. Selain itu, ada potensi biaya yang dikeluarkan untuk sumber daya (fasilitas, dosen, dll.) yang tidak dimanfaatkan secara optimal karena mahasiswa tidak menyelesaikan studinya.
3.  **Penurunan Reputasi Institusi:** Angka dropout yang tinggi dapat merusak reputasi Jaya Jaya Institut di mata calon mahasiswa, orang tua, dan lembaga akreditasi, yang pada akhirnya dapat mempengaruhi jumlah pendaftar di masa mendatang.
4.  **Hilangnya Potensi Alumni:** Setiap mahasiswa yang dropout berarti hilangnya potensi alumni yang sukses yang dapat berkontribusi pada jaringan dan dukungan institusi di masa depan.
5.  **Ketidaksesuaian Alokasi Sumber Daya:** Sulit untuk mengalokasikan sumber daya seperti kelas, staf pengajar, dan fasilitas secara efektif jika angka dropout tidak dapat diprediksi.

**Urgensi** untuk mengatasi masalah tingginya angka dropout mahasiswa ini sangat tinggi. Jika dibiarkan, tren ini akan terus meningkatkan kerugian finansial, merusak reputasi Jaya Jaya Institut sebagai lembaga pendidikan yang berhasil mencetak lulusan, dan pada akhirnya dapat membahayakan keberlanjutan operasional serta posisi kompetitif institusi dalam jangka panjang.

Oleh karena itu, proyek ini bertujuan untuk mengidentifikasi mahasiswa yang berisiko tinggi mengalami dropout melalui model machine learning, menyediakan informasi yang memungkinkan manajemen Jaya Jaya Institut untuk mengambil tindakan proaktif untuk memberikan dukungan yang diperlukan dan mengurangi jumlah dropout. Hal ini penting untuk mengurangi **dampak negatif dan risiko bisnis** yang disebabkan oleh tingginya dropout.

### Cakupan Proyek
Tujuan-tujuan proyek ini berupa:
1. Melatih model prediktif untuk mengidentifikasi siswa yang berisiko dropout pada Jaya Jaya Institut.
2. Menyediakan dashboard dan solusi machine learning agar manajemen dapat dengan mudah memonitori siswa yang berisiko dropout.

Proyek ini meliputi tahap-tahap berikut:
1. **Persiapan**
- Impor Library: Mengimpor library yang diperlukan seperti Pandas, NumPy, Matplotlib, Seaborn, Joblib, dan modul dari scikit-learn dan imblearn untuk manipulasi data, visualisasi, modeling, dan evaluasi.
- Data: Memuat dataset (data.csv) ke dalam Pandas DataFrame, dengan menentukan pemisah titik koma (delimiter).
2. **Data Understanding**
- Eksplorasi: Melihat dataset menggunakan df.info(), df.describe(), dan memeriksa nilai yang hilang dan duplikat.
- Analisis Target: Menganalisis variabel target 'Status' dengan mendapatkan jumlah nilai (value counts), proporsi, dan memvisualisasikan distribusinya menggunakan countplot dan pie chart.
3.  **Data Preparation / Preprocessing**
- Pemilihan Data: Memisahkan data siswa 'Enrolled' untuk inferensi dan membuat DataFrame terpisah untuk siswa 'Dropout' dan 'Graduate' untuk pelatihan model.
- Encoding: Mengodekan label 'Status' ('Dropout' dan 'Graduate') menggunakan LabelEncoder.
- SMOTE: Menggunakan SMOTE untuk mengatasi ketidakseimbangan kelas antara 'Dropout' dan 'Graduate'.
- Data Splitting: Membagi data yang sudah di-resample menjadi set pelatihan dan pengujian dengan rasio 80/20.
4. **Modeling**
- Pelatihan: Melatih model Random Forest pada data pelatihan.
- Prediksi: Membuat prediksi pada data pengujian menggunakan model yang telah dilatih.
5. **Evaluation**
- Evaluasi: Mengevaluasi model menggunakan laporan klasifikasi (classification report) untuk melihat presisi, recall, dan F1-score, serta menghitung akurasi.
- Visualisasi: Membuat dan memvisualisasikan confusion matrix untuk menunjukkan True Positive, True Negative, False Positive, dan False Negative.
- Kesimpulan: Mengambil kesimpulan dari hasil analisis data dan kinerja model dalam memprediksi siswa dropout dan graduate berdasarkan metrik evaluasi dan confusion matrix.
6. **Inference Test**
- Prediksi: Menggunakan model yang telah dilatih untuk memprediksi probabilitas dropout untuk siswa 'Enrolled'.
- Identifikasi: Mengidentifikasi siswa dengan risiko dropout tinggi (probabilitas > 0.5).
- Pelaporan: Mencetak jumlah siswa berisiko tinggi dan proporsinya dari total siswa enrolled.
- Penyimpanan Hasil: Menambahkan hasil prediksi dan probabilitas ke DataFrame siswa enrolled.
- Konversi: Mendefinisikan dan menerapkan fungsi untuk mengembalikan nilai kategorikal numerik ke deskripsi teks aslinya.
- Penyimpanan Model: Menyimpan model yang telah dilatih dan dataset siswa enrolled dengan prediksi dari model menggunakan joblib.
7. **Dashboard dan Solusi Machine Learning**
- Membuat dashboard dan solusi machine learning agar manajemen Jaya Jaya Institut dapat dengan mudah memantau siswa enrolled yang teridentifikasi berisiko dropout.

### Persiapan

Sumber data: Dataset untuk analisis faktor-faktor attrition yang digunakan pada proyek didapatkan dari https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance, seperti instruksi submission.

**Setup environment**:
> Opsi 1: Menjalankan Notebook pada Colab
1. Buka link https://colab.research.google.com/ dan klik "Upload" untuk mengupload file notebook.
2. Connect pada runtime dengan menggunakan "Connect" > "Connect to a hosted runtime"
3. Upload file dataset yang digunakan ke dalam Colab.
4. Jalankan semua sel dengan "Runtime" > "Run all." untuk melihat semua hasil output dari model.

> Opsi 2: Menjalankan Notebook pada Environment Lokal
1. Pastikan telah menginstall Python, pip, dan Jupyter Notebook pada komputer.
2. Letakkan file notebook, dataset, dan requirements.txt pada directory yang sama.
3. Buka Terminal atau Command Prompt dan buka directory dimana file-file tersebut terletak menggunakan perintah cd, contohnya berikut:
```
cd C:\Example\Files_Directory
```
4. Buat virtual environment dengan perintah berikut:
```
python3 -m venv venv
```
5. Aktivasi virtual environment menggunakan perintah berikut:
```
.\venv\Scripts\activate
```
6. Setelah virtual environment sudah aktif, install semua dependensi dari file requirements.txt dengan perintah berikut:
```
pip install -r requirements.txt
```
7. Jika Jupyter Notebook belum diinstall, pastikan install pada environment dengan:
```
pip install jupyter
```
8. Jalankan Jupyter Notebook dengan:
```
jupyter notebook
```
9. Pada file browser Jupyter, klik file notebook yang ingin dijalankan.
10. Gunakan "Cell" > "Run All" untuk menjalankan semua sel dan melihat semua hasil output dari model.

## Business Dashboard
Dashboard dibuat agar tim manajemen Jaya Jaya Institut mudah memahami data dan memonitor performa siswa yang dinilai berisiko dropout tinggi. Pada proyek ini, hal tersebut didefinisikan sebagai siswa yang dinilai oleh model memiliki probabilitas dropout lebih dari 50 persen. Dashboard ini dibuat menggunakan data siswa enrolled, yaitu siswa yang masih menjalani proses pembelajaran pada Jaya Jaya Institut, dengan prediksi kelas (Likely Dropout atau Unlikely Dropout) dari model yang telah dilatih pada data siswa dropout dan graduate serta probabilitas dropout dan graduate mereka.

Hal ini dilakukan agar dashboard dapat digunakan oleh tim manajemen untuk melihat pola-pola pada data siswa yang diprediksi berisiko tinggi dropout dan yang tidak berisiko dropout, memungkinkan mereka menyusun strategi untuk mengurangi siswa dropout dan melakukan usaha proaktif dalam membimbing siswa berisiko. Berikut adalah tampilan dari dashboard:

![img](https://i.imgur.com/3zWHTEi.png)

**Cara menggunakan Dashboard**
 1. Gunakan Docker dan file Metabase yang disediakan untuk mempersiapkan dashboard.
 2. Buka link Metabase dari Docker pada browser, yaitu http://localhost:3000/.
 3. Gunakan username **root@mail.com** dan password **root123** untuk masuk ke Metabase.
 4. Buka collection "Dashboards" dan klik "Enrolled Students Monitoring" untuk menggunakan dashboard.

## Menjalankan Sistem Machine Learning

**Cara menggunakan Sistem Machine Learning Streamlit**
> Opsi 1: Menjalankan Aplikasi Secara Lokal
1. Pastikan Python sudah terinstal di komputer anda.
2. Download file dropout_prediction.py, requirements.txt, dan rf_dropout_prediction.pkl.
3. Buka Terminal atau Command Prompt.
4. Navigasikan ke direktori tempat anda menyimpan file-file tersebut.
5. Install library yang diperlukan dengan menjalankan perintah berikut:
```
pip install -r requirements.txt
```
6. Jalankan aplikasi Streamlit dengan perintah berikut:
```
streamlit run dropout_prediction.py
```
7. Buka http://localhost:8501 pada browser anda untuk mengakses aplikasi Streamlit yang telah dijalankan.
8. Isi semua informasi siswa yang ingin diprediksi dropout atau tidaknya pada form-form yang tersedia.
9. Klik tombol "Predict Dropout Probability" untuk mendapatkan prediksi model mengenai apakah siswa yang belajar pada institut kemungkinan dropout atau tidak, dan probabilitas dropout siswa tersebut yang dihitung oleh model.

> Opsi 2: Menggunakan Aplikasi Online
1. Buka https://rf-dropout-pred-bcadrrghuqck342mm9jsge.streamlit.app/ pada browser anda untuk mengakses aplikasi Streamlit.
2. Isi semua informasi siswa yang ingin diprediksi dropout atau tidaknya pada form-form yang tersedia.
3. Klik tombol "Predict Dropout Probability" untuk mendapatkan prediksi model mengenai apakah siswa yang belajar pada institut kemungkinan dropout atau tidak, dan probabilitas dropout siswa tersebut yang dihitung oleh model.

## Conclusion
Untuk menyimpulkan apakah proyek telah terpenuhi dengan baik, mari melihat kembali tujuan-tujuan utama proyek:
1. Melatih model prediktif untuk mengidentifikasi siswa yang berisiko dropout pada Jaya Jaya Institut.
2. Menyediakan dashboard dan solusi machine learning agar manajemen dapat dengan mudah memonitori siswa yang berisiko dropout.

Maka dapat disimpulkan bahwa proyek analisis data ini berhasil mencapai semua tujuannya dalam membantu mengatasi permasalahan jumlah siswa dropout yang tinggi di Jaya Jaya Institute. Tujuan utama proyek ini, yaitu melatih model prediktif untuk mengidentifikasi siswa yang berisiko dropout pada Jaya Jaya Institut dan menyediakan alat monitoring dalam bentuk dashboard dan aplikasi streamlit, telah terpenuhi dengan baik.

Kita telah menemukan dari hasil analisis fitur oleh model Random Forest bahwa dropout secara umum:
- Memiliki jumlah unit disetujui lebih rendah pada semester 1 dan 2.
- Memiliki nilai lebih rendah pada semester 1 dan 2.
- Memiliki evaluasi lebih rendah pada semester 2.
- Kemungkinan tidak tepat waktu dalam membayar tuition.
- Kemungkinan tidak mendapat scholarship.
- Kemungkinan lebih tua.
- Memiliki nilai lebih rendah pada kualifikasi sebelumnya dan pada admisi.

Data ini dapat digunakan oleh Jaya Jaya Institut untuk menyusun strategi mengatasi jumlah dropout nantinya, digabungkan dengan model yang telah dilatih dan alat monitoring yang telah dibuat, sebagai solusi komprehensif mengidentifikasi dan memantau siswa yang berpotensi dropout.

### Rekomendasi Action Items
Berikut rekomendasi action items untuk dilakukan Jaya Jaya Institut:
1. **Identifikasi mahasiswa berisiko tinggi secepat mungkin:** 

Gunakan dashboard dan aplikasi yang telah disediakan untuk secara proaktif mengidentifikasi mahasiswa yang terdaftar yang diklasifikasikan sebagai 'Likely Dropout'. Deteksi dini memungkinkan bantuan/bimbingan lebih awal pada siswa yang berisiko.

2. **Membuat program bantuan siswa:** 

Membuat program bantuan untuk mahasiswa yang diidentifikasi berisiko tinggi. Ini dapat meliputi:
- Konseling akademik.
- Program bimbingan belajar.
- Program mentoring.
- Menghubungkan mahasiswa dengan sumber daya yang relevan seperti penasihat bantuan keuangan, layanan kesehatan mental, atau konselor karier.

3. **Analisis lanjut faktor-faktor penyebab:** 

Dashboard yang dibuat telah menyediakan data siswa enrolled yang dapat dieksplorasi oleh Jaya Jaya Institut lebih lanjut untuk menyusun strategi untuk mengurangi jumlah siswa dropout. Sebagai contoh, beberapa observasi menarik dari dashboard adalah:

- Pada grafik "Average Dropout Probability by Course" terlihat bahwa Informatics Engineering menempati posisi teratas, dengan rata-rata probabilitas dropout 73%. 
- Siswa berusia 30-35 tahun pada saat pendaftaran memiliki proporsi paling besar siswa yang kemungkinan dropout.
- Jauh lebih sedikit siswa penerima beasiswa yang kemungkinan dropout daripada yang tidak mendapatkan beasiswa.
- Siswa yang kemungkinan dropout dan yang tidak kemungkinan dropout memiliki nilai rata-rata yang hampir sama pada kualifikasi sebelumnya dan pada admission, namun siswa yang kemungkinan dropout memiliki nilai rata-rata lebih buruk pada semester 1 dan 2 dibandingkan yang tidak kemungkinan dropout.
- Jauh lebih banyak siswa yang memiliki hutang diprediksi sebagai siswa yang kemungkinan dropout.
- Jauh lebih banyak siswa yang tidak membayar semua biaya pembelajarannya diprediksi sebagai siswa yang kemungkinan dropout.

Observasi-observasi ini dapat menuju ke investigasi lebih lanjut oleh Jaya Jaya Institut untuk mengatasi masalah tersebut, untuk memastikan apakah korelasi tersebut memang berarti bahwa faktor-faktor itu adalah faktor penyebab siswa melakukan dropout. Pemahaman yang didapatkan dari investigasi dapat digabungkan dengan pemantauan performa siswa melalui sistem dashboard dan aplikasi Streamlit untuk meminimalisir siswa yang dropout.

4. **Kembangkan intervensi yang ditargetkan:**

Berdasarkan analisis faktor-faktor penyebab, rancang bantuan khusus untuk mengatasi masalah tersebut. Misalnya:

- Jika masalah keuangan adalah faktor signifikan, promosikan kesadaran dan aksesibilitas opsi beasiswa dan bantuan keuangan.
- Jika kinerja akademik di semester pertama adalah indikator kuat, tawarkan dukungan akademik tambahan atau mata kuliah remedial.

5. **Pantau dan lacak perkembangan siswa:**

Terus memantau perkembangan akademik dan keterlibatan siswa berisiko tinggi yang menerima dukungan. Lacak apakah bantuan efektif dalam meningkatkan kemungkinan mereka menghindari dropout, dan kumpulkan feedback dari siswa yang telah berpartisipasi dalam program untuk memahami apa yang berhasil dengan baik dan apa yang dapat diperbaiki.

6. **Kembangkan model lebih lanjut:**

Evaluasi dan latih kembali model prediksi dropout dengan data baru secara berkala untuk memastikan akurasi dan efektivitasnya tidak menurun seiring waktu. Ini dapat melibatkan penggabungan feedback dan wawasan yang diperoleh dari program bantuan.
