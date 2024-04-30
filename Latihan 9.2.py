angka = []

print("Masukkan angka satu per satu (ketik 'done' untuk selesai):")
while True:
    angka_input = input("Angka: ")
    if angka_input == 'done':
        break
    try:
      list_angka = float(angka_input)
      angka.append(list_angka)
    except ValueError:
      print("Format Nilai salah. Silahkan masukan nilai atau 'done'.")

maxNum = max(angka)
minNum = min(angka)

if angka:
    print(f"Nilai maksimum: {maxNum}")
    print(f"Nilai minimum: {minNum}")
else:
    print("Nilai kosong, Silahkan masukan nilai!")
