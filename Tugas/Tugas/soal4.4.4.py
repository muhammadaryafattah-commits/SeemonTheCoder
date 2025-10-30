n = 6
for i in range(n):
    for z in range(n):
        #Buat bordernya
        if i == 0 or i == n - 1 or z == 0 or z == n - 1:
            print("#", end=(" "))
        #Buat pola ditengah border
        elif 2 <= i <= 3 and 2 <= z <= 3:
            print("#", end=(" "))
        else:
            print(" ", end=(" "))
    print()