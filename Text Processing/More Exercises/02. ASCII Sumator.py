first = ord(input())
second = ord(input())
strings = input()
total_sum = 0

for chrs in strings:
    
    final = ord(chrs)

    if first < final < second:
        total_sum += final

print(total_sum)
