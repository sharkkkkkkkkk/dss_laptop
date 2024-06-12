import streamlit as st
import pandas as pd

# Memuat data dari file CSV
@st.cache_data
def load_data():
    data = pd.read_csv('data_laptop.csv')
    return data

data = load_data()

# Set up halaman
st.set_page_config(page_title="Sistem Pendukung Keputusan Pemilihan Laptop", page_icon=":computer:", layout="wide")

# Header
st.image("https://images.app.goo.gl/dEKRW8VtDUWDSJM97", width=100)  # Ganti dengan URL gambar logo Anda
st.title('Sistem Pendukung Keputusan Pemilihan Laptop')
st.markdown("Selamat datang di Sistem Pendukung Keputusan untuk pemilihan laptop yang sesuai dengan kebutuhan Anda. "
            "Silakan sesuaikan kriteria di bawah ini untuk mendapatkan rekomendasi terbaik.")

# Layout dengan dua kolom
col1, col2, col3 = st.columns(3)

with col1:
    max_price = st.slider('Batas Maksimal Harga (IDR)', 0, 30000000, 15000000, step=1000000)

with col2:
    min_ram = st.slider('Minimal RAM (GB)', 4, 64, 8, step=4)

with col3:
    min_storage = st.slider('Minimal Penyimpanan (GB)', 128, 2048, 256, step=128)

# Filter data berdasarkan input pengguna
filtered_data = data[(data['Harga (IDR)'] <= max_price) &
                     (data['RAM (GB)'] >= min_ram) &
                     (data['Penyimpanan (GB)'] >= min_storage)]

# Menampilkan hasil dengan style
st.subheader('Laptop yang Direkomendasikan')
st.write(f"Menampilkan {len(filtered_data)} dari {len(data)} laptop yang memenuhi kriteria Anda:")
st.dataframe(filtered_data.style.format({"Harga (IDR)": "Rp{:,.0f}", "RAM (GB)": "{:,.0f} GB", "Penyimpanan (GB)": "{:,.0f} GB"}))

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
        © 2024 Sistem Pendukung Keputusan Pemilihan Laptop. Dikembangkan oleh hitler.
    </div>
""", unsafe_allow_html=True)
