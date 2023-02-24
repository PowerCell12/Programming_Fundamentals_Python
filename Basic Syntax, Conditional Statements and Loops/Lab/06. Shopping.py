money = int(input())

while True:
    money_spent  = input()
    
    if money_spent == "End":
        print('You bought everything needed.')
        break

    money_spent =  int(money_spent)

    money -= money_spent
    
    if money < 0:
        print(f'You went in overdraft!')
        break
