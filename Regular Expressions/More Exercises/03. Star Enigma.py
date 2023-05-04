lines = int(input())
import re
length = 0
new_string = ""
attacked_counter = 0
desetroyed_counter = 0
attacket_list = []
destroyed_list = []

for i in range(lines):
    messages = input()

    regex1 = r"[starSTAR]+"
    final1 = re.findall(regex1, messages)
    
    for matches in final1:
        for length1 in matches:
            length += 1


    for message in messages:
        final_message = ord(message) - length
        new_string += chr(final_message)


    regex2 = r"@([A-Za-z]+)[^@\-!:\>]*:([0-9]+)[^\-!:\>]*!([AD])![^\-!:\>]*->([0-9]+)"
    final2 = re.findall(regex2, new_string)

    if not final2:
        length = 0
        new_string = ""
        continue

    if final2[0][2] == "D":
        desetroyed_counter += 1
        destroyed_list.append(final2[0][0])
    else:
        attacked_counter += 1
        attacket_list.append(final2[0][0])


    new_string = ""
    length = 0

attacket_list = sorted(attacket_list)
destroyed_list = sorted(destroyed_list)


print(f"Attacked planets: {attacked_counter}")
for attack in attacket_list:
    print(f"-> {attack}")
print(f"Destroyed planets: {desetroyed_counter}")
for destroyed in destroyed_list:
    print(f"-> {destroyed}")
