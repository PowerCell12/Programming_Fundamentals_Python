import re
list_furniture = []
total = 0

while True:
  commands = input()

  if commands == "Purchase":
    break

  regex1 = r">>([a-zA-Z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)"
  final1 = re.findall(regex1, commands)


  if final1:
    list_furniture.append(final1[0][0])

    final_money = float(final1[0][1]) * float(final1[0][3])

    total += final_money


print("Bought furniture:")
for items in list_furniture:
  print(f"{items}", end="\n")
print(f"Total money spend: {total:.2f}")
