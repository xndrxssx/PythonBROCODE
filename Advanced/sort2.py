students = [("Caua", "F", 60),
            ("Nicolle", "A", 33),
            ("Zé", "D", 36),
            ("Luiz", "B", 20),
            ("Augusto", "C", 78)
]

grade = lambda grades:grades[1]
students.sort(key=grade, reverse=True)

for i in students:
    print(i)