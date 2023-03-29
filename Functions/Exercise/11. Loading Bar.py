number = int(input())
list1 = []
divise = 10

for i in range(0, 10):
    list1.append(".")


for i in range(0, 11):
    if number / divise >= 1:
        list1.remove(".")
        list1.insert(0, "%")
        divise += 10
    else:
        break

final_list = "".join(list1)

if number == 100:
    print("100% Complete!")
    print("[%%%%%%%%%%]")
elif number == 0:
    print("0% [..........]")
    print("Still loading...")
else:
    print(f"{number}% [{final_list}]")
    print("Still loading...")
