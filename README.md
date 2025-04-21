# 📚 Pencarian Data Paper (Linear & Binary Search) dari Excel

Proyek Python ini dibuat untuk membaca data dari file Excel (.xlsx) dan memungkinkan pengguna melakukan pencarian berdasarkan:

- Judul Paper
- Tahun Terbit
- Nama Penulis

Dua metode pencarian yang digunakan:
- **Linear Search**: Mencari data satu per satu, cocok untuk pencarian kata kunci.
- **Binary Search**: Pencarian cepat berdasarkan Tahun Terbit, membutuhkan data terurut.

---

## 📦 Library yang Digunakan

- `pandas`: Untuk membaca dan mengolah file Excel.
- `bisect`: Untuk melakukan binary search menggunakan `bisect_left`.

---

## 🧠 Fitur Utama

✅ Membaca file Excel dan mengekstrak kolom:
- `Judul Paper`
- `Tahun Terbit`
- `Nama Penulis`

✅ Membersihkan data dari karakter `\n`, `\r`, dan spasi berlebihan.

✅ Menu interaktif di terminal untuk melakukan pencarian.

✅ Hasil pencarian ditampilkan dalam format rapi:

