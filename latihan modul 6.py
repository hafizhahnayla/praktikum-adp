titik =  []
for i in range (3):
    x = float(input(f'masukkan nilai titik x{i+1} : '))
    y = float(input(f'masukkan nilai titik y{i+1} : '))
    titik.append([x, y])

print(titik)

sisi1 = ((titik[0][0]-titik[1][0])**2 + (titik[0][1]-titik[1][1])**2)*0.5
sisi2 = ((titik[1][0]-titik[2][0])**2 + (titik[1][1]-titik[2][1])**2)*0.5
sisi3 = ((titik[0][0]-titik[2][0])**2 + (titik[0][1]-titik[2][1])**2)*0.5

if sisi1==sisi2 or sisi1==sisi3 or sisi2==sisi3:
    print('ketiga titik tersebut membentuk segitiga sama kaki')
else:
    print('ketiga titik tersebut tidak membentuk segitiiga sama kaki')

print()