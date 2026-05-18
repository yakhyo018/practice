''' Comprehension
(1) what is comprehension & list comp.
(2) set and dictionary comp.
'''

print("===== What is comprehension & list comprehension =====")
# Comprehension acts like spread operator!

'''
-- Comprehension general syntax:
a) iterable
b) <expression> for item in iterable
c) <expression> for item in iterable <condition>
'''

# list comp.
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [numbers]  # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("-----")
people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0] for person in people]  # b version
print("list_people:", list_people)

print("-----")
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars:", list_cars)

print("----- set and dictionary comprehension =====")
nums = [1, 5, 4, 20, 4, 5, 1, 4]
set_nums = {*nums}
print("set_nums:", set_nums)

dict_people = {person[0]: person[1] for person in people}  # b version
print("dict_people:", dict_people)

# (expression) for item in iterable) generic
