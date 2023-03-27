number1 = int(input())
number2 = int(input())
number3  = int(input())
biggest = 0

def smallest(number1, number2, number3, biggest):
    if number1 < number2 and number1 < number3:
        biggest = number1
    elif number2 < number1 and number2 < number3:
        biggest = number2
    elif number3 < number1 and number3 < number2:
        biggest = number3
    return biggest

print(smallest(number1, number2, number3, biggest))
