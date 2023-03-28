number = input()
list = []
odd = 0
even = 0

def oddandeven(number, list, odd, even):
      for i in range(0, len(number)):
            current_number = int(number[i])
            list.append(current_number)

      for i in range(0, len(list)):
            current_number = (list[i])
            if current_number % 2 == 0:
                  even += current_number
            else:
                  odd += current_number
      print(f"Odd sum = {odd}, Even sum = {even}")

      
oddandeven(number, list, odd, even)
