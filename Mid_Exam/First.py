number = int(input())
allProfit = 0

for i in range(1, number  + 1):
    name = str(input())
    earned = float(input())
    expenses = float(input())
    expenses1 = expenses

    if i % 3 == 0:
        expenses = expenses + expenses * 0.50

    if i % 5 == 0:
        earned = earned - earned * 0.10

        if i % 3 == 0:
            expenses = expenses1

    final = earned - expenses
    allProfit += final

    print(f"In {name} Burger Bus earned {final:.2f} leva.")

print(f"Burger Bus total profit: {allProfit:.2f} leva.")
