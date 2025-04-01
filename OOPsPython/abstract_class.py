from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod
    def move(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass

class Car(Vehicle):
 
    def move(self):
        print("You drive the car")
    
    def stop(self):
        print("You stop the car")

class Bike(Vehicle):
    def move(self):
        print("you ride the bike")
    def stop(self):
        print("you stop the bike")

class Boat(Vehicle):
    def move(self):
        print("you sail the boat")
    def stop(self):
        print("you stop the boat")
car = Car()
bike = Bike()
boat = Boat()
car.move()
car.stop()
bike.move()
bike.stop()
boat.move()
boat.stop()
