#======================== BIOSKOP ========================
menu = """
Lihat Film
Lihat Kursi
Beli Tiket
Cek Tiket
Keluar
"""

film = [
    {"judul": "Avatar 3", "harga": 50000},
    {"judul": "Inside Out 2", "harga": 45000},
    {"judul": "Venom 3", "harga": 55000},
    {"judul": "Siksa Kubur", "harga": 40000}
]

kursi = {f["judul"]: [f"A{i}" for i in range(1, 6)] for f in film}
tiket = []

def tampil_film():
    for i, f in enumerate(film, 1):
        print(f"{i}. {f['judul']} - Rp{f['harga']}")

while True:
    print(menu)
    try:
        p = int(input("Pilih menu: "))
    except:
        print("Input salah."); continue

    if p == 1:
        tampil_film()

    elif p == 2:
        tampil_film()
        idx = int(input("Pilih film: ")) - 1
        j = film[idx]['judul']
        print("Kursi tersedia:", kursi[j] if kursi[j] else "Penuh")

    elif p == 3:
        tampil_film()
        idx = int(input("Film ke: ")) - 1
        f = film[idx]; j = f['judul']
        print("Kursi:", kursi[j])
        n = int(input("Jumlah tiket: "))
        if n > len(kursi[j]): print("Kursi tidak cukup."); continue
        pilih = []
        for i in range(n):
            k = input(f"Pilih kursi ke-{i+1}: ").upper()
            if k in kursi[j]: pilih.append(k); kursi[j].remove(k)
            else: print("Kursi tidak valid."); break
        total = f['harga'] * len(pilih)
        tiket.append((j, pilih, total))
        print(f"Tiket {j} dibeli ({', '.join(pilih)}) total Rp{total}")

    elif p == 4:
        if not tiket: print("Belum ada tiket.")
        else:
            for i, t in enumerate(tiket, 1):
                print(f"{i}. {t[0]} | Kursi: {', '.join(t[1])} | Rp{t[2]}")

    elif p == 5:
        print("Terima kasih!"); break

    else:
        print("Pilih 1-5 saja.")

    print()