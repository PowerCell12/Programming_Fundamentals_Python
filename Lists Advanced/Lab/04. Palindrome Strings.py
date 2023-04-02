words = input()
palidrome = input()
list1 = []
list2 = []
current_number2 = ''
index = -1
list1 = words.split()

for i in range(0, len(list1)):
    current_number = list1[i]
    for y in range(1, len(current_number) + 1):
        current_number2 += current_number[index]
        index += -1
    if current_number == current_number2:
        list2.append(current_number)
    current_number2 = ""
    index = -1

counter = 0
for i in range(0, len(list2)):
    if palidrome in list2[i]:
        counter += 1

print(list2)
print(f"Found palindrome {counter} times")
