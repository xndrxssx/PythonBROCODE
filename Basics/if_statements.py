age = int(input("How old are you?: "))

if age == 100:
    print("You're a century old!")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 18:
    print("You're an adult!")
else:
    print("You're a child!")
