n = int(input())
boolean = False
all = 0


for i in range(1, n + 1):

    if i < 10:
        if  i == 5 or i == 7:
            boolean = True
        else:
            boolean = False

        print(f"{i} -> {boolean}")
    else:
        for j in range(0, len(str(i))):
            i1 = str(i)
            all += int(i1[j])

        if all == 5 or all == 7 or all == 11:
            boolean = True
        else:
            boolean = False
        
        print(f"{i} -> {boolean}")

    boolean = False
    all = 0
