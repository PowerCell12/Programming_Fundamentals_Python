import re
lines = int(input())
valid_ones = []
digits = ""

for i in range(lines):
  barcode = input()

  regex1 = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
  final1 = re.findall(regex1, barcode)

  if not final1:
    print("Invalid barcode")
    continue

  for chrs in final1[0]:
    if chrs.isdigit():
      digits += chrs

  if digits != "":
    print(f"Product group: {digits}")
  else:
    print("Product group: 00")

  digits = ""
