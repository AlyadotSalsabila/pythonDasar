angka_int = 5
angka_float = 3.14
teks = "Hai"
daftar = [1, 2, 3, 4, 5]

print ("int: ", type (angka_int))
print ("float: ", type (angka_float))
print ("Teks: ", type (teks))
print ("List: ", type (daftar))

belanja = ["beras", "minyak", "telur", "gula", "kopi"]

for u in range (5):
    print (belanja)

harga_belanja = {
    "beras" : 12000,
    "minyak" : 17000,
    "telur" : 24000,
    "gula" : 15000,
    "kopi" : 20000
}

total = sum (harga_belanja.values())
print ("\nTotal harga belanjaan: ", total)

def persegi_panjang (panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

luas, keliling = persegi_panjang (5, 3)
print ("\nLuas persegi panjang: ", luas)
print ("Keliling persegi panjnag: ", keliling)

usia = int (input ("\nMasukkan usia anda: "))
if 0 <= usia <= 13:
    print ("Anak")
elif 14 <= usia <= 24:
    print ("Remaja")
elif 25 <= usia <= 49:
    print ("Dewasa")
elif usia >= 50:
    print ("Lansia")
else:
    print ("Usia tidak valid")
