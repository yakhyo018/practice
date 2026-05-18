"""
CLASS deep diving
(1) ENCAPSULATION
(2) INHERITENCE
(3) POLIMORPHISM
"""

print("===== INHERITENCE =====")

# PARENT > CHILD
# PRENT provides only Public & Protected properties(state and method) to childreen!


class Animal:  # Parent
    description = "The class is parent for animals"

    def __init__(self, voice):
        self.status = "The animal is alive!"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # Child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}~{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

    def make_voice(self):
        print(f"the {self.name} says: {self.sound}")


class Cat(Animal):  # Child
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}~{self.sound}")

    def play(self):
        print("Yes, I can play with you!")


class Fish(Animal):  # Child
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}~{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "Zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("-------")

dog.make_voice()
cat.make_voice()
fish.make_voice()

print("-------")

print(Animal.description)
print(dog.description)

print("-------")
print(dog.voice, cat.voice)
print(dog.status)


print("===== POLIMORPHIZM =====")

dog.make_voice()
fish.make_voice()

print("--------")
# fish > Fish > Animal > Object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"The result: {result}")

# Fish > Animal > Object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print(data1, data2)
