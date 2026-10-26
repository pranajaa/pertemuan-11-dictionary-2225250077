def cari_mahasiswa(data, nim):
    if nim in data:
        print("\nData Mahasiswa:")
        print("NIM   :", nim)
        print("Nama  :", data[nim]["nama"])
        print("Kelas :", data[nim]["kelas"])
        print("Nilai :", data[nim]["nilai"])
    else:
        print("\nData mahasiswa tidak ditemukan.")


def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0

    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 82},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88},
    "A006": {"nama": "Fajar", "kelas": "C", "nilai": 80}
}

# Pencarian mahasiswa
print("=== PENCARIAN MAHASISWA ===")
nim_cari = input("Masukkan NIM yang dicari: ")
cari_mahasiswa(data_mahasiswa, nim_cari)

# Penambahan mahasiswa baru
print("\n=== TAMBAH MAHASISWA ===")
nim_baru = "A006"

if nim_baru not in data_mahasiswa:
    data_mahasiswa[nim_baru] = {
        "nama": "Fajar",
        "kelas": "C",
        "nilai": 80
    }
    print("Mahasiswa baru berhasil ditambahkan.")
else:
    print("NIM sudah terdaftar.")

# Pembaruan nilai mahasiswa
print("\n=== PEMBARUAN NILAI ===")
nim_update = "A002"

if nim_update in data_mahasiswa:
    data_mahasiswa[nim_update]["nilai"] = 82
    print("Nilai Budi berhasil diubah menjadi 82.")

# Menampilkan seluruh data mahasiswa
print("\n=== REKAP DATA MAHASISWA ===")

for nim, mahasiswa in data_mahasiswa.items():
    print(
        f"NIM: {nim} | "
        f"Nama: {mahasiswa['nama']} | "
        f"Kelas: {mahasiswa['kelas']} | "
        f"Nilai: {mahasiswa['nilai']}"
    )

# Menghitung rata-rata nilai
print("\n=== RATA-RATA NILAI ===")
rata_rata = rata_rata_nilai(data_mahasiswa)
print(f"Rata-rata nilai seluruh mahasiswa: {rata_rata:.2f}")

# Rekap rata-rata nilai setiap kelas
print("\n=== RATA-RATA NILAI PER KELAS ===")

nilai_kelas = {}

for mahasiswa in data_mahasiswa.values():
    kelas = mahasiswa["kelas"]
    nilai = mahasiswa["nilai"]

    if kelas not in nilai_kelas:
        nilai_kelas[kelas] = []

    nilai_kelas[kelas].append(nilai)

for kelas, daftar_nilai in nilai_kelas.items():
    rata_rata_kelas = sum(daftar_nilai) / len(daftar_nilai)
    print(f"Kelas {kelas}: {rata_rata_kelas:.2f}")
