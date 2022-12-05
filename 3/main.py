def point(val):
    v = ord(val)
    if v < 91:
        return v - 64 + 26
    return v - 96

with open('input') as file:
    total = 0
    c = 0
    common = ''
    for line in file.readlines():
        line = line.replace('\n', '')
        if c == 0:
            common = set(line)
        else:
            common = common.intersection(set(line))
        c += 1
        if c == 3:
            total += point(list(common)[0])
            c = 0
    print(total)
    
