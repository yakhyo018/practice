'''
OBJECTS
(1) What is object
(2) Iterable objects & RANGE
(3) DICTIONARY
(4) Error handling system
'''

import array  # package/module
import math   # package
from math import ceil

print("===== What is object =====")
# An object has state and method properties.
# Everything is object in Python!

print(type('Hello World!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritance | Polimorphism

result1 = math.ceil(97.7)  # CALL
print("result1:", result1)

result2 = ceil(98.7)
print("result2:", result2)


print("===== Error handling system =====")
car_dict = dict(name="Tayota", year=2026, electric=True)

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)

# except (KeyError, AttributeError) as err:
# print("Errors:", err) // Bu bir qancha turdagi errorlarni bitta qatorda yozish uchun yani jamlash uchun

# except exception as err:
# print("General error:", err).   bu hamma turdagi errorlarni handle qilish uchun

except KeyError as err:
    print("No origin state property found:", err)

except AttributeError as err:
    print("No speed found:", err)

else:
    print("Executed successfully without errors")

finally:
    print("Final closing logic")
