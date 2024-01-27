#inheritance

class Animal:
    
    alive = True
    
    def eat(self):
        print("This animal is eating") #method
        
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("The rabbit is running")
    
    def eat(self):
        print("This rabbit is eating a carrot") #method overrinding
        
class Fish(Animal):
    def swim(self):
        print("The fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("The hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
#fish.swim()
#hawk.fly()
rabbit.eat()