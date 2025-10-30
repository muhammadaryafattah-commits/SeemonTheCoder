def is_prime(x):
    if x < 2:
        return False
    for k in range(2, int(x**0.5) + 1):
        if x % k == 0:
            return False
    return True

num = 1
for i in range(10):
    for j in range(10):
        if is_prime(num):
            print("P", end=("\t"))
        else:
            print(num, end=("\t"))
        num += 1
    print()