number1 = int(input())
number2 = int(input())

print(f"Before:")
print(f"a = {number1}")
print(f"b = {number2}")

temp = number1

number1 = number2
number2 = temp

print(f"After:")
print(f"a = {number1}")
print(f"b = {number2}")
