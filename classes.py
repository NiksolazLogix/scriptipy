class NumberHolder:
    def __init__(self, number):
        self.number = number

    def sumForFive(self):
        return self.number * 5


firstObj = NumberHolder(4)

x = firstObj.sumForFive()
print(x)

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)
print(p1)


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname + " " + self.lname)

class Student(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname,lname)
        self.age = age
    def printname(self):
        print(self.fname + " " + self.lname + " " + self.age)

student = Student("Nix", "Olaz", "47")

student.printname()
