import streamlit as st
import pandas as pd

# Memuat data dari file CSV
@st.cache_data
def load_data():
    data = pd.read_csv('data_laptop.csv')
    return data

data = load_data()

# Header
st.title('Sistem Pendukung Keputusan Pemilihan Laptop')
st.markdown("Selamat datang di Sistem Pendukung Keputusan untuk pemilihan laptop yang sesuai dengan kebutuhan Anda. "
            "Silakan sesuaikan kriteria di bawah ini untuk mendapatkan rekomendasi terbaik.")

# Rentang harga yang tersedia
harga_values = sorted(data['Harga'].unique())
ram_values = sorted(data['RAM'].unique())
storage_values = sorted(data['Penyimpanan'].unique())

# Menampilkan rentang harga terendah dan tertinggi
st.markdown(f"**Harga Terendah:** IDR {harga_values[0]:,}")
st.markdown(f"**Harga Tertinggi:** IDR {harga_values[-1]:,}")

# Selectbox untuk memilih rentang harga
col1, col2 = st.columns(2)
with col1:
    min_price = st.selectbox('Batas Minimal Harga (IDR)', harga_values, index=0)
with col2:
    max_price = st.selectbox('Batas Maksimal Harga (IDR)', harga_values, index=len(harga_values)-1)

# Selectbox untuk memilih rentang RAM
col3, col4 = st.columns(2)
with col3:
    min_ram = st.selectbox('Minimal RAM (GB)', ram_values, index=0)
with col4:
    max_ram = st.selectbox('Maksimal RAM (GB)', ram_values, index=len(ram_values)-1)

# Selectbox untuk memilih rentang penyimpanan
col5, col6 = st.columns(2)
with col5:
    min_storage = st.selectbox('Minimal Penyimpanan (GB)', storage_values, index=0)
with col6:
    max_storage = st.selectbox('Maksimal Penyimpanan (GB)', storage_values, index=len(storage_values)-1)


# Filter data berdasarkan input pengguna
filtered_data = data[(data['Harga'] >= min_price) &
                     (data['Harga'] <= max_price) &
                     (data['RAM'] >= min_ram) &
                     (data['RAM'] <= max_ram) &
                     (data['Penyimpanan'] >= min_storage) &
                     (data['Penyimpanan'] <= max_storage)]

if selected_brand != 'Nama':
    filtered_data = filtered_data[filtered_data['Nama'] == selected_brand]

# Menampilkan hasil
st.subheader('Laptop yang Direkomendasikan')
st.write(f"Menampilkan {len(filtered_data)} dari {len(data)} laptop yang memenuhi kriteria Anda:")
st.dataframe(filtered_data)

# Footer
st.markdown("""
    <style>
        .footer {
            font-size: 12px;
            text-align: center;
            color: grey;
            padding: 10px;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
        }
    </style>
    <div class="footer">
        © 2024 Sistem Pendukung Keputusan Pemilihan Laptop.
    </div>
""", unsafe_allow_html=True)
