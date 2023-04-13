Country_Names = input().split(", ")
capital = input().split(", ")
final = zip(Country_Names, capital)

SortedIn = {key:value for key,value in final}

for key, value in SortedIn.items():
    print(f"{key} -> {value}")
