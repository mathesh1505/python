
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    def start(self):
        print(f"{self.color} {self.brand} {self.model} is starting...")

    def stop(self):
        print(f"{self.brand} {self.model} has stopped.")
car1 = Car("Tata", "Nexon", "Blue")
car2 = Car("Hyundai", "Creta", "White")
car1.start()
car2.start()
car1.stop()
