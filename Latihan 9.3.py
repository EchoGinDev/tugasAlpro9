nama_file = "berita.txt"
try:
    with open(nama_file, "r", encoding="utf-8") as file:
        for line in file:
            kata = line.split()
            print(f"Kata unik dalam kalimat: {kata}")
except FileNotFoundError:
    print("File tidak ditemukan.")

