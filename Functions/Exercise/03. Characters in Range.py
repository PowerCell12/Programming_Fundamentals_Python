chr1 = str(input())
chr2 = str(input())
list = []
chr1 = ord(chr1)
chr2 = ord(chr2)


def chinrange(chr1,chr2,list,):
    while True:
        chr1 += 1
        if chr1 == chr2:
         break
        chr1 = chr(chr1)
        chr2 = chr(chr2)

        list.append(chr1)

        chr1 = ord(chr1)
        chr2 = ord(chr2)
    print(' '.join(list))


chinrange(chr1, chr2, list)
