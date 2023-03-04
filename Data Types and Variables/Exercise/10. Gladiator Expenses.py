lostFights = int(input())
counter = 0
helmet = float(input())
sword = float(input())
shiled = float(input())
armor = float(input())
counterhelmet = 0
countersword = 0
countershiled = 0
couteraromor = 0
list1 = []

for i in range(1, lostFights + 1):
    if i % 2 == 0:
        counterhelmet += 1

    if i % 3 == 0:
        countersword += 1

    if i % 2 == 0 and i % 3 == 0:
        counter += 1
        countershiled += 1


    if counter % 2 == 0 and counter != 0 and counter not in list1:
        couteraromor  += 1
        list1.append(counter)

final = helmet * counterhelmet + sword * countersword + shiled * countershiled + armor * couteraromor

print(f"Gladiator expenses: {final:.2f} aureus")
