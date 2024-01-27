#filter(function, iterable)

friends = [("Caua", 19),
           ("Nicolle", 18),
           ("Hanah", 19),
           ("Zé", 17),
           ("Augusto", 21),
           ("Joao Pedro", 17)]

age = lambda data:data[1] >= 18

drinking = list(filter(age, friends))

for i in drinking:
    print(i)

