numbers = input()
list2 = numbers.split()
list1 = []


def rounding(numbers, list2, list1):
    for i in range(0, len(list2)):
        current_number = int(round(float(list2[i])))
        list1.append(current_number)
    return list1

print(rounding(numbers, list2, list1))
