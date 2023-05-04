import re
total = 0

while True:
    name_money = input()

    if name_money == "end of shift":
        break

    regex1 = r"%([A-Z][a-z]+)%[^|$%.]*<([\w]+)>[^|$%.]*\|([0-9]+)\|[^|$%.0-9]*(-?\d+(\.\d+)?)\$"
    final1 = re.findall(regex1, name_money)
    if final1:
        final = float(final1[0][2]) * float(final1[0][3])
        total += final

    if final1:
        print(f"{final1[0][0]}: {final1[0][1]} - {final:.2f}")  

print(f"Total income: {total:.2f}")
