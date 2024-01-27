class Duck:
    def walk(self):
        print("walking")
        
    def talk(self):
        print("qwuacking")
        
class Dog:
  
    def talk(self):
        print("barking")
        
class Person():
    def catch(self,duck):
        duck.talk()
        print("you caught him")
        
        
duck = Duck()
dog = Dog()
person = Person()

person.catch(dog)