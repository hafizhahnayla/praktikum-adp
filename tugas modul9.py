import os
import time
from termcolor import cprint

text = " ✨Happy Eid✨ " * 5  # teks diulang agar bisa lanjut terus
jeda = 0.2
durasi = 20
perulangan = int(durasi/ jeda)
ukuran_frame = 20  # lebar teks dalam bingkai
line = ' '*ukuran_frame + text


for i in range(perulangan):
    os.system('cls')  # bersihkan layar

    tampilan = line[i:i+ukuran_frame]  # ambil bagian teks untuk ditampilkan
    garis_bingkai = "+" + "-" * (ukuran_frame+2) + "+"

    if i % 2 == 0:
        cprint(garis_bingkai, 'red', attrs=['bold'])  #garis atas bingkai
        cprint(tampilan.ljust(ukuran_frame), 'red', attrs=['bold'])          #tampilan teks
        cprint(garis_bingkai, 'red', attrs=['bold'])  #garis bawah bingkai
    else:
        cprint(garis_bingkai, 'blue', attrs=['bold'])   #garis atas bingkai
        cprint(tampilan.ljust(ukuran_frame), 'blue', attrs=['dark'])         #tampilan teks 
        cprint(garis_bingkai, 'blue', attrs=['bold']) #garis bawah bingkai


    time.sleep(jeda)