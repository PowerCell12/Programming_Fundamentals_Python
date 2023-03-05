number =   int(input())
numberintwo = number / 2
flag = " "

for i in range(1, number):
    for t in range(1, number):
        if number == i * t:
            flag = "False"
            print("False")
            quit()
        else:
            flag = "True"

print(flag)
