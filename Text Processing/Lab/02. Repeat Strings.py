strings = input()

strings_list = strings.split(" ")
final_str = ""

for i in strings_list:

    repeated = len(i)

    final_str += i * repeated

print(final_str)
