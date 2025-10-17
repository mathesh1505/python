class GrandFather:
    def property(self):
        print("Land and House")

class Father(GrandFather):
    def car(self):
        print("Owns a Car")

class Son(Father):
    def bike(self):
        print("Owns a Bike")

s = Son()
s.property()
s.car()
s.bike()
