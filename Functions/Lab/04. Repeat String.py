string = input()
counter = int((input()))

def repeat(string, counter):
    for i in range(counter):
        print(string, end='')
        
repeat(string, counter)
