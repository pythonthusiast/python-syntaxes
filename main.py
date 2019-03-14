"""
Menunjukkan semua sintaksis Python
"""
print('Hello World!')

# Menghitung luas segitiga

alas = 10
tinggi = 30
luas_segitiga = alas * tinggi
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
