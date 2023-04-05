integers = list(map(int, input().split(" ")))
list_integers = []

while integers:
    commands = int(input())
    value = 0

    if commands < 0:
        value = integers[0]
        integers.pop(0)
        integers.insert(0, integers[len(integers) - 1])
    elif commands > len(integers) - 1:
        value = integers[-1]
        integers.pop()
        integers.insert(len(integers), integers[0])
    else:
        value = integers[commands]
        integers.pop(commands)


    for i in range(len(integers)):
        things = int(integers[i])
        if things <= value:
            integers[i] += value
        else:
            integers[i] -= value
        
    list_integers.append(value)

print(f"{sum(list_integers)}")
