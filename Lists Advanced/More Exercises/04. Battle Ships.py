ships = int(input())
list_final = []

for i in range(ships):

    rows = list(map(int, input().split(" ")))

    list_final.append(rows)

hits = input().split(" ")
destryoed = 0

for i in range(len(hits)):
    current = hits[i]
    
    current1= list(map(int, current.split("-")))

    if list_final[current1[0]][current1[1]] != 0 and int(list_final[current1[0]][current1[1]]) - 1 == 0:
        destryoed += 1
        list_final[current1[0]][current1[1]] = 0
    else:
        list_final[current1[0]][current1[1]] -= 1


print(destryoed)
