numbers = input()

list = numbers.split()

list_final = []

for i in range(0, len(list)):
    current_number = int(list[i])
    list_final.append(current_number)

final = sorted(list_final)

print(final)
