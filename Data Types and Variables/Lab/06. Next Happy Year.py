yearStarting = input()
yearStarting = int(yearStarting)  + 1
yearStarting = str(yearStarting)
counter = 0
special = 0
boolean = False
counter = 0

while True:
    for i in range(0, len(yearStarting)):
        for j in range(i + 1, len(yearStarting)):
        ## check if the year is happy 
            if yearStarting[i] == yearStarting[j]:
                boolean = False
                break
            else:
                boolean = True
        
        if boolean == False:
            break
        else:
            counter += 1

        if counter == len(yearStarting):
            print(yearStarting)
            quit()

    yearStarting1 = int(yearStarting)
    yearStarting1 += 1
    yearStarting = yearStarting1
    yearStarting = str(yearStarting)
    counter = 0
