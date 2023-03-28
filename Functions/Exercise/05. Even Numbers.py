numbers = input()
list  = numbers.split()
listfinal = []

for i in range(0, len(list)):
    current_number = int(list[i])
    if current_number % 2 == 0:
        listfinal.append(current_number)

print(listfinal)
