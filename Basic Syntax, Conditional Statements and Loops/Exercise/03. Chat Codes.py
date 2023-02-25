number = int(input())

for i in range(number):
    codes = int(input())

    if codes == 88:
        print("Hello")

    if codes == 86:
        print("How are you?")

    if codes > 88:
        print("Bye.")

    if codes != 88 and  codes != 86 and codes < 88:
        print('GREAT!')
