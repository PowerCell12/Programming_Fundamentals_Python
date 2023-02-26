quantity = int(input())
daysLeft = int(input())
all_money = 0
all_points = 0


for i in range(1, daysLeft + 1):

    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        all_money += 2 * quantity
        all_points += 5

    if i % 3 == 0:
        all_money += 8 * quantity
        all_points += 13
    
    if i % 5  == 0:
        all_money += 15 * quantity
        all_points += 17

        if i % 3 == 0:
            all_points += 30

    if i % 10 == 0:
        all_points -= 20
        all_money += 23

if daysLeft % 10 == 0:
    all_points = all_points - 30

print(f"Total cost: {all_money}")
print(f"Total spirit: {all_points}")
