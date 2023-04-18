strings =  input()
new_string  = ""
numbers = ""
a_bit = ""


for i in range(len(strings)):
    chrs = strings[i]
    if chrs.isdigit():
        numbers += chrs

        if i + 1 < len(strings):
            if strings[i + 1].isdigit():
                pass
            else:
                final  = int(numbers)  * a_bit
                new_string += final.upper()
                a_bit = ""
        elif i == len(strings) - 1:
            final  = int(numbers)  * a_bit
            new_string += final.upper()
            a_bit = ""  

    else:
        numbers = ""
        a_bit += chrs

final1 = set(new_string)
final1 = len(final1)

print(f"Unique symbols used: {final1}")
print(new_string)
