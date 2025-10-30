number = 2 
total = 0

for i in range(2):
    for z in range(5):
        print(number, end="\t") #Overwrite print
        total += number
        number +=2 
    print() #Print yg asli disini
print(f"Total: {total}")
