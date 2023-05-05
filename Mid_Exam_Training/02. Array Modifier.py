integers = list(map(int, input().split()))
list1 = []

## check the swap insert option if it still on 80/100


while True:
    whattodo = list(input().split())

    if whattodo[0] == "end":
        break


    if whattodo[0] == "swap":
        if int(whattodo[1]) < int(whattodo[2]):
            second = integers.pop(int(whattodo[2]))
            first = integers.pop(int(whattodo[1]))


            integers.insert(int(whattodo[1]), second)
            integers.insert(int(whattodo[2]), first)
        else:
            first = integers.pop(int(whattodo[1]))
            second = integers.pop(int(whattodo[2]))

            integers.insert(int(whattodo[2]), first)
            integers.insert(int(whattodo[1]), second)


    if whattodo[0] == "decrease":
        for i in range(0, len(integers)):
            integers[i] = integers[i] - 1
        
    
    if whattodo[0] == "multiply":
        if int(whattodo[1]) < int(whattodo[2]):
            second = integers.pop(int(whattodo[2]))
            first = integers.pop(int(whattodo[1]))

            final = first * second
            position = int(whattodo[1])
            position1 = int(whattodo[2])
            integers.insert(position, final)
            integers.insert(position1, second)

        else:
            first = integers.pop(int(whattodo[1]))
            second = integers.pop(int(whattodo[2]))

            
            final = first * second
            position = int(whattodo[1])
            position1 = int(whattodo[2])
            integers.insert(position1, second)
            integers.insert(position, final)


for i in range(0, len(integers)):
    current = integers[i]
    string = '-' + str(abs(current)) if current < 0 else str(current)
    list1.append(string)


final1 = ", ".join(list1)



print(final1)
