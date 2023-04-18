strigs = input()

for i in range(0, len(strigs)):
  chrs = strigs[i]
  
  if chrs == ":":
    final = strigs[i + 1]
    print(f"{chrs}{final}", end="\n")
