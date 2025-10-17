class Student:
    def __init__(self, name, marks):
        self.__name = name       
        self.__marks = marks     
    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Please enter between 0 and 100.")
s1 = Student("Mathesh", 85)
print("Name:", s1.get_name())
print("Marks:", s1.get_marks())
s1.set_marks(92)
print("Updated Marks:", s1.get_marks())

