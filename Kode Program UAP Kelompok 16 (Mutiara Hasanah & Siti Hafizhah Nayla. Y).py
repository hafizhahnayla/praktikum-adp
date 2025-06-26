import os
import time
from termcolor import cprint
os.system('cls')

cprint('Loading', 'white', end='')
for j in range(5):
    print('..', end='', flush=True)
    time.sleep(0.5)
time.sleep(0.5)

os.system('cls')
teks = ' '*10 + '~ SELAMAT DATANG DI MOODIE ~' + ' '*10
cprint('='*48, 'light_grey')
cprint(teks, 'dark_grey', 'on_light_grey' )
cprint('='*48, 'light_grey')
print()

time.sleep(1.5)
def tampilan_awal():
    cprint(" Menu :        ", 'white', 'on_dark_grey')
    cprint(" 1. Lagu       ", 'dark_grey', 'on_light_grey')
    cprint(" 2. Film       ", 'dark_grey', 'on_light_grey')
    cprint(" 3. Novel      ", 'dark_grey', 'on_light_grey')
    print()

# ===== MENU LAGU =====
def genre_lagu():
    cprint(' Genre :       ', 'white', 'on_dark_grey')
    cprint(" 1. Senang     ", 'dark_grey', 'on_light_grey')
    cprint(" 2. Tenang     ", 'dark_grey', 'on_light_grey')
    cprint(" 3. Galau      ", 'dark_grey', 'on_light_grey')
    cprint(" 4. Butterfly  ", 'dark_grey', 'on_light_grey')
    cprint(" 5. Energik    ", 'dark_grey', 'on_light_grey')

def lagu():
    while True:
        genre_lagu()
        pilihan = input("\nMasukkan pilihan genre (1 - 5): ")

        if pilihan == "1": 
            genre = "senang"
            break
        elif pilihan == "2": 
            genre = "tenang"
            break
        elif pilihan == "3": 
            genre = "galau"
            break
        elif pilihan == "4": 
            genre = "butterfly"
            break
        elif pilihan == "5": 
            genre = "energik"
            break
        else:
            print("Pilihan tidak valid.")
            print()

    data_lagu = {
            "senang": [
                    ["TAYLOR SWIFT:", "Shake it off", "22", "You Belong With Me"],
                    ["MALIQ & D’ESSENTIALS:", "Menari", "Semoga", "Setapak Sriwedari"],
                    ["TWICE", "Feel Special:", "Fancy", "Cheer Up"]
                    ],

            "tenang": [
                    ["DANIEL CAESAR:","Superpowers", "Best Part", "Hold Me Down"],
                    ["NADIN AMIZAH:", "Amin Paling Serius", "Sorai", "Tapi Diterima"],
                    ["LEE HI:", "Only", "Breathe", "My Love"],
                    ],

            "galau": [
                    ["NIKI:", "Autumn", "La La Lost You", "Backburner"],
                    ["Bernadya:", "Satu Bulan", "Lama-Lama","Asumsi"],
                    ["IU:", "Eight", "Love Peom", "My Old Story"]
                    ],

            "butterfly": [
                        ["TAYLOR SWIFT:", "Labirin", "Fearless", "Untouchable"],
                        ["HIVI:", "Satu-satunya", "Gadis Sampul", "Mata Ke Hati"],
                        ["SEVENTEEN:", "Adore U", "Let Me Hear You", "Beautiful"],
                        ],

            "energik": [
                        ['KATY PERRY:', 'Roar', 'Dark Horse', 'Swish Swish'],
                        ['DEWA19:', 'Arjuna','Cinta Gila', 'Sedang Ingin Bercinta'],
                        ['BTS:', 'Fire', 'MIc Drop', 'Dope']
                        ]}

    print(f"\nDaftar lagu genre {genre}:")
    for array in data_lagu[genre]:
        print(f"\n{array[0]}")
        for lagu in array[1:]:
            print(f"  - {lagu}")

    simpan_data("lagu", genre)
    return menu_ulang()

# ===== MENU FILM DAN NOVEL =====
def genre_film_novel():
    cprint(' Genre :       ', 'white', 'on_dark_grey')
    cprint("1. Komedi      ", 'dark_grey', 'on_light_grey')
    cprint("2. Romansa     ", 'dark_grey', 'on_light_grey')
    cprint("3. Fantasi     ", 'dark_grey', 'on_light_grey')
    cprint("4. Horor       ", 'dark_grey', 'on_light_grey')
    cprint("5. Melow       ", 'dark_grey', 'on_light_grey')

def film():
    while True:
        genre_film_novel()
        pilihan = input("\nMasukkan pilihan genre (1 - 5): ")
        
        if pilihan == "1": 
            genre = "komedi"
            break
        elif pilihan == "2": 
            genre = "romansa"
            break
        elif pilihan == "3": 
            genre = "fantasi"
            break
        elif pilihan == "4": 
            genre = "horor"
            break
        elif pilihan == "5": 
            genre = "melow"
            break
        else:
            print("Pilihan tidak valid.")
            print()

    data_film = {
        "komedi": [['Indonesia:', 'Yowis Ben', 'Cek Toko Sebelah'],
                ['Western:', 'Secret Zoo', 'Miss Granny'],
                ['Korea:', 'Man Of Plastic', 'More Than Family']],
        "romansa": [['Indonesia:', 'Habibie & Ainun', 'ILY From 38.000 Ft'],
                    ['Western:', 'Purple Heart', 'My Fault'],
                    ['Korea:', 'Sweet & Sour', 'Love Reset']],
        "fantasi": [['Indonesia:', 'Petualangan Sherina', 'Sweet 20'],
                    ['Western:', 'Maleficent', 'Avangers'],
                    ['Korea:', 'Monstrum', 'Il Mare']],
        "horor": [['Indonesia:', 'Sumala', 'Diambang Kematian'],
                    ['Western:', 'The Nun', 'Insidious'],
                    ['Korea:', 'Darknuns', 'Exhuma']],
        "melow": [['Indonesia:', 'Bila Esok Ibu Tiada', 'Home Sweet Loan'],
                ['Western:', 'La La Land', 'Me Before You'],
                ['Korea:', 'Hope', 'Unforgettable']]}

    print(f"\nDaftar film genre {genre}:")
    for array in data_film[genre]:
        print(f"\n{array[0]}")
        for film in array[1:]:
            print(f"  - {film}")

    simpan_data("film", genre)
    return menu_ulang()

# ===== MENU NOVEL ======

def novel():
    while True:
        genre_film_novel()
        pilihan = input("\nMasukkan pilihan genre (1 - 5): ")

        if pilihan == "1": 
            genre = "komedi"
            break
        elif pilihan == "2": 
            genre = "romansa"
            break
        elif pilihan == "3": 
            genre = "fantasi"
            break
        elif pilihan == "4": 
            genre = "horor"
            break
        elif pilihan == "5": 
            genre = "melow"
            break
        else:
            print("Pilihan tidak valid.")
            print()
    data_novel = {
            "komedi": ["Cado-Cado", "Ngomongin Orang", "Koala Kumal", "Berburu Restu", "Teori Tawa", "Resign"],
            "romansa": ["Butterfly", "Galaksi", "Mariposa", "Hallo, Cello", "Malioboro at Midnight", "Terpikat"],
            "fantasi": ["Bumi", "Dunia Tanpa Warna", "Nightfall", "The Major", "The Atala", "Semua Ikan di Langit"],
            "horor": ["Gadis Kretek", "Aroma Karsa", "Danur", "Malice", "Real Face", "Masquerade"],
            "melow": ["Laut Bercerita", "Pelangi Waktu Malam", "Hujan", "Rindu", "Serangkai", "Sudut Tersepi Bumi"]
        }

    print(f"\nDaftar novel genre {genre}:")
    for array in data_novel[genre]:
        print(f"  - {array}")

    simpan_data("novel", genre)
    return menu_ulang()

# ===== MENU ULANG ======
def menu_ulang():
    print()
    print("\n1. Kembali ke menu awal")
    cprint("2. Keluar", 'red')
    while True:
        pilih = input("Masukkan pilihan (1/2): ")
        print()
        if pilih == "1":
            os.system('cls')
            return True
        elif pilih == "2":
            teks = ' '*7 + '~ TERIMAKASIH! SAMPAI JUMPA LAGI ~' + ' '*7
            cprint('='*48, 'light_grey')
            cprint(teks, 'dark_grey', 'on_light_grey' )
            cprint('='*48, 'light_grey')
            print()
            exit()
        else:
            print("Pilihan tidak valid. Masukkan 1 atau 2.")
            print()
     
# ====== FITUR FILE TEXT - SIMPAN HISTORI PENGGUNA =====

def simpan_data(menu, genre):
    with open("data_moodie.txt", "a", encoding="utf-8") as file:
        file.write(f"{menu.upper()} - Genre: {genre.capitalize()}\n")

# ====== PROGRAM TAMPILAN =====

def tampilan():
    while True:
        tampilan_awal()
        pilih = input("Masukkan nomor menu: ")
        print()
        if pilih == "1":
            lagu()
        elif pilih == "2":
            film()
        elif pilih == "3":
            novel()
        else:
            print("Pilihan tidak valid.")
            print()

# ====== PROGRAM UTAMA ======

def program_utama():
    tampilan()

program_utama()