budget = float(input())
flour1 = float(input())
eggs1 = flour1 - flour1 * 0.25
milk1 = flour1 + flour1 * 0.25
##use only 250 m for bread
counter = 0
colored = 0

while True:

    money_forOne = flour1 + eggs1 + milk1 * (1 / 4)

    if budget - money_forOne < 0:
        print(f"You made {counter} loaves of Easter bread! Now you have {colored} eggs and {budget:.2f}BGN left.")
        break

    budget = budget - money_forOne

    counter += 1

    colored += 3 

    if counter % 3 == 0:
        toLoss = counter - 2
        colored = colored - toLoss
