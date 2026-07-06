import pandas as pd
import sqlite3

def robot_pembersih(df):
    df = df.drop_duplicates().copy()
    df['kategori_produk'] = df['kategori_produk'].str.strip().str.title()
    kamus = {
        'Mamin': 'Makanan & Minuman',
        'Oto': 'Otomotif'
    }
    df['kategori_produk'] = df['kategori_produk'].replace(kamus)
    df['jumlah_item'] = df['jumlah_item'].fillna(1).astype(int)
    df['harga_satuan'] = df['harga_satuan'].fillna(0)
    df['harga_satuan'] = df['harga_satuan'].astype(int)
    df = df[df['harga_satuan'] >= 0]
    df['total_pendapatan'] = df['jumlah_item']*df['harga_satuan'].astype(int)
    df_akhir = df.groupby('kategori_produk')['total_pendapatan'].sum().reset_index()
    
    return df_akhir

sumber_data = sqlite3.connect(r"C:\GHOZI'S PROJECT\Data Engineer NEW\File .db\ecommerce_operasional.db")
df = pd.read_sql('SELECT * FROM penjualan_mentah', sumber_data)
sumber_data.close()

df_bersih = robot_pembersih(df)

data_warehouse = sqlite3.connect(r"C:\GHOZI'S PROJECT\Data Engineer NEW\File .db\Warehouse\ecommerce_analytics.db")
df_bersih.to_sql("omset_produk_bulanan", data_warehouse, if_exists='replace', index=False)
data_warehouse.close()

print("Pembersihan Sukses...")
