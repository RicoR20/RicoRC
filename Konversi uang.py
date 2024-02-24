import streamlit as st

def konversi_usd_ke_idr(jumlah_usd, kurs_usd_idr):
    jumlah_idr = jumlah_usd * kurs_usd_idr
    return jumlah_idr

def main():
    st.title("Konversi USD ke IDR")

    # Kurs USD ke IDR
    kurs_usd_idr = 14000

    # Input jumlah USD
    jumlah_usd = st.number_input("Masukkan jumlah USD", value=0.0)

    # Konversi USD ke IDR
    jumlah_idr = konversi_usd_ke_idr(jumlah_usd, kurs_usd_idr)

    # Menampilkan hasil konversi
    st.write(f"Jumlah dalam IDR: {jumlah_idr}")

if _name_ == "_main_":
    main()
