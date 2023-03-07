string = input()
list = string.split()
list1 = []
listwith = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
listwith2 = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
counter = 0

for i in range(0, len(list)):
    current_number = list[i]
    if current_number in listwith:
        listwith.remove(current_number)
    if current_number in listwith2:
        listwith2.remove(current_number)

    finalA = len(listwith)
    finalB = len(listwith2)

    if finalA < 7 or finalB < 7:
        print(f"Team A - {finalA}; Team B - {finalB}")
        print("Game was terminated")
        break
    counter += 1

    if counter == len(list):
        print(f"Team A - {finalA}; Team B - {finalB}")
