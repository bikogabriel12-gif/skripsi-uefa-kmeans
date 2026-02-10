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

st.set_page_config(page_title="Klasifikasi Taktik Tim UEFA", layout="centered")

st.title("Sistem Klasifikasi Taktik Tim UEFA")
st.write("Pilih nama tim untuk mengetahui cluster dan karakteristik taktiknya.")

nama_tim = st.selectbox(
    "Nama Tim",
    sorted(df["Nama_Tim"].unique())
)

hasil = df[df["Nama_Tim"] == nama_tim]

if not hasil.empty:
    cluster = int(hasil["Cluster"].values[0])
    st.success("Hasil Klasifikasi")
    st.write(f"**Cluster** : {cluster}")
    st.write(f"**Karakteristik Taktik** : {label_cluster[cluster]}")
else:
    st.error("Tim tidak ditemukan.")

 
