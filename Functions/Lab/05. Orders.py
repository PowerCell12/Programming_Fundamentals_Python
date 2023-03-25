product = input()
quantity = int(input())
price = 0


def orders(product, quantity):
    if product == "coffee":
        price = 1.50
    elif product == "coke":
        price = 1.40
    elif product == "water":
        price = 1
    elif product == "snacks": 
        price = 2
    
    final  = price * quantity
    final = (f"{final:.2f}")
    return final

print(orders(product, quantity))
