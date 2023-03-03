number = int(input())
final = ""
final1 = 0

for i in range(number):
    letter = input()
    final = ord(letter)
    final1 += final

print(f"The sum equals: {final1}")
