#tuple

student = ("Bro", 21, "Male")
#index       0     1     2

print(student.count("Bro")) #untuk mengecek berapa kali value "Bro" muncul didalam variable student
print(student.index("Bro")) #Untuk mengecek value "Bro" ada di index berapa, dan untuk tuple disini indexnya dimulai dari 0

#Cari penjelasan untuk kode dibawah ini
for x in student:
    print(x)

#Jika ada "Bro" didalam variable student yang dimana hasilnya True, kenapa true? karna value "Bro" ada didalam student, jika true maka akan memberikan ouput "Bro is here!"
if "Bro" in student:
    print("Bro is here!")