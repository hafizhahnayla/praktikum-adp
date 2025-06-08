data_praktikan = ['2411223301, naina, 79, 83, 98',
                  '2411223302, sisil, 88, 90, 86',
                  '2411223303, kaira, 86, 87, 89',
                  '2411223304, maura, 89, 87, 90',
                  '2411223305, yoola, 97, 89, 74',
                  '2411223306, yauna, 95, 84, 68',
                  '2411223307, qeela, 88, 98, 78',
                  '2411223309, tasya, 87, 89, 92',
                  '2411223309, rayqa, 84, 82, 88',
                  '2411223310, haura, 97, 98, 85']

with open('data_praktikan.txt', 'w') as file:
    for baris in data_praktikan:
        file.write(baris + '\n')

praktikan= {}

with open('data_praktikan.txt', 'r') as file:
    for baris in file:
        nim, nama, pretest, postest, tugas = baris.split(',')
        praktikan[nim] = {'nama': nama,
                          'pretest': int(pretest),
                          'postest': int(postest),
                          'tugas': int(tugas)
                         }

with open('data_nilai_akhir.txt', 'w') as file:
    file.write(f"{'NIM':<12} {'Nama':<8} {'Pretest':<9} {'Postest':<9} {'Tugas':<7} {'Total Nilai':<12}\n")
    file.write("="*61 + "\n")
    for nim, data in praktikan.items():
        nilai_akhir = (0.35 * data["pretest"] + 0.35 * data["postest"] +0.30 * data["tugas"])
        data['nilai_akhir'] = nilai_akhir
        baris = f"{nim:<11} {data['nama']:11} {data['pretest']:<9} {data['postest']:<8} {data['tugas']:<8} {nilai_akhir:<12.2f}"
        file.write(baris + "\n")

total_nilai = [data['nilai_akhir'] for data in praktikan.values()]
rata_rata = sum(total_nilai) / len(total_nilai)
nilai_tertinggi = max(total_nilai)
nilai_terendah = min(total_nilai)
nama_nilai_tertinggi = [data['nama'] for data in praktikan.values() if data['nilai_akhir'] == nilai_tertinggi]
nama_nilai_terendah = [data['nama'] for data in praktikan.values() if data['nilai_akhir'] == nilai_terendah]
nim_nilai_tertinggi = [nim for nim, data in praktikan.items() if data['nilai_akhir'] == nilai_tertinggi]
nim_nilai_terendah = [nim for nim, data in praktikan.items() if data['nilai_akhir'] == nilai_terendah]
praktikan_dibawah_rata2 = [data['nama'] for data in praktikan.values() if data['nilai_akhir'] < rata_rata]

print(f"Rata-rata nilai akhir: {rata_rata:}")
print(f"Nilai tertinggi adalah: {nilai_tertinggi} oleh{''.join(nama_nilai_tertinggi)} dengan nim {','.join(nim_nilai_tertinggi)}")
print(f"Nilai terendah adalah: {nilai_terendah} oleh{''.join(nama_nilai_terendah)} dengan nim {','.join(nim_nilai_terendah)}")
print(f"jumlah praktikan yang memiliki nilai di bawah rata-rata: {len(praktikan_dibawah_rata2)} orang")
print(f"Nama-nama praktikan yang memiliki di bawah rata-rata: {', '.join(praktikan_dibawah_rata2)}")
