<img width="500" height="375" alt="Laporan omset_produk" src="https://github.com/user-attachments/assets/6cbca74a-63a1-4434-8e90-e9d554176cfc" /># E-Commerce ETL Pipeline

Proyek ini adalah sistem otomatisasi data (*Data Pipeline*) skala menengah yang dirancang untuk mensimulasikan proses **ETL (Extract, Transform, Load)** pada data transaksi E-Commerce yang berantakan (*dirty data*). Pipeline ini telah diuji menggunakan **200 baris data simulasi ekstrem** yang penuh dengan duplikat, data bolong, dan anomali teks.

## Tech Stack yang Digunakan
* **Python 3**
* **Pandas** (Untuk manipulasi data, agregasi, dan *Data Cleaning*)
* **SQLite3** (Sebagai database operasional sumber dan target *Data Warehouse*)

## Alur Kerja Pipeline (ETL)
1. **Extract**: Robot mengambil data transaksi mentah bulanan dari database operasional toko (`ecommerce_operasional.db`).
2. **Transform (Pembersihan Tingkat Lanjut)**: 
   * **Deduplication**: Menghapus transaksi duplikat permanen secara aman menggunakan `.copy()`.
   * **Text Standardization**: Membersihkan spasi gaib (*whitespace*) dan memaksa semua format teks menjadi *Title Case*.
   * **Data Mapping**: Menyelaraskan data singkatan yang berantakan (mengubah `Mamin` otomatis menjadi `Makanan & Minuman`, dan `Oto` menjadi `Otomotif`) menggunakan kamus pemetaan Pandas.
   * **Handling Missing Values**: Mengamankan data bolong (*NaN*) dengan mengisi nilai default (Item diisi `1`, Harga diisi `0`).
   * **Anomaly Filtering**: Membuang data cacat sistem yang memiliki harga di bawah atau sama dengan 0.
   * **Feature Engineering**: Membuat kolom kalkulasi baru berupa `total_pendapatan` ($jumlah\_item \times harga\_satuan$).
3. **Load**: Melakukan agregasi (*Group By*) untuk merangkum total omset bersih per kategori, lalu menyimpannya ke tabel *Data Warehouse* (`omset_produk_bulanan`) di database `ecommerce_analytics.db`.

## Hasil Uji Coba (200 Data Pasca ETL)

Berhasil mereduksi 200 data mentah yang rusak menjadi laporan keuangan bersih yang dikelompokkan ke dalam 4 kategori utama:

| Kategori Produk | Total Pendapatan (Rp) |
| :--- | :--- |
| **Elektronik** | 66.060.000 |
| **Fashion** | 31.610.000 |
| **Makanan & Minuman** | 45.560.000 |
| **Otomotif** | 20.590.000 |

### 📉 Visualisasi Dashboard
![Dashboard Omset](<img width="500" height="375" alt="Laporan omset_produk" src="https://github.com/user-attachments/assets/470a4bfb-e570-45ad-ab92-1e7cbcd3b24e" />
)

## Cara Menjalankan
Pastikan database sumber sudah terisi, lalu cukup jalankan script utama via terminal laptop Anda:
```bash
python cron_job_omset.py
