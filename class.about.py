""" Class
    (1) What is class
    (2) ordinary vs static properties
    (3) special methods
"""

print("=== What is Class ====")


class Person():
    # state
    message = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def Introduce(self):
        print(f"{self.name} says: How do you do")

    def say_age(self):
        print(f"{self.name} says i am {self.age}!")

    @classmethod    # static method
    def explain(cls):
        print("static method property executed!")


person1 = Person("yakhyo", 21)
person2 = Person("Feride", 20)

# ordinary state
print("person1:", person1.name)

# ordinary method
person2.Introduce()
person1.say_age()

# static method
Person.explain()


print("==== special/magic methods =====")

# Python's most common special methods are below!
# __init__ __new__ __str__ __call__ __getItem__ __len__ __eq__ ...


class Car():
    # state
    description = "this class makes cars"

    # constructor

    def __new__(cls, *args):
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def startEngine(self):
        print(f"The {self.name} started engine")

    def stopEngine(self):
        print(f"The {self.name} stopped engine!")

    def __str__(self):
        return f"{self.name} was produced {self.year} year!"

    def __call__(self):
        print("hi")


my_car = Car("Ferrari", 2026)
my_car.startEngine()
my_car.stopEngine()

print("-------")
your_car = Car("supra", 2010)

# print(your_car)
# response = your_car()
# print("your_car", response)

your_car()
