from abc import ABC

class Vehicle(ABC):
    def start(self):
        pass
    def stop(self):
        print("Vehicle stopped")
class Car(Vehicle):

    def start(self):
        print("Car engine started")

class Bike(Vehicle):

    def start(self):
        print("Bike started with self-start")

c = Car()
c.start()
c.stop()

b = Bike()
b.start()
b.stop()
