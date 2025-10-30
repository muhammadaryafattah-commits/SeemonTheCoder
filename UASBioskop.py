#Tampilan menu
menu = """=============BIOSKOP===============
1. Lihat Film yang sedang tayang
2. Lihat studio yang tersedia
3. Check tiket
4. Beli tiket
5. Keluar dari program
==================================="""

#List studio
studios = [
    {"Studio": "Reguler"},
    {"Studio": "IMAX"}
]

#list film 
film = [
    {"Judul": "Venom", "Harga": 53000, "Jam": ("10:00", "13:00", "15:00")},
    {"Judul": "Look Back", "Harga": 52000, "Jam": ("13:00", "16:00", "19:00")},
    {"Judul": "Transformers ONE", "Harga": 55000, "Jam": ("15:00", "17:00", "21:00")}
]

# Membuat daftar kursi untuk setiap film
kursi = {f["Judul"]: [f"A{i}" for i in range(1, 4)] for f in film}

# Set untuk melacak kursi yang sudah dibeli (tidak bisa double)
kursi_terisi = {f["Judul"]: set() for f in film}

# List untuk menyimpan data tiket
tiket = []

# =================== Fungsi ===================
def tampilan_studio():
    print(f"\nDaftar studio yang tersedia:")
    for z in range(len(studios)):
        studio = studios[z]["Studio"]
        print(f"{z + 1}. {studio}")

def tampilan_film():
    print("\nDaftar Film yang Sedang Tayang:")
    for i in range(len(film)):
        judul = film[i]["Judul"]
        harga = film[i]["Harga"]
        jam_tayang = ", ".join(film[i]["Jam"])
        print(f"{i + 1}. {judul} - Harga: Rp{harga} - Jam Tayang: {jam_tayang}")

def tampilin_tiket():
    if tiket:
        print("\nDaftar Tiket yang Kamu Miliki:")
        for i in tiket:
            print(i, end=("\n"))
        print()
    else:
        print("\nKamu belum memiliki tiket")

def beli_tiket():
    tampilan_film()
    pilih = int(input("\nPilih nomor film: "))

    if 1 <= pilih <= len(film):
        
        judul = film[pilih - 1]["Judul"]
        harga = film[pilih - 1]["Harga"]
        print(f"\nKursi yang tersedia untuk film {judul}: {kursi[judul]}")
        print(f"Kursi yang sudah terisi: {kursi_terisi[judul] if kursi_terisi[judul] else 'Belum ada yang terisi'}")
        
        jam = input("Pilih jam tayang: ")
        kursi_pilih = input("Pilih kursi (misal A1): ")

        # Mengecek apakah kursi sudah dibeli
        if kursi_pilih in kursi_terisi[judul]:
            print("\nKursi ini sudah dipesan! Silakan pilih kursi lain.")
        elif kursi_pilih not in kursi[judul]:
            print("\nKursi tidak valid. Pilih kursi yang tersedia di daftar.")
        else:
            kursi_terisi[judul].add(kursi_pilih)  # Menambahkan ke set
            tiket_baru = f"{judul} | Jam: {jam} | Kursi: {kursi_pilih} | Harga: Rp{harga}"
            tiket.append(tiket_baru)
            print("\nTiket berhasil dibeli!")
    else:
        print("Nomor film tidak valid.")

# =================== Program Utama ===================

while True:
    print(f"\n{menu}")
    input_choice = int(input(f"\nMenu apa yang ingin anda kunjungi?: "))
    
    if input_choice == 1:
        tampilan_film()
    elif input_choice == 2:
        tampilan_studio()
    elif input_choice == 3:
        tampilin_tiket()
    elif input_choice == 4:
        beli_tiket()
    elif input_choice == 5:
        print("Terimakasih karena telah menggunakan sistem kami!")
        break
    else:
        print("Pilih opsi dari 1-5")