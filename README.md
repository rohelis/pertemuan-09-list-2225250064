# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Rohelis
NIM: 2225250064
Kelas: 3B

## Tujuan
Mengolah kumpulan data numerik menggunakan list Python, melakukan manipulasi data, agregasi, filtering, serta membungkus fungsi untuk analisis statistik nilai mahasiswa.

## Struktur Program
- `02_indeks_slicing.py`: Program untuk mengakses elemen pertama, terakhir, dan melakukan *slicing* pada list nilai.
- `03_manipulasi_list.py`: Program untuk melakukan perubahan nilai, penambahan (`append`), penyisipan (`insert`), dan penghapusan (`remove`) pada list.
- `04_agregasi_nilai.py`: Program untuk menghitung total, rata-rata, nilai minimum, dan maksimum menggunakan fungsi agregasi bawaan Python.
- `05_filter_kelulusan.py`: Program untuk menyaring nilai mahasiswa yang memenuhi batas kelulusan (>= 60).
- `06_fungsi_statistik.py`: Program untuk menghitung rata-rata menggunakan fungsi kustom (`def`).
- `praktik/analisis_nilai_mahasiswa.py`: Program utama analisis data nilai mahasiswa yang menggabungkan seluruh konsep di atas (statistik, fungsi, dan filter kelulusan).

## Cara Menjalankan
Jalankan program praktik utama melalui terminal/command prompt:
```bash
python3 praktik/analisis_nilai_mahasiswa.py
## Test Case

| No | Data Nilai | Hasil yang Diharapkan | Hasil Aktual | Status |
|----|------------|-----------------------|--------------|--------|
| 1  | `[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]` | Banyak data: 10, Rata-rata: 69.50, Jumlah Lulus: 7, Jumlah Belum Lulus: 3 | Sesuai | **Lulus** |

## Refleksi
- **Hal yang dipahami**: Saya memahami cara mengakses elemen list menggunakan indeks positif maupun negatif, melakukan *slicing*, serta mengolah data numerik secara efisien menggunakan fungsi dan perulangan.
- **Kesalahan yang berhasil diperbaiki**: Sempat terjadi kesalahan logika pada perhitungan jumlah mahasiswa belum lulus, yang kemudian berhasil diperbaiki dengan mengurangkan total banyak data dengan jumlah mahasiswa yang lulus (`banyak_data - jumlah_lulus`).