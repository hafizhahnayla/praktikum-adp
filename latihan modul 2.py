print('Pesanan Makanan Online')
print('----------------------')
print('jenis paket makanan :')
print('ayam = Rp.20000')
print('sapi = Rp.35000')
print('cumi-cumi = Rp.45000')

jenis_paket_makanan = str(input('masukkan jenis paket makanan : '))

if jenis_paket_makanan=='ayam':
    harga = 20000
elif jenis_paket_makanan =='sapi':
    harga = 35000
else:
    harga = 45000

jarak = float(input('masukkan jarak rumah ke restoran dalam KM : '))
if jarak<1:
    ongkir = 0
elif 1<=jarak<=3:  
    ongkir = 7000
else:
    ongkir = 15000

biaya_total = harga + ongkir
# print(jenis_paket_makanan) 
# print(biaya_pengiriman)      
print(f'harga paket makanan anda adalah {harga} dan biaya pengiriman sebesar {ongkir}. Jadi, total pembelian andalah adalah {biaya_total}')