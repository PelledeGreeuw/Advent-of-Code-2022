with open('input') as file:
    directions = file.read().replace('\n', '')


    def next_dir():
        while 1:
            for i, c in enumerate(directions):
                yield i, ((1, 0) if c == '>' else (-1, 0))
                yield -1, (0, 1)


    rocks = [
        (4, (
            0b1111,
        )),
        (3, (
            0b010,
            0b111,
            0b010
        )),
        (3, (
            0b001,
            0b001,
            0b111
        )),
        (1, (
            0b1,
            0b1,
            0b1,
            0b1
        )),
        (2, (
            0b11,
            0b11
        ))
    ]


    def next_rock():
        while 1:
            for i, rck in enumerate(rocks):
                yield i, rck

    print(12138 - 9492)
    width = 7
    height = 0
    grid = [0b1111111]
    n_rock = next_rock()
    n_dir = next_dir()
    previous_grid = grid
    previous_height = 0
    previous_x = 0
    heights = []
    cycle_height = 0
    found_cycle = False
    total = 1000000000000
    previous_pos = (0,0)
    for x in range(total):
        if x % 10000 == 0:
            print(x)
        i_r, (l_r, rock) = next(n_rock)
        pos = (2, -3 - len(rock))

        while 1:
            i_d, d = next(n_dir)
            if i_d == 0 and i_r == 0:
                if len(grid) == len(previous_grid) and previous_pos == pos and len(grid) > 1 and all([grid[i] == previous_grid[i] for i in range(len(grid))]):
                    # print(heights)
                    # print(previous_height, previous_x, cycle_height, x, len(heights), x - previous_x)
                    remaining = (total - previous_x) % len(heights)
                    loops = (total - previous_x) // len(heights)
                    # print(remaining, loops, loops * len(heights) + previous_x + remaining)
                    height = cycle_height + (heights[-1] * loops) + heights[remaining]
                    grid = []
                    found_cycle = True
                    break
                else:
                    previous_x = x
                    previous_pos = pos
                    previous_height = height
                    cycle_height = height + len(grid) - 1
                    previous_grid = grid[:]
                    heights = []

            # print(d, pos)
            n_pos = pos[0] + d[0], pos[1] + d[1]
            if n_pos[0] < 0 or width < n_pos[0] + l_r:
                continue
            collision = False
            lowest = n_pos[1] + (len(rock) - 1)
            for i in range(min(lowest + 1, len(rock))):
                # print(width - l_r - n_pos[0])
                # print(grid[lowest - i])
                # print(grid[lowest - i] & (rock[len(rock) - 1 - i] << (width - l_r - n_pos[0])))
                if grid[lowest - i] & (rock[len(rock) - 1 - i] << (width - l_r - n_pos[0])):
                    collision = True
                    break
            if not collision:
                pos = n_pos
            if collision and d[1]:
                break
        if found_cycle:
            break
        if pos[1] < 0:
            for _ in range(abs(pos[1])):
                grid.insert(0, 0b0000000)
            pos = pos[0], 0
        for i, row in enumerate(rock):
            grid[i + pos[1]] = grid[i + pos[1]] | row << (width - l_r - pos[0])
        heights.append((height + len(grid) - 1) - cycle_height)
        for i in range(len(grid) - 1):
            if grid[i] == 0b1111111:
                height += (len(grid) - (i + 1))
                grid = grid[:i + 1]
                break
    # for row in grid:
    #     print(''.join(['#' if x else '.' for x in row]))

    print(height + len(grid) - 1)
