tickets = input().split(",")
valid = False
winning = False
jackpot = False
symbols = ['@', '#', '$', '^']
counter1 = 0
counter = 0
match_symbol = ""
final_counter = 0
final_counter1 = 0


for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) == 20:
        valid = True
        half1 = int(len(ticket) / 2)
        half = ticket[:half1]
        other_half = ticket[half1:]

        for i in range(len(half)):
            chrs = half[i]
            if chrs in symbols:
                counter += 1
                match_symbol = chrs
            else:
                if i > 0:
                    if half[i - 1]  in symbols:
                        if counter < 6:
                            counter = 0
                        elif counter1 >= 6 and counter > final_counter:
                            final_counter = counter
                            counter = 0

        for j in range(len(other_half)):
            chrs1 = other_half[j]
            if chrs1 in symbols:
                counter1 += 1
            else:
                if j > 0:
                    if other_half[j - 1]  in symbols:
                        if counter1 < 6:
                            counter1 = 0
                        elif counter1 >= 6 and counter1 > final_counter1:
                            final_counter1 = counter1
                            counter1 = 0
                        

        if final_counter1 != 0:
            pass
        else:
            final_counter1 = counter1

        if final_counter != 0:
            pass
        else:
            final_counter = counter


        if final_counter1 >= 6 and final_counter >= 6:
            winning = True

        if final_counter1 >= 10 and final_counter >= 10:
            jackpot = True


        if final_counter < final_counter1:
            final_counter1 = final_counter
        elif final_counter > final_counter1:
            final_counter = final_counter1


    if jackpot:
        print(f'ticket "{ticket}" - {final_counter}{match_symbol} Jackpot!')
    elif winning:
        print(f'ticket "{ticket}" - {final_counter}{match_symbol}')
    elif valid:
        print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")

    jackpot =False
    winning = False
    valid = False
    counter = 0 
    counter1 = 0
    final_counter1 = 0
    final_counter = 0
