number_ofOrders = int(input())
all = 0

for i in range(1, number_ofOrders + 1):
    price = float(input())
    days = int(input())
    capsulesNeeded = int(input())

    if price < 0.01 or price > 100.00:
        continue

    if days < 1 or days > 31:
        continue

    if capsulesNeeded < 1 or capsulesNeeded > 2000:
        continue

    total_price = price * days * capsulesNeeded
    all += total_price

    print(f"The price for the coffee is: ${total_price:.2f}")

print(f"Total: ${all:.2f}")
