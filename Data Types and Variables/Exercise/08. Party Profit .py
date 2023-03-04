groupSize = int(input())
days = int(input())
all_money = 0
Everyday1 = 0

for i in range(1, days + 1):

    if i % 10 == 0:
        groupSize = groupSize - 2

    if i  % 15 == 0:
        groupSize = groupSize + 5


    forFood = 2 * groupSize
    Everyday = 50 - forFood

    Everyday1 = Everyday

    if i % 3 == 0:
        drinking = groupSize * 3
        Everyday1 = Everyday1 - drinking

    if i % 5 == 0:
        bossSlayer = 20 * groupSize
        Everyday1 = Everyday1 + bossSlayer

        if i % 3 == 0:
            Everyday1 -= 2 * groupSize 

    all_money += Everyday1
    

final = int(all_money / groupSize)

print(f"{groupSize} companions received {final} coins each.")
