import re

with open('input') as file:
    pattern = re.compile('(?P<x>\d+),(?P<y>\d+),(?P<z>\d+)')
    points = []
    for m in re.finditer(pattern, file.read()):
        points.append((int(m.group('x')), int(m.group('y')), int(m.group('z'))))
    sx = max([x[0] for x in points]) + 1
    sy = max([x[1] for x in points]) + 1
    sz = max([x[2] for x in points]) + 1
    grid = [
        [[2 if x == 0 or i == 0 or j == 0 or x == sx - 1 or j == sy - 1 or i == sz - 1 else 0 for x in range(sx)] for j
         in range(sy)] for i in range(sz)]
    for point in points:
        grid[point[2]][point[1]][point[0]] = 1
    # for plane in grid:
    #     for row in plane:
    #         print(row)
    #     print("")
    edge = []
    for i, plane in enumerate(grid):
        for j, row in enumerate(plane):
            for k, point in enumerate(row):
                if point == 2:
                    edge.append((k, j, i))

    while len(edge) != 0:
        n_edge = []
        for x, y, z in edge:
            for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                try:
                    if grid[z + dz][y + dy][x + dx] == 0:
                        grid[z + dz][y + dy][x + dx] = 2
                        n_edge.append([x + dx, y + dy, z + dz])
                except IndexError:
                    pass

        edge = n_edge

    for i, plane in enumerate(grid):
        for j, row in enumerate(plane):
            for k, point in enumerate(row):
                if point == 0:
                    grid[i][j][k] = 1
    for i, plane in enumerate(grid):
        for j, row in enumerate(plane):
            for k, point in enumerate(row):
                if point == 2:
                    grid[i][j][k] = 0
    sides = 0
    for i, plane in enumerate(grid):
        for j, row in enumerate(plane):
            for k, point in enumerate(row):
                if k + 1 < sx and row[k + 1] != point:
                    sides += 1
                if (k + 1 == sx or k == 0) and point == 1:
                    sides += 1

                if j + 1 < sy and plane[j + 1][k] != point:
                    sides += 1
                if (j + 1 == sy or j == 0) and point == 1:
                    sides += 1

                if i + 1 < sz and grid[i + 1][j][k] != point:
                    sides += 1
                if (i + 1 == sz or i == 0) and point == 1:
                    sides += 1

    print(sides)
