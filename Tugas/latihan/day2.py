#dictionary
#dictionary itu punya key dan value
#operation dictionary adalah .get(), .keys(), .value(), .update()
#.clear() juga ada
#.key() untuk menampilkan semua key, begitu juga dengan .value()
#.items() untuk mgencek semua items yg ada di dictionary
users = {
    "andi123": "password123",
    "budi456": "pass456",
    "citra789": "citra@123"
}

def checkValidUser(users_dict,username,password ):
    return username in users_dict and users_dict[username] == password

def register(users_dict):
    register_user = input("Buat username baru: ")

    if register_user in users_dict:
        print("Akun ini sudah terdaftar.")
        return False
    
    register_pass = input("Buat password baru: ")
    users_dict[register_user] = register_pass
    print("Registrasi berhasil!")
    return True

def main():
    tries = 0 
    while True:
        username = input("Masukkan username: ")
        passwords = input("Masukkan password: ")

        # Cek login valid
        if username in users and users[username] == passwords:
            print("Login berhasil! ")
            break

        #Kalau username belum terdaftar
        elif username not in users:
            print("Username belum terdaftar. Apakah ingin register?")
            choice_regist = input("Y/N: ").lower()
            if choice_regist == "y":
                registered = register(users)
                if registered:
                    continue
                else:
                    continue
            else:
                print("Exiting...")
                break
        else:
            tries += 1
            print(f"Password salah, Coba lagi Percobaan ke-{tries}")

        if tries == 3:
            print("Anda kena blacklist")
            break

    print(users)

if __name__ == "__main__":
    main()