import re
pattern = re.compile('move (?P<amount>\d+) from (?P<origin>\d) to (?P<dest>\d)')
with open('input') as file:
    state = []
    for i in range(9):
        state.append([])
    loaded = False
    for line in file.readlines():
        if not loaded:
            if line.startswith(' 1 '):
                loaded = True
                continue
            for i in range(9):
                crate = line[4*i + 1]
                if crate != ' ':
                    state[i].append(crate)
        m = re.search(pattern, line)
        if m is not None:
            for i in range(int(m.group('amount'))):
                state[int(m.group('dest'))-1].insert(i, state[int(m.group('origin'))-1].pop(0))
    
    print(''.join([x[0] for x in state]))
