num1 = int(input())
num2 = int(input())
num3 = int(input())
sum_of_two = 0

def sum_numbers(num1, num2, sum_of_two):
    sum_of_two = num1 + num2
    return sum_of_two

def subtract(sum_of_two):
    return sum_numbers(num1, num2, sum_of_two) - num3

print(subtract(sum_of_two))
