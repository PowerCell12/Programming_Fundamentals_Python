number = int(input())
counter  = 1
list = []
all_of_of_them = 0


while True:
    formula = 2 * (counter ** 2)
    counter += 1

    if all_of_of_them + formula > number:
        final = number - all_of_of_them

    all_of_of_them += formula
    if all_of_of_them > number:
        list.append(final)

    if formula <= number and all_of_of_them <= number:
        list.append(formula)

    if all_of_of_them >= number:
        break


print(list)
