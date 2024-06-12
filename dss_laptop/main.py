import streamlit as st
import pandas as pd

# Memuat data dari file CSV
@st.cache
def load_data():
    data = pd.read_csv('data_laptop.csv')
    return data

data = load_data()

st.title('Sistem Pendukung Keputusan Pemilihan Laptop')

# Input dari pengguna
max_price = st.slider('Batas Maksimal Harga (IDR)', 0, 30000000, 15000000)
min_ram = st.slider('Minimal RAM (GB)', 4, 64, 8)
min_storage = st.slider('Minimal Penyimpanan (GB)', 128, 2048, 256)

# Filter data berdasarkan input pengguna
filtered_data = data[(data['Harga (IDR)'] <= max_price) &
                     (data['RAM (GB)'] >= min_ram) &
                     (data['Penyimpanan (GB)'] >= min_storage)]

# Menampilkan hasil
st.subheader('Laptop yang Direkomendasikan')
st.write(filtered_data)