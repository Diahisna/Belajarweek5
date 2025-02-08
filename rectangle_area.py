def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

# Input dari pengguna
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

# Menghitung luas
hasil = hitung_luas_persegi_panjang(panjang, lebar)

# Menampilkan hasil
print(f"Luas persegi panjang dengan:")
print(f"Panjang = {panjang}")
print(f"Lebar = {lebar}")
print(f"Adalah = {hasil}")