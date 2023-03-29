number1 = int(input())
number2 =  int(input())
random = 2
final = 1

for i in range(random, number1 + 1):
    final = final * i

final1 = 1

for j in range(random, number2 + 1):
    final1 = final1 * j


final2 = final  / final1

print(f"{final2:.2f}")
