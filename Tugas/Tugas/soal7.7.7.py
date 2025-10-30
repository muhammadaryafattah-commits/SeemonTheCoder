N = 7

for i in range(N // 2 + 1): 
    for j in range(i):
        print(" ", end="")       
    for k in range(N - i):
        print("* ", end="")       
    print()
    
for i in range(N // 2 - 1, -1, -1): 
    for j in range(i):
        print(" ", end="")
    for k in range(N - i):
        print("* ", end="")
    print()