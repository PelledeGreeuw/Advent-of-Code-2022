import re

with open('input') as file:
    cycles = [1]
    x = 1
    pattern = re.compile(r'addx (?P<amount>-?\d+)')
    for line in file.readlines():
        if line.startswith('noop'):
            cycles.append(x)
        else:
            m = re.search(pattern, line)
            cycles.append(x)
            x += int(m.group('amount'))
            cycles.append(x)
    print(sum([cycles[x - 1] * x for x in [20, 60, 100, 140, 180, 220]]))
    for i in range(6):
        s = ''
        for j in range(40):
            if cycles[i*40 + j] in [j-1, j, j+ 1]:
                s += '#'
            else:
                s += '.'
        print(s)

