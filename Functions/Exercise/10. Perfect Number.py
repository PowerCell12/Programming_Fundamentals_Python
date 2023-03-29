number = int(input())
final = 0

def perfectnum(number, final):
    for i in range(1, number + 1):
        if i == number:
            continue
        if number % i == 0:
            final += i

    if final == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")

perfectnum(number, final)
