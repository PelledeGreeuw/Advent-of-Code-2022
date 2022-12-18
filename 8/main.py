with open('input') as file:
    grid = []
    visible = 0
    for line in file.readlines():
        row = []
        line = line.replace('\n', '')
        for char in line:
            row.append(int(char))
        grid.append(row)
    for i, row in enumerate(grid):
        if i == 0 or i == len(grid) - 1:
            visible += len(row)
            continue
        for j, b in enumerate(row):
            if j == 0 or j == len(row) - 1:
                visible += 1
            else:
                if max(row[:j]) < b:
                    visible += 1
                elif max(row[j + 1:]) < b:
                    visible += 1
                elif max([row[j] for row in grid[:i]]) < b:
                    visible += 1
                elif max([row[j] for row in grid[i + 1:]]) < b:
                    visible += 1
    scene = 0
    x = len(grid) - 1
    y = len(grid[0]) - 1


    def count(r, t):
        c = 0
        for e in r:
            c += 1
            if e >= t:
                return c
        return c


    for i, row in enumerate(grid):
        for j, b in enumerate(row):
            m_scene = count(reversed(row[:j]), b) * count(row[j + 1:], b) * count(reversed(
                [row[j] for row in grid[:i]]), b) * count([row[j] for row in grid[i + 1:]], b)
            if m_scene > scene:
                scene = m_scene
    print(scene)
