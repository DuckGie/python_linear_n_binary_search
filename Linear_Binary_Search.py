import pandas as pd
from bisect import bisect_left

# Fungsi membaca file Excel
def baca_excel(nama_file):
    df = pd.read_excel(nama_file)
    df.columns = df.columns.str.strip()

    data = []
    for _, row in df.iterrows():
        judul = str(row.get("Judul Paper", "")).strip()
        tahun = str(row.get("Tahun Terbit", "")).strip()

        penulis = str(row.get("Nama Penulis", "")).replace('\n', '').replace('\r', '').strip()
        penulis = penulis.replace(' ,', ',') 
        penulis = " ".join(penulis.split())

        try:
            tahun_float = float(tahun)
            tahun_int = int(tahun_float)

            data.append({
                "Judul": judul,
                "Tahun": tahun_int,
                "Penulis": penulis
            })
        except:
            continue

    return data

# Linear Search
def linear_search(data, keyword, kunci):
    hasil = []
    keyword = keyword.lower().strip()
    for row in data:
        nilai = str(row[kunci]).lower().strip()
        if keyword in nilai:
            hasil.append(row)
    return hasil

# Binary Search 
def binary_search(data, tahun_dicari):
    data_urut = sorted(data, key=lambda x: x["Tahun"])
    tahun_list = [row["Tahun"] for row in data_urut]
    
    index = bisect_left(tahun_list, tahun_dicari)
    hasil = []

    if index < len(tahun_list) and tahun_list[index] == tahun_dicari:
        i = index
        while i >= 0 and tahun_list[i] == tahun_dicari:
            i -= 1
        i += 1

        while i < len(tahun_list) and tahun_list[i] == tahun_dicari:
            hasil.append(data_urut[i])
            i += 1

    return hasil

# Main program
data = baca_excel("dataset.xlsx")

while True:
    print("\n=== MENU PENCARIAN ===")
    print("1. Linear Search - Judul Paper")
    print("2. Linear Search - Nama Penulis")
    print("3. Linear Search - Tahun Terbit")
    print("4. Binary Search - Tahun Terbit")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "0":
        print("Sampai Jumpa Kembali")
        break

    elif pilihan == "1":
        keyword = input("Masukkan kata kunci judul: ")
        hasil = linear_search(data, keyword, "Judul")

    elif pilihan == "2":
        keyword = input("Masukkan nama penulis: ")
        hasil = linear_search(data, keyword, "Penulis")

    elif pilihan == "3":
        keyword = input("Masukkan tahun (angka): ")
        hasil = linear_search(data, keyword, "Tahun")

    elif pilihan == "4":
        tahun = int(input("Masukkan tahun (angka): "))
        hasil = binary_search(data, tahun)

    else:
        print("Pilihan tidak valid.")
        continue

    # Hasil
    if hasil:
        for row in hasil:
            print("---------------------------")
            print(f"Judul   : {row['Judul']}")
            print(f"Tahun   : {row['Tahun']}")
            print(f"Penulis : {row['Penulis']}")
            print("---------------------------\n")
    else:
        print("Data tidak ditemukan.")