efficiency1 = int(input())
efficiency2 = int(input())
efficiency3 = int(input())
count = int(input())

allpeoplehour = efficiency1 + efficiency2 + efficiency3


peopleleft = count
counter = 0
hours = 0


for i in range(1, count + 1):
    counter += 1
    peopleleft -= allpeoplehour
    if peopleleft < 1:
        break
    
    if i % 3 == 0:
        counter += 1

    

print(f"Time needed: {counter}h.")
