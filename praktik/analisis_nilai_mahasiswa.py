def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    lulus = []
    for x in data:
        if x >= batas:
            lulus.append(x)
    return lulus

nilai = []

# Gunakan fungsi dan tampilkan ringkasan
banyak_data = len(nilai)
total_nilai = sum(nilai)
rerata = rata_rata(nilai)
nilai_min = min(nilai)
nilai_maks = max(nilai)

list_lulus = nilai_lulus(nilai, batas=60)
jumlah_lulus = len(list_lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

print("=== RINGKASAN ANALISIS NILAI ===")
print(f"Data Nilai           : {nilai}")
print(f"Banyak Data          : {banyak_data}")
print(f"Total Nilai          : {total_nilai}")
print(f"Rata-rata            : {rerata:.2f}")
print(f"Nilai Minimum        : {nilai_min}")
print(f"Nilai Maksimum       : {nilai_maks}")
print("--------------------------------")
print(f"Jumlah Lulus         : {jumlah_lulus}")
print(f"Jumlah Belum Lulus   : {jumlah_belum_lulus}")
print(f"Daftar Nilai Lulus   : {list_lulus}")