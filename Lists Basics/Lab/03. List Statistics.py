number = int(input())
list1 = []
list2 = []

for i in range(number):
    number1 = int(input())

    if number1 <= 0:
        list1.append(number1)
    else:
        list2.append(number1)

    
final1 = len(list2)
final2 = sum(list1)
print(list2)
print(list1)
print(f"Count of positives: {final1}")
print(f"Sum of negatives: {final2}")
