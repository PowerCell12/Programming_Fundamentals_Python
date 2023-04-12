elements = input().split(' ')
dict_elemets = {}


for i in range(0, len(elements)):
  current = elements[i].lower()


  if current not in dict_elemets:
    dict_elemets[current] = 1
  else:
    dict_elemets[current] += 1

all_words = []

for key, value in dict_elemets.items():
  if value % 2 != 0:
    all_words.append(key)

all_words_final = " ".join(all_words)
print(all_words_final)
