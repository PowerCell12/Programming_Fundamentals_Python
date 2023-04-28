import re

strings = input()
to_find = input()

final1 = r"\b" + re.escape(to_find) + r"\b"
final = re.findall(final1, strings, re.IGNORECASE)

final3 = len(final)
print(final3)
