class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"The {self.name} is eating")
    def sleep(self):
        print(f"The {self.name} is sleeping")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Prey(Animal):
    def run(self):
        print(f"{self.name} belongs to 'prey' category, cannot hunt")

class Rabbit(Prey):                                                           
    pass
class Lion(Predator):
    pass
class Frogs(Predator,Prey):         #Multiple inheritance
    pass

rabbit = Rabbit("Henry")
lion = Lion("Mufasa")
frog = Frogs("Hawk")

rabbit.run()
lion.hunt()
frog.hunt()
frog.run()
rabbit.eat(),rabbit.sleep()
lion.eat(), lion.sleep()
frog.eat(), frog.sleep()