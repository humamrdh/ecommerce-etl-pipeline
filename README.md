# E-Commerce ETL Pipeline

Proyek ini adalah sistem otomatisasi data (*Data Pipeline*) sederhana yang dirancang untuk mensimulasikan proses **ETL (Extract, Transform, Load)** pada data transaksi E-Commerce.

## Tech Stack yang Digunakan
* **Python 3**
* **Pandas** (Untuk proses *Transformation* dan *Data Cleaning*)
* **SQLite3** (Sebagai database operasional sumber dan target *Data Warehouse*)

## Alur Kerja Pipeline (ETL)
1. **Extract**: Robot menyedot data transaksi mentah harian dari database kasir toko (`ecommerce_operasional.db`).
2. **Transform**: 
   * Menghapus transaksi duplikat permanen.
   * Membersihkan spasi gaib dan merapikan teks kategori produk menjadi *Title Case*.
   * Mengamankan data dari sistem error (menyaring harga produk yang bernilai minus).
   * Mengisi data bolong (*missing values*) pada jumlah item secara otomatis.
   * Membuat kolom kalkulasi baru berupa `total_pendapatan`.
3. **Load**: Menyimpan hasil agregasi omset bersih ke dalam tabel warehouse (`omset_produk`) untuk siap dikonsumsi oleh tim bisnis.

## Contoh Data yang Diproses

**Data Mentah (Source):**
* TX-001 | Elektronik | 1 | 5000000 (Duplikat)
* TX-005 | Fashion | 1 | -50000 (Harga Minus/Error)
* TX-006 | elektronik | 1 | 1200000 (Typo Huruf Kecil)

**Hasil Akhir di Warehouse (Target):**
* Elektronik: 11.950.000
* Fashion: 650.000

## Cara Menjalankan
Cukup jalankan script utama via terminal laptop Anda:
```bash
python cron_job_omset_mingguan.py
