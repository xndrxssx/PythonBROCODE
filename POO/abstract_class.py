from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    
    @abstractclassmethod #obriga os demais a herdar os metodos 
    def go(self):
        pass
    
    @abstractclassmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def go(self):
        print("You drive the car")
        
    def stop(self):
        print("Stopped")
    
class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
        
    def stop(self):
        print("Stopped")
    

#vehicle = Vehicle()
car = Car ()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
car.stop()

