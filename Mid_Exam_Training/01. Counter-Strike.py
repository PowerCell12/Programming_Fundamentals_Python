initial = int(input())
count = 0

while True:
    distance = input()

    if distance == "End of battle":
        print(f"Won battles: {count}. Energy left: {initial}" )
        break

    distance = int(distance)


    if initial - distance < 0:
        print(f"Not enough energy! Game ends with {count} won battles and {initial} energy")
        break        

    initial = initial - distance

    count += 1

    if count % 3 == 0:
        initial = initial + count
