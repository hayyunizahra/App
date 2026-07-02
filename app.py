import streamlit as st
import pandas as pd

st.set_page_config(page_title="Kalkulator Aktuaria", page_icon="📊")

st.title("📊 Kalkulator Aktuaria")
st.write("Aplikasi perhitungan bunga, investasi, pinjaman, anuitas, dan premi sederhana")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Bunga Sederhana",
        "Bunga Majemuk",
        "Investasi",
        "Pinjaman Anuitas",
        "Tabel Angsuran",
        "Premi Sederhana"
    ]
)

if menu == "Bunga Sederhana":
    st.header("Bunga Sederhana")
    P = st.number_input("Modal awal")
    r = st.number_input("Bunga per tahun (%)")
    t = st.number_input("Waktu (tahun)")
    if st.button("Hitung"):
        bunga = P*r/100*t
        st.success(f"Bunga: Rp {bunga:,.0f}")
        st.success(f"Nilai akhir: Rp {P+bunga:,.0f}")

elif menu == "Bunga Majemuk":
    st.header("Bunga Majemuk")
    P = st.number_input("Modal awal")
    r = st.number_input("Bunga (%)")
    n = st.number_input("Periode")
    if st.button("Hitung"):
        A = P*(1+r/100)**n
        st.success(f"Nilai akhir: Rp {A:,.0f}")

elif menu == "Investasi":
    st.header("Investasi Berkala")
    setoran = st.number_input("Setoran tiap periode")
    i = st.number_input("Bunga periode (%)")
    n = st.number_input("Jumlah periode")
    if st.button("Hitung"):
        hasil = setoran*((1+i/100)**n-1)/(i/100)
        st.success(f"Nilai investasi: Rp {hasil:,.0f}")

elif menu == "Pinjaman Anuitas":
    st.header("Pinjaman dengan Anuitas")
    P = st.number_input("Jumlah pinjaman")
    r = st.number_input("Bunga tahunan (%)")
    tahun = st.number_input("Tenor (tahun)")
    if st.button("Hitung"):
        i = r/100/12
        n = tahun*12
        cicilan = P*i/(1-(1+i)**(-n))
        st.success(f"Cicilan per bulan: Rp {cicilan:,.0f}")

elif menu == "Tabel Angsuran":
    st.header("Tabel Amortisasi")
    P = st.number_input("Pinjaman")
    r = st.number_input("Bunga tahunan (%)")
    n = st.number_input("Jumlah bulan")
    if st.button("Buat tabel"):
        i = r/100/12
        cicilan = P*i/(1-(1+i)**(-n))
        saldo = P
        data=[]
        for bulan in range(1, int(n)+1):
            bunga = saldo*i
            pokok = cicilan-bunga
            saldo -= pokok
            data.append([bulan, cicilan, bunga, pokok, max(saldo,0)])
        df = pd.DataFrame(data, columns=["Bulan","Angsuran","Bunga","Pokok","Sisa"])
        st.dataframe(df)

elif menu == "Premi Sederhana":
    st.header("Premi Sederhana")
    manfaat = st.number_input("Nilai manfaat")
    peluang = st.number_input("Peluang (%)")
    biaya = st.number_input("Biaya (%)")
    if st.button("Hitung"):
        premi = manfaat*(peluang/100)*(1+biaya/100)
        st.success(f"Premi: Rp {premi:,.0f}")
