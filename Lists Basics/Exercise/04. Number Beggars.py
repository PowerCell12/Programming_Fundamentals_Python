list_of_money = input().split(", ")
number_of_beggars = int(input())

list_of_beggars = []

for i in range(0, number_of_beggars):
    list_of_beggars.append(0)
    
for i in range(0, len(list_of_money)):
    current_money = int(list_of_money[i])
    
    while i >= len(list_of_beggars):
        i -= len(list_of_beggars)
    index_of_current_beggar = i
    list_of_beggars[index_of_current_beggar] += current_money

print(list_of_beggars)
