
baris = 5
for i in range(baris):
    for s in range(baris - i):
        print(" ", end="")
    n = 1
    for z in range(i + 1):
        print(n, end=" ")
        n = n * (i-z) // (z+1)
    print()