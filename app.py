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

# Mapping nama variabel ke label
label_variabel = {
    "Penguasaan_Bola_Percent": "Penguasaan Bola (%)",
    "Passes_Per_90": "Jumlah Operan / 90 Menit",
    "LongBalls_Per_90": "Umpan Panjang / 90 Menit",
    "Tackles_Per_90": "Tackle / 90 Menit",
    "Shots_Per_90": "Tembakan / 90 Menit",
    "Carries_Per_90": "Progressive Carries / 90 Menit",
    "xG_Per_90": "Expected Goals (xG) / 90 Menit"
}

# Penjelasan singkat tiap cluster
penjelasan_cluster = {
    0: (
        "Tim dalam cluster ini cenderung tidak mendominasi penguasaan bola dan memiliki "
        "aktivitas serangan yang terbatas. Hal tersebut menunjukkan pendekatan permainan "
        "yang lebih pasif dan berorientasi pada pertahanan."
        "\n\n"
        "Jumlah tekel yang relatif tinggi mengindikasikan fokus utama tim adalah membatasi "
        "serangan lawan, sementara peluang ofensif diciptakan secara terbatas."
    ),

    1: (
        "Cluster ini merepresentasikan tim dengan dominasi permainan yang kuat melalui "
        "penguasaan bola dan jumlah operan yang tinggi. Pola ini menunjukkan kontrol tempo "
        "dan alur permainan yang konsisten."
        "\n\n"
        "Tingginya nilai tembakan dan expected goals (xG) mencerminkan efektivitas serangan "
        "yang baik, dengan pendekatan bertahan yang tidak terlalu intensif."
    ),

    2: (
        "Tim pada cluster ini menunjukkan keseimbangan antara penguasaan bola, serangan, "
        "dan pertahanan. Tidak terdapat kecenderungan dominasi maupun bertahan ekstrem."
        "\n\n"
        "Karakteristik tersebut menggambarkan pendekatan permainan yang stabil dan fleksibel "
        "dalam menyesuaikan strategi pertandingan."
    ),

    3: (
        "Cluster ini ditandai oleh intensitas bertahan yang tinggi dengan kecenderungan "
        "memanfaatkan transisi cepat dan serangan balik."
        "\n\n"
        "Meskipun tidak mendominasi penguasaan bola, tim dalam cluster ini tetap mampu "
        "menciptakan peluang serangan secara efektif melalui statistik umpan panjang yang sangat tinggi."
    )
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
    st.markdown("### Penjelasan Karakteristik Taktik")
    st.write(penjelasan_cluster[cluster])



    # Statistik
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

    statistik_tim.index = statistik_tim.index.map(
        lambda x: label_variabel.get(x, x)
    )

    st.table(statistik_tim.round(2))

else:
    st.error("Tim tidak ditemukan.")
