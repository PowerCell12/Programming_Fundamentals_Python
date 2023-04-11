staticks_dict = {}

while True:
    food = input()

    if food == "statistics":
        break

    food = food.split(": ")
    

    if food[0] not in staticks_dict:
        staticks_dict[food[0]] = int(food[1])
    else:
        staticks_dict[food[0]]  = staticks_dict[food[0]] + int(food[1])


print(f'Products in stock:')
for key, value in staticks_dict.items():
    print(f"- {key}: {value}")

total = len(staticks_dict)    
print(f"Total Products: {total}")
quantity = sum(staticks_dict.values())
print(f"Total Quantity: {quantity}")
