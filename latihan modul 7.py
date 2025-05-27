def menu():
    print('====================================')
    print()
    print("Menu:")
    print("1. Tabel perkalian modulo n")
    print("2. Mencari nilai Σ x")
    print("3. Mencari nilai n!")
    print("4. Total dan rata-rata suatu data")
    print("5. Keluar")
    print()

def tabel_perkalian_modulo():
    while True:
        n = int(input("Masukkan nilai n (0 < n ≤ 10): "))
        if 0 < n <= 10:
            break
        else:
            print("Input tidak valid. Nilai n harus dalam interval 1 - 10")
    
    print(f"Tabel Perkalian Modulo {n}:")
    print(" x"+" |", end="")
    for i in range(n):
        print(f"{i:3}", end="")
    print("\n" + "-" * (n * 3 + 4))
    for i in range(n):
        print(f"{i:2} |", end="")
        for j in range(n):
            print(f"{(i*j)%n:3}", end="")
        print()

def sigma_x():
    print(f'Mencari nilai dari Σ x')
    while True:
        bawah = int(input("Masukkan batas bawah: "))
        atas = int(input("Masukkan batas atas: "))
        if atas >= bawah:
            break
        else:
            print("Batas atas harus lebih besar atau sama dengan batas bawah.")
    
    print(f'Nilai dari Σ x dengan batas bawah {bawah} dan batas atas {atas} adalah : ')
    total = 0
    for i in range(bawah, atas+1):
        total += i
    print("Σ x =", total)

def faktorial():
    print('Mencari nilai faktorial dari n')
    while True:
        n = int(input("Masukkan nilai n: "))
        if n >= 0:
            break
        else:
            print("nilai n harus ≥ 0")

    hasil = 1
    for i in range(2, n+1):
        hasil *= i
    print(f"{n}! =", hasil)

def total_rata_rata():
    print(f'Mencari nilai rata-rata')
    while True:
        n = int(input("Masukkan banyak data (n): "))
        if n > 0:
            break
        else:
            print("Jumlah data harus lebih dari 0")
        
    data = []
    for i in range(n):
        while True:
            nilai = float(input(f"Data ke-{i+1}: "))
            data.append(nilai)
            break

    total = 0
    for nilai in data:
        total += nilai
    rata2 = total / n
    print("Total =", total)
    print("Rata-rata =", rata2)

def pilihan():
    while True:
        menu()
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            tabel_perkalian_modulo()
        elif pilihan == '2':
            sigma_x()
        elif pilihan == '3':
            faktorial()
        elif pilihan == '4':
            total_rata_rata()
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-5.")
        print()

pilihan()
print() 