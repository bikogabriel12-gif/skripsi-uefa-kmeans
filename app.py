import streamlit as st
import pandas as pd

# Load data hasil clustering
df = pd.read_csv("DATA_TAHAP_5_FINAL_RESULT_K4.csv")

# Mapping cluster ke label taktik
label_cluster = {
    0: "Fokus Bertahan dan Serangan Terbatas",
    1: "Dominasi Permainan dan Serangan Efektif",
    2: "Permainan Seimbang",
    3: "Intensitas Bertahan Tinggi dan Transisi Cepat"
}

# Konfigurasi halaman
st.set_page_config(
    page_title="Klasifikasi Taktik Tim UEFA Champions League 2024–2025",
    layout="centered"
)

# Judul & deskripsi
st.title("Sistem Klasifikasi Taktik Tim UEFA Champions League 2024–2025")
st.write(
    "Pilih nama tim untuk mengetahui cluster serta karakteristik taktik "
    "berdasarkan statistik permainan musim 2024–2025."
)

# Pilih tim
nama_tim = st.selectbox(
    "Nama Tim",
    sorted(df["Nama_Tim"].unique())
)

# Ambil data tim
hasil = df[df["Nama_Tim"] == nama_tim]

if not hasil.empty:
    cluster = int(hasil["Cluster"].values[0])

    # Hasil klasifikasi
    st.success("Hasil Klasifikasi")
    st.write(f"**Cluster** : {cluster}")
    st.write(f"**Karakteristik Taktik** : {label_cluster[cluster]}")

   
    # Tampilkan Statistik Asli
   
    st.subheader("Statistik Permainan Tim (Per 90 Menit)")

    kolom_statistik = [
        "Penguasaan_Bola_Percent",
        "Passes_Per_90",
        "LongBalls_Per_90",
        "Tackles_Per_90",
        "Shots_Per_90",
        "Carries_Per_90",
        "xG_Per_90"
    ]

    statistik_tim = hasil[kolom_statistik].T
    statistik_tim.columns = ["Nilai"]

    st.table(statistik_tim.round(2))

else:
    st.error("Tim tidak ditemukan.")
