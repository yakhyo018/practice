"""
    List
    (1) Working with lists
    (2) List methods
    (3) Lambda function
    (4) enumarate, map and filter
"""

print("===== Working with lists =====")
# Java/PHP/NodeJS array => Python list

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list

for team in groups:
    print(f"the team: {team}")


# constructor
letters = list("Hello World!")
print(f"the letters: {letters} and size: {len(letters)}")

print("------")

fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]   # [0, 2)
c = fruits[::3]  # 0 indexni oladi va 3 index ni oladi
d = fruits[::-1]  # bu reverse qiladi

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("===== List methods =====")
# methods = append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]

letters.append("c")  # add behind
print(f"the append letters: {letters}")

letters.insert(0, "z")  # add front
print(f"the insert letters: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop front
print(f"the pop result2: {result2} and letters: {letters}")

print("------")

animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("animals remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)

animals.clear()
print("animals clear:", animals)

if "cat" in animals:
    print(f"index of cat: {animals.index("cat")}")
else:
    print("cat does not exist")

print("------")
numbers = [2, 20, 12, 8, 57]

numbers.sort()
print("sort default:", numbers)

numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable > sorted function & index() method
numbers = [2, 20, 12, 100]
new_numbers = sorted(numbers)

print(f"the sorted nums: {numbers} and new_numbs: {new_numbers}")

print("===== Lambda function =====")
# lambda is small anonymous function!


def calculate(x, y):
    return x * y


result = calculate(3, 5)
print("result:", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]

people.sort()
print("people(1)", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])
print("people(2)", people)

print("===== enumarate, map and filter =====")
# Enumerate for index and value

Animals = ["dog", "cat", "fish"]  # list
for element in enumerate(Animals):
    print("element:", element)

for (index, value) in enumerate(Animals):
    print(f"the index {index} and the value {value}")

print("------")
# similar in dictionaries
car_obj = dict(brand="ferrari", year=2025)  # dict
result = car_obj.items()
for (key, value) in result:
    print(f"The key: {key} and the value: {value}")

print("------")
# Map
Cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33),
]
new_cars = []
for car in Cars:
    new_cars.append(car[0])
print("new_cars", new_cars)

result_map = map(lambda car: car[0], Cars)
print(f"the result_map: {result_map} and type: {type(result_map)}")
new_cars = list(result_map)
print("new_cars", new_cars)

print("------")
# filter
result_filter = filter(lambda car: car[1] > 80, Cars)
print(f"the result_filter {result_filter} and type: {type(result_filter)}")
print(list(result_filter))
