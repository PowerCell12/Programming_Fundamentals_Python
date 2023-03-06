number = int(input())
word = ""
list1 = []
lits2 = []
lits3 = []
lits4 = []
counter = 0

for i in range(1, number + 1):
    integrer = int(input())
    

    if integrer %  2 == 0 or integrer == 0:
        list1.append(integrer)

    if integrer % 2 != 0:
        lits2.append(integrer)

    if integrer < 0:
        lits3.append(integrer)

    if integrer >= 0:
        lits4.append(integrer)
     
    counter += 1  
    if counter == number:
        word = str(input())



if word == "even":
    print(list1)

if word == "odd":
    print(lits2)

if word == "negative":
    print(lits3)

if word == "positive":
    print(lits4)
