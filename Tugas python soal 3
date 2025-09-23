#Toko peralatan sekolah
print("Selamat datang di Toko Peralatan Sekolah!")
list = """
=== Daftar Barang ===
1. Buku Tulis - Rp 5.000
2. Pulpen - Rp 3.500
3. Penghapus - Rp 2.000
4. Beli semua barang di atas
====================="""

while True:
    print(list)
    pilihan = input("Pilih barang yang ingin dibeli (1-4) atau ketik '0' untuk keluar: ")
    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah Buku Tulis yang ingin dibeli: "))
        total = jumlah * 5000
        print(f"Total harga Buku Tulis: Rp {total}")   
    elif pilihan == "2":
        jumlah = int(input("Masukkan jumlah Pulpen yang ingin dibeli: "))
        total = jumlah * 3500
        print(f"Total harga Pulpen: Rp {total}")
    elif pilihan == "3":
        jumlah = int(input("Masukkan jumlah Penghapus yang ingin dibeli: "))
        total = jumlah * 2000
        print(f"Total harga Penghapus: Rp {total}")
    elif pilihan == "4":
        #input jumlah semua barang
        jumlah_buku = int(input("Masukkan jumlah Buku Tulis yang ingin dibeli: "))
        jumlah_pulpen = int(input("Masukkan jumlah Pulpen yang ingin dibeli: "))
        jumlah_penghapus = int(input("Masukkan jumlah Penghapus yang ingin dibeli: "))

        #hitung total semua barang
        total_buku = jumlah_buku * 5000
        total_pulpen = jumlah_pulpen * 3500
        total_penghapus = jumlah_penghapus * 2000
        total_semua = total_buku + total_pulpen + total_penghapus
        pajak = total_semua // 10
        grand_total = total_semua + pajak    
        print(f"Total harga semua barang: Rp {total_semua}")
        #Print struk
        input_struk = input("Print struk? (Y/N): ")
        if input_struk == "Y" or input_struk == "y":
            print("===================================")
            print("           STRUK BELANJA       ")
            print("===================================")
            print(f"Buku Tulis x{jumlah_buku} = Rp {total_buku}")
            print(f"Pulpen x{jumlah_pulpen} = Rp {total_pulpen}")
            print(f"Penghapus x{jumlah_penghapus} = Rp {total_penghapus}")
            print(f"Pajak 10% = Rp {pajak} ")
            print("===================================")
            print(f"Grand Total = Rp {grand_total}")
            print("===================================")
            print("Terima kasih telah berbelanja di Toko Peralatan Sekolah kami!")
            break
        elif input_struk == "N" or input_struk == "n":
            print("Terima kasih telah berbelanja di Toko Peralatan Sekolah kami!")
            break
        else:
            print("Input tidak valid. Kembali ke menu utama.")
            continue
    elif pilihan == "0":
        print("Terima kasih telah berbelanja di Toko Peralatan Sekolah!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
