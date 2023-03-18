train_ticket = 150
markup = 0.4

type_price = input().split("|")

budget = float(input())
list_bought = []

for i in range(len(type_price)):
    current = type_price[i]


    current = current.split("->")


    if current[0] == "Clothes" and float(current[1]) > 50.00:
        continue
    elif current[0] == 'Shoes' and float(current[1]) > 35.00:
        continue
    elif current[0] == 'Accessories' and float(current[1]) > 20.50:
        continue

    if budget >= float(current[1]):
        budget = budget - float(current[1])
        list_bought.append(float(current[1]))

profit  = 0

for j in range(len(list_bought)):
    current1 = list_bought[j]


    profit += current1 * 0.4

    list_bought[j] = list_bought[j] + list_bought[j] * 0.4

left_budget = budget + sum(list_bought)


for k in range(len(list_bought)):
    chrss = list_bought[k]
    
    if k < len(list_bought) - 1:    
        print(f"{chrss:.2f}", end=" ")
    else:
        print(f"{chrss:.2f}")

print(f"Profit: {profit:.2f}")

if left_budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
