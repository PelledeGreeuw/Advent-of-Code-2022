with open('input') as file:
    elves = []
    current = 0
    for line in file.readlines():
        if line == '\n':
            elves.append(current)
            current = 0
        else:
            current += int(line.replace('\n', ''))
    elves = sorted(elves)
    print(elves[len(elves)-3:])
    print(sum(elves[len(elves)-3:]))
    
