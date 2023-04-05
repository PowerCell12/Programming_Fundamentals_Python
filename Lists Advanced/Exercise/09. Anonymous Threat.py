elements = input().split()

while True:
    command = input()
    if command == "3:1":
        break
    
    tokens = command.split()
    action = tokens[0]
    index = int(tokens[1])
    
    if action == "merge":
        end_index = int(tokens[2])
        merged = "".join(elements[max(index, 0):min(end_index+1, len(elements))])
        elements = elements[:max(index, 0)] + [merged] + elements[min(end_index+1, len(elements)):]
        
    elif action == "divide":
        partitions = int(tokens[2])
        element = elements[index]
        partition_size = len(element) // partitions
        extra_chars = len(element) % partitions
        result = []
        start = 0
        for i in range(partitions):
            if i < extra_chars:
                end = start + partition_size + 1
            else:
                end = start + partition_size
            result.append(element[start:end])
            start = end
        elements = elements[:index] + result + elements[index+1:]

print(" ".join(elements))
