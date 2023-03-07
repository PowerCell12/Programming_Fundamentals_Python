numbers_string = str(input())
numbers_string_list = numbers_string.split()
printlist = []

for i in range(0, len(numbers_string_list)):
    current_number = int(numbers_string_list[i])
    if current_number > 0:
        current_number *= -1
    elif current_number < 0:
        current_number *= -1
    printlist.append(current_number)

print(printlist)
