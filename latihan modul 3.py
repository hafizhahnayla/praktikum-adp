while True:
    angka_pertama = float(input('masukkan angka pertama : '))
    angka_kedua = float(input('masukkan angka kedua : '))
    print('pilih operasi')
    print('1. penjumlahan')
    print('2. pengurangan')
    print('3. perkalian')
    print('4. pembagian')
    print('5. keluar')
    operasi = int(input('pilih operasi : '))
    if operasi==1:
        hasil = angka_pertama+angka_kedua
        print(f'hasil : {hasil}')
    elif operasi==2:
        hasil = angka_pertama-angka_kedua
        print(f'hasil : {hasil}')
    elif operasi==3:
        hasil = angka_pertama*angka_kedua
        print(f'hasil : {hasil}')
    elif operasi==4:
        if angka_kedua==0:
            print('operasi ini tidak terdefinisi')
        else:
            hasil = angka_pertama/angka_kedua
            print(f'hasil : {hasil}')
    else:
        print('terimakasih')
        break


