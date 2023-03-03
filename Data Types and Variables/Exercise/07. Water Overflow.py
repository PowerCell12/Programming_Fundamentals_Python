lines = int(input())
litters = 255
all = 0

for i in range(1, lines + 1):
    toFull = int(input())

    if litters - toFull >= 0:
        litters = litters - toFull
        all += toFull
    else:
        print("Insufficient capacity!")

    
print(all)
