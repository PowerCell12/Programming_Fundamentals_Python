days = int(input())
daily = int(input())
needed = float(input())
all = 0
counter = 0

for i in range(1, days + 1):
    all += daily
    counter += 1

    if i % 3 == 0:
        all += daily * 0.50

    if i % 5 ==0:
        all -= all * 0.30

    if all >= needed and counter == days:
        print(f'Ahoy! {all:.2f} plunder gained.')
        break

if all < needed:
    percentage = (float(all) / needed) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
