import time


def show(ps):
    for l in ps:
        print(''.join([p[0] if p[1] == -1 else str('#') for p in l]))


with open('input') as file:
    points = []
    start, end = [0, 0], [0, 0]
    for line in file.readlines():
        row = []
        for c in line:
            if c == '\n':
                pass
            elif c == 'S':
                start = (len(points), len(row))
                row.append(['a', -1])
            elif c == 'E':
                end = (len(points), len(row))
                row.append(['z', 0])
            else:
                row.append([c, -1])

        points.append(row)

    edge = {end}
    while len(edge) > 0:
        n_edge = set()
        for x1, y1 in edge:
            c1, n1 = points[x1][y1]
            if c1 == 'a':
                print(c1, n1)
            for x2, y2 in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]:
                if x2 < 0 or x2 >= len(points) or y2 < 0 or y2 >= len(points[x2]):
                    continue
                c2, n2 = points[x2][y2]
                # print(c2, n2, x2, y2)
                if n2 == -1:
                    dif = ord(c2) - ord(c1)
                    if dif >= -1:
                        points[x2][y2][1] = n1 + 1
                        n_edge.add((x2, y2))
        edge = n_edge

    print(points[end[0]][end[1]])
