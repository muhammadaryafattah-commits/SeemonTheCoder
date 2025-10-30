#Forloop
#Soal 1

n = 7
for i in range(n):
    for j in range(n):
        if i == j or i == n-1-j:
            print("*", end=(" "))
        else:
            print(" ", end=(" "))
    print()