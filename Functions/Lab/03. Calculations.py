whatdoto = input()
number1 = int(input())
number2 = int(input())

def calculation(number1, number2, whatdoto):
    final = 0
    if whatdoto == "multiply":
      final = number1 * number2
    elif whatdoto == "divide":
        final = number1 / number2
        final = int(final)
    elif whatdoto == "add":
        final = number1 + number2   
    elif whatdoto == "subtract":
        final =  number1 - number2
        
    return final

print(calculation(number1, number2, whatdoto))
