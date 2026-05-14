print("====== for loop ======")
# Iterable objects > string dict tuple list range map filter
text = "MIT"
number = [3, 2, 3, 4]
car_object = dict(brand="ferrari", year=2025)
range_object = range(5)

for latter in text:
    print(f"the latter: {latter}")

print("--------")

for num in number:
    print(f"The number: {num}")

print("--------")
for key in car_object:
    print(f"the key: {key} => value: {car_object.get(key)}")

print("====== break/else ======")

for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10:
        print("reached break")
        break
else:
    print("executed successfully")

print("====== while operator ======")

num = 40
while num > 0:
    num -= 10
    print(F"the num equal: {num}")

print("--------")

count = 0
while True:
    count += 1
    x = int(input("find number:"))

    if x == 42:
        print(f"you found number in {count} steps!")
        break
    else:
        print("Wrong, please try again!")
