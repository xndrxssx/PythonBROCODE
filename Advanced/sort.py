students = ["Caua", "Nicolle", "Gandhi", "Luiz", "Hanah"]
#nao funciona com tuplas
#students.sort(reverse=True) #usar reverse=True organiza ao contrario
#sort é pra listas

sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)