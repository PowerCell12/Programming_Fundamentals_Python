numbers = input().split(", ")
list = [int(num) for num in numbers]
list2 = []

list1 =  [num if num >= 0 else list2.append(num) for num in list]

while True:
    if None in list1:
        list1.remove(None)
    else:
        break

list4 = []
list3 = [num1 if num1 % 2 == 0 else list4.append(num1) for num1 in list]

while True:
    if None in list3:
        list3.remove(None)
    else:
        break

list5 = ", ".join(map(str, list1))
list6 = ", ".join(map(str, list2))
list7 = ", ".join(map(str, list3))
list8 = ", ".join(map(str, list4))

print(f"Positive: {list5}")
print(f'Negative: {list6}')
print(f'Even: {list7}')
print(f'Odd: {list8}')
