numbers = input().split()
numbers = [int(num) for num in numbers]

command = input().split()
while command[0] != "end":
    if command[0] == "exchange":
        index = int(command[1])
        if index < 0 or index >= len(numbers):
            print("Invalid index")
        else:
            numbers = numbers[index+1:] + numbers[:index+1]
    elif command[0] == "max" or command[0] == "min":
        even_odd = command[1]
        filtered_nums = [num for num in numbers if num % 2 == (0 if even_odd == "even" else 1)]
        if len(filtered_nums) == 0:
            print("No matches")
        else:
            if command[0] == "max":
                index = len(numbers) - 1 - numbers[::-1].index(max(filtered_nums))
            else:
                index = len(numbers) - 1 - numbers[::-1].index(min(filtered_nums))
            print(index)
    elif command[0] == "first" or command[0] == "last":
        count = int(command[1])
        even_odd = command[2]
        filtered_nums = [num for num in numbers if num % 2 == (0 if even_odd == "even" else 1)]
        if count > len(numbers):
            print("Invalid count")
        else:
            if command[0] == "first":
                print(filtered_nums[:count])
            else:
                print(filtered_nums[-count:])
    command = input().split()

print(numbers)
