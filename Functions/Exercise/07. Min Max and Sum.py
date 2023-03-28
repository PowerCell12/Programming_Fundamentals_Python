numbers = input()

list = numbers.split()
listfinal = []


def min_max_sum(numbers, list, listfinal):
    for i in range(0, len(list)):
        current_number = int(list[i])
        listfinal.append(current_number)

    minnumber  = min(listfinal)
    maxnumber = max(listfinal)
    sumnumber = sum(listfinal)
    print(f"The minimum number is {minnumber}")
    print(f"The maximum number is {maxnumber}")
    print(f"The sum number is: {sumnumber}")

min_max_sum(numbers, list, listfinal)
