"""
Menunjukkan semua sintaksis Python
"""
from geometry.segitiga import hitung_luas_segitiga
from geometry.persegi_panjang import hitung_luas_persegi_panjang
from geometry_class.segitiga import Segitiga

print('Hello World!')

# Menghitung luas segitiga

alas = 10
tinggi = 30
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

# Menggunakan logika percabangan
if luas_segitiga < 30:
    print('Kecil!')
elif luas_segitiga == 30:
    print('Cukupan')
else:
    print('Buesar bianget!')

# Perulangan mengatasi kode seperti ini...
print('1', luas_segitiga)
print('2', luas_segitiga)
print('3', luas_segitiga)
print('4', luas_segitiga)
print('5', luas_segitiga)
print('6', luas_segitiga)
print('7', luas_segitiga)
print('8', luas_segitiga)
print('9', luas_segitiga)
print('10', luas_segitiga)

# .. dengan cara seperti ini
print('Dengan for')
for i in range(0, 10):
    print(i+1, luas_segitiga)


# MODULARISASI TAHAP 1: PEMBUATAN FUNGSI
print('Segitiga 1')
alas = 5
tinggi = 15
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

print('Segitiga 2')
alas = 3
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

print(hitung_luas_segitiga('Segitiga 3', 5, 15))
print(hitung_luas_segitiga('Segitiga 4', 3, 6))

# MODULARISASI TAHAP 2: PEMBUATAN PACKAGE
print(hitung_luas_persegi_panjang('Persegi 1', 10, 2))
print(hitung_luas_persegi_panjang('Persegi 2', 5, 3))

# MODULARISAI TAHAP 3: PEMBUATAN CLASS
segitiga1 = Segitiga('Segitiga 1 as class', 50, 3)
print(segitiga1.title)
print(segitiga1.hitung_luas())
segitiga2 = Segitiga('Segitiga 2 as class', 7, 2)
print(segitiga2.title)
print(segitiga2.hitung_luas())
