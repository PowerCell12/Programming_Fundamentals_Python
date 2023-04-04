string = list(map(int, input().split(", ")))
counter = 10
counter1 = 0
list = []
counter2 = 0




while True:
    while True:
        if string[counter1] <= counter:
            list.append(string[counter1])
            string.remove(string[counter1])
            counter1 -= 1
        
        counter2 += 1
        counter1 += 1

        if counter1 == len(string):
            break

    print(f"Group of {counter}'s: {list}")
    list = []
    counter += 10
    counter1 = 0
    if not string:
        break
