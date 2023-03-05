lines = int(input())
counter1 = 0
counter2 = 0

for i in range(0, lines):
    strings  = str(input())

    if strings == '(':
        counter1 += 1
    elif strings == ')':
        counter2 += 1


if counter1 == counter2:
    print("BALANCED")
else:
    print("UNBALANCED")
    
## 75/100
