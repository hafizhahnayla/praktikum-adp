n = int(input("Masukkan nilai n (minimal 4): "))
BOOM = 0
if n < 4:
    print("nilai n minimal adalah 4")
else:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if n % 2 ==1 and i == j == (n//2)+1:
                print(f" HORE ", end="")
            elif i == j:
                print("   1  ",end="")
            elif i + j == n + 1:
                print("   2  ",end="")  
            else:
                print(" BOOM ", end="")
                BOOM = BOOM+1
        print()
print(f'Total BOOM yang muncul sebanyak = {BOOM}')