# Pertemuan 11 - Dictionary/Map

**Nama:** Hitana Rifa Pranaja 

**NIM:** 2225250077 

**Kelas:** 3A

## Tujuan
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data
Program menggunakan dictionary `data_mahasiswa` dengan NIM sebagai key utama. Setiap value berupa dictionary yang berisi nama, kelas, dan nilai mahasiswa.

## Cara Menjalankan
```bash
python3 praktik/data_mahasiswa.py
```

## Test Case

| Kasus | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Pencarian tersedia | A003 | Data Citra ditampilkan | Data Citra berhasil ditampilkan | Berhasil |
| Pencarian tidak tersedia | A999 | Pesan "Data tidak ditemukan" | Pesan "Data mahasiswa tidak ditemukan" ditampilkan | Berhasil |
| Pembaruan nilai | A002 menjadi 82 | Nilai A002 berubah menjadi 82 | Nilai Budi berhasil diubah menjadi 82 | Berhasil |
| Penambahan data | A006 | Key A006 tersedia setelah ditambahkan | Data mahasiswa A006 berhasil ditambahkan | Berhasil |
| Rekap | `items()` | Semua NIM dan data tampil | Seluruh data mahasiswa ditampilkan | Berhasil |

## Refleksi
Kesalahan akses key dapat terjadi ketika key yang dicari tidak tersedia dalam dictionary. Untuk mengatasinya, program memeriksa keberadaan key menggunakan operator `in` sebelum mengakses data sehingga program dapat menampilkan pesan yang sesuai tanpa mengalami `KeyError`.
