// Konversi suhu



print('Program Konversi Suhu Sederhana')
pilihan = input('Pilih jenis konversi yang diinginkan : ')
suhu = float(input('Masukkan suhu °C : '))

if pilihan == 'C ke F':
    hasil = (suhu*9/5)+32
    print('suhu ', suhu, ' °C dalam Farenheit adalah ', hasil, 'F')
elif pilihan == 'C ke K':
    hasil = suhu + 273.15
    print('suhu ', suhu, ' °C dalam Kelvin adalah ', hasil, 'K')
elif pilihan == 'C ke R':
    hasil = suhu * 4/5
    print('suhu ', suhu, ' °C dalam Reamur adalah ', hasil, 'R')
else:
    print('Pilihan tidak valid')