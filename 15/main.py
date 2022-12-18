import re

with open('input') as file:
    pattern = re.compile(
        r'Sensor at x=(?P<s_x>-?\d+), y=(?P<s_y>-?\d+): closest beacon is at x=(?P<b_x>-?\d+), y=(?P<b_y>-?\d+)')
    sensors = []
    beacons = set()
    for match in re.finditer(pattern, file.read()):
        sens = {
            "x": int(match.group('s_x')),
            "y": int(match.group('s_y')),
            "bx": int(match.group('b_x')),
            "by": int(match.group('b_y')),
        }
        dif = [sens['bx'] - sens['x'], sens['by'] - sens['y']]
        sens['radius'] = abs(dif[0]) + abs(dif[1])
        sensors.append(sens)
        beacons.add((sens['bx'], sens['by']))
    t = 2000000
    max_x = max([x['bx'] for x in sensors] + [x['x'] for x in sensors])
    min_x = min([x['bx'] for x in sensors] + [x['x'] for x in sensors])


    def get_blocked(target):
        blocked = []
        for sensor in sensors:
            if sensor['y'] > target >= sensor['y'] - sensor['radius']:
                diff = sensor['y'] - target
                blocked.append([sensor['x'] - sensor['radius'] + diff, sensor['x'] + sensor['radius'] - diff])
            elif sensor['y'] < target <= sensor['y'] + sensor['radius']:
                diff = target - sensor['y']
                blocked.append([sensor['x'] - sensor['radius'] + diff, sensor['x'] + sensor['radius'] - diff])
            elif sensor['y'] == target:
                blocked.append([sensor['x'] - sensor['radius'], sensor['x'] + sensor['radius']])
        return blocked


    blcked = get_blocked(t)
    blcked.sort(key=lambda x: x[0])
    disjoint = []
    last = blcked[0]
    for x, x2 in blcked[1:]:
        if x > last[1]:
            disjoint.append(last)
            last = [x, x2]
        elif x2 > last[1]:
            last[1] = x2
    if last:
        disjoint.append(last)
    total = 0
    for x1, x2 in disjoint:
        total += x2 - x1 + 1
    for bx, by in beacons:
        if by == t:
            for x1, x2 in disjoint:
                if x1 <= bx <= x2:
                    total -= 1
    print(total)
    max_size = 4000000
    min_x = 0
    max_x = max_size


    def app(l, elem):
        if elem[0] > max_x:
            return
        elif elem[1] >= max_x:
            elem[1] = max_x
            l.append(elem)

        if elem[0] < min_x and elem[1] < min_x:
            return
        elif elem[0] < min_x:
            elem[0] = min_x
            l.append(elem)


    for i in range(max_size):
        blcked = get_blocked(i)
        blcked.sort(key=lambda x: x[0])
        disjoint = []
        last = blcked[0]
        for x, x2 in blcked[1:]:
            if x > last[1]:
                app(disjoint, last)
                last = [x, x2]
            elif x2 > last[1]:
                last[1] = x2

        app(disjoint, last)
        if disjoint[0][0] != 0 or disjoint[0][1] != max_x:
            x = 0
            if len(disjoint) == 1 and disjoint[0][1] != max_x:
                x = max_x
            elif len(disjoint) == 2:
                x = disjoint[0][1] + 1
            print(x * max_x + i)
            print(blcked)
            print(disjoint)
            break
