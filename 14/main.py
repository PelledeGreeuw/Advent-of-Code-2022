import re

with open('input') as file:
    tuple_pattern = re.compile('(?P<x>\d+),(?P<y>\d+)')
    size_x, size_y = 0, 0
    min_x, min_y = 1000, 1000
    for m in re.finditer(tuple_pattern, file.read()):
        tx, ty = int(m.group('x')), int(m.group('y'))
        size_x = max(tx, size_x)
        size_y = max(ty, size_y)
        min_x, min_y = min(min_x, tx), min(min_y, ty)
    size_x += 200
    grid = [[False for i in range(size_x + 1)] for j in range(size_y + 2)]
    grid.append([True for i in range(size_x + 1)])
    file.seek(0)
    for line in file.readlines():
        current = None
        for point in re.finditer(tuple_pattern, line):
            tx, ty = int(point.group('x')), int(point.group('y'))
            if current is None:
                current = (tx, ty)
                grid[current[1]][current[0]] = True
            else:
                diff = (tx - current[0], ty - current[1])
                step = ((diff[0] // abs(diff[0])) if diff[0] != 0 else 0, (diff[1] // abs(diff[1])) if diff[1] != 0 else 0)
                steps = max(abs(diff[0]), abs(diff[1]))
                for i in range(steps):
                    current = (current[0] + step[0], current[1] + step[1])
                    grid[current[1]][current[0]] = True
                if current != (tx, ty):
                    print("RIP", current, (tx, ty))
    sand = [500, 0]
    c = 0
    while (1):
        try:
            if not grid[sand[1]+1][sand[0]]:
                sand[1] += 1
            elif not grid[sand[1]+1][sand[0]-1]:
                sand[0] -= 1
                sand[1] += 1
            elif not grid[sand[1] + 1][sand[0] + 1]:
                sand[0] += 1
                sand[1] += 1
            else:
                grid[sand[1]][sand[0]] = True
                c += 1
                if sand == [500, 0]:
                    break
                sand = [500, 0]
        except IndexError:
            break

    print(c)
    for line in grid:
        print(''.join(['#' if x else '.' for x in line]))


