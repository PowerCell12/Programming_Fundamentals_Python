string = list(map(int, input().split(", ")))


found  = map(lambda x: x if string[x] % 2 == 0 else "no", range(0, len(string)))

index =  list(filter(lambda a: a != "no", found))

print(index)
