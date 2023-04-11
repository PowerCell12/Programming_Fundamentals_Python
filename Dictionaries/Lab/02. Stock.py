food = input().split(" ")
bakery = {}
products = input().split(" ")

for i in range(0, len(food), 2):
    key = food[i]
    value = int(food[i + 1])
    bakery[key] = value

for i in range(len(products)):
    if products[i] in bakery.keys():
        quantity  = bakery.get(products[i])
        print(f"We have {quantity} of {products[i]} left")
    else:
        print(f"Sorry, we don't have {products[i]}")
