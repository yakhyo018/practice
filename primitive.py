print("=====number====")
# in JVA, variable is a name storage location!
# in Python, variable is named reference!

count = 100
count_type = type(count)
print("count:", count, count_type)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("==== string ====")

course = "AI Python FullStack"
result = type(course)
print(f"the type of course: {result}")
result = course.title()
print(f"the result: {result} ")

result = course.upper()
print(f"the result: {result} ")

result = course.replace("FullStack", "MAsterClass")
print(f"the result (4): {result} ")

print("==== boolean ====")

# function > type() input() bool() int() str()
y = input("give your value for y:")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")

# TRUTHY vs FALSY value
# TRUTHY: True 100 -100 "MIT"
# FALSY:  False 0 "" None

test_falsy = "" or False or None or 0
print("the FALSY:", bool(test_falsy))

test_truthy = 100
print("the TRUTHY:", bool(test_truthy))
