strings = input()
encrypted1 = ""

for chr1 in strings:

  final = ord(chr1)
  final2 = final + 3
  final1 = chr(final2)

  encrypted1 += final1

print(encrypted1)
