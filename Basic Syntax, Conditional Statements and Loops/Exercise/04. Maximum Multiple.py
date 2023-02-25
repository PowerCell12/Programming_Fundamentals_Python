divisor = int(input())
positivenumber = int(input())

for i in range(positivenumber, 1, -1):

    if i % divisor == 0 and i > 0:
        print(i)
        break
