integer1 = int(input())
integer2 = int(input())
integer3 = int(input())


final = integer1 * integer2 * integer3

if final < 0:
    print("negative")

if final == 0:
    print("zero")

if final > 0:
    print("positive")
