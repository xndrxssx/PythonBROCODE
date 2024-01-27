from variables import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

#print(car_1.make)
#print(car_1.model)
#print(car_1.year)
#print(car_1.color)

#car_1.drive()
#car_1.stop()

#car_1.wheels = 2

Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)

#print(Car.wheels)

