class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"The {self.name} is eating")

    def sleep(self):
        print(f"The {self.name} is asleep")
    
class dog(Animal):
    pass
    def speak(self):
        print("Woof")
class cat(Animal):
    pass
    def speak(self):
        print("Meow")
class cow(Animal):
    pass
    def speak(self):
        print("MOO")

dog = dog("Bruno")
cat = cat("Tom")
cow = cow("Bingo")

print(dog.name,dog.is_alive)
print(cat.name,cat.is_alive)
print(cow.name,cow.is_alive)
dog.eat(), dog.sleep()
cat.eat(), cat.sleep()
cow.eat(), cow.sleep()
dog.speak()
cat.speak()
cow.speak()