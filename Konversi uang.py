def konversi_usd_ke_idr(jumlah_usd, kurs_usd_idr):
    jumlah_idr = jumlah_usd * kurs_usd_idr
    return jumlah_idr

# Kurs USD ke IDR
kurs_usd_idr = 14000

# Jumlah USD yang ingin dikonversi
jumlah_usd = float(input("Masukkan jumlah USD: "))

# Konversi USD ke IDR
jumlah_idr = konversi_usd_ke_idr(jumlah_usd, kurs_usd_idr)

print("Jumlah dalam IDR:", jumlah_idr)
