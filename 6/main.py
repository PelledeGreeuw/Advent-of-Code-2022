with open('input') as file:
    for line in file.readlines():
        buffer = []
        for i, char in enumerate(line):
            buffer.append(char)
            if len(buffer) > 14:
                buffer.pop(0)
            if len(set(buffer)) == 14:
                print(i + 1)
                exit(0)
