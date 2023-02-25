number = int(input())

for i in range(1, number + 1):
    string1 = str(input())

    if "," in string1 or '.' in string1 or "_" in string1:
        print(f"{string1} is not pure!")
        continue
    
    print(f"{string1} is pure.")
