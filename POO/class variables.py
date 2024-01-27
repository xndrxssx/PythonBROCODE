#class variables

class Car:
    
    wheels = 4 #class variable
    color = None
      
    def __init__(self, make, model, year):
        self.make = make    #instance_variables
        self.model = model  #instance_variables
        self.year = year    #instance_variables
        #self.color = color  #instance_variables
    
    def drive (self):
        print("This "+self.model+" is driving")
        return self #method chaining
        
    def stop (self):
        print("This car is stopped")
        
    def turn_on(self):
        print("You start the engine")
        return self #method chaining
        
    def brake(self):
        print("You step on the brakes")
        return self #method chaining
    
    def turn_off(self):
        print("You turn off the engine")
        return self #method chaining
        
   
car_1 = Car("Chevy", "Corvette", 2021)
#method chaining

car_1.turn_on().drive()

car_1.brake().turn_off()


#object as arguments:

def change_color(car, color):
    car.color = color
    
car_3=Car("Chevy", "Corvette", 2021)
car_4=Car("Chevy", "Corvette", 2021)
car_5=Car("Chevy", "Corvette", 2021)

change_color(car_3, "red")
change_color(car_4, "blue")
change_color(car_5, "pink")

print(car_3.color)
print(car_4.color)
print(car_5.color)
        
