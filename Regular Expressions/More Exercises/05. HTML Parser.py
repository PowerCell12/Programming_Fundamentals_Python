html = input()

import re

regex1 = r"<title>.*</title>"
final1 = re.findall(regex1, html)

final2 = final1[0][7:-8]


regex5  = r"<[^>]+>"
final7 = re.findall(regex5, final2)

for k in range(len(final7)):
    current2 = final7[k]
    final2 = final2.replace(current2, "", 1)


regex6 = r"\\n"
final8 = re.findall(regex6, final2)

for w in range(len(final8)):
    current4 = final8[w]
    final2 = final2.replace(current4, "", 1)

print(f"Title: {final2}")

## ----------------------------------------

regex2 = r"<body>.*</body>"
final3 = re.findall(regex2, html)

final4 =  final3[0][6:-7]

regex3 = r"<[^>]+>"
final5 = re.findall(regex3, final4)


for i in range(len(final5)):
    current  = final5[i]
    final4 = final4.replace(current, "", 1)

regex4 = r"\\n"
final6 = re.findall(regex4, final4)

for j in range(len(final6)):
    current1 = final6[j]
    final4 = final4.replace(current1, "", 1)

print(f"Content: {final4}")
