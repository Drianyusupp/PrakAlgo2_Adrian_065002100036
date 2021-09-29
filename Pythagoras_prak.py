Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from math import sqrt
print("Asumsikan sisi-sisinya adalah a,b,c dengan c sebagai sisi miring")
formula = input('Sisi mana yang ingin anda hitung = ')

if formula == 'c':
    sisiA = int(input('Masukkan panjang sisi a = '))
    sisiB = int(input('Masukkan panjang sisi b = '))
    
    sisiC = sqrt(sisiA*sisiA + sisiB*sisiB)
    print('Panjang sisi c adalah', sisiC)
    
elif formula == 'a':
    sisiC = int(input('Masukkan panjang sisi c = '))
    sisiB = int(input('Masukkan panjang sisi b = '))
if (sisiC<sisiB):
    print('Panjang sisi c tidak valid! ')
    sisiC = int(input('Masukkan panjang c = '))
    sisiA = sqrt(sisiC*sisiC - sisiB*sisiB)
    print('Panjang sisi a adalah', sisiA)
    
elif formula == 'b':
    sisiC = int(input('Masukkan panjang sisi c = '))
    sisiA = int(input('Masukkan panjang sisi a = '))
if (sisiC<sisiA): 
    print('Panjang c tidak valid! ')
    sisiC = int(input('Masukkan panjang c = '))
    sisiB = sqrt(sisiC*sisiC - sisiA*sisiA)
    print('Panjang sisi b adalah', sisiB)