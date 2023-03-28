numbers = input()
list = numbers.split(", ")

def palindromeint(numbers, list):
    for i in range(0, len(list)):
        current_number = (list[i])
        if current_number == current_number[::-1]:
            print("True")
        else:
            print("False")

palindromeint(numbers, list)
