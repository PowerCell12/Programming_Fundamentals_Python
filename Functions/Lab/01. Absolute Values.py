numbers = input()
list1 = numbers.split()
list2 = []

def absolute(numbers, list1, list2):
    for i in range(0, len(list1)):
        current_number = float(list1[i])
        current_number = abs(current_number)
        list2.append(current_number)

    return list2

print(absolute(numbers, list1, list2))
