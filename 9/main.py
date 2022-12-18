import re
import time


def show(heads, snakes):
    height, width = 6, 6
    grid = ['.'.join(['' for i in range(width * 2)]) for j in range(height * 2)]
    for i, t in enumerate(reversed(snakes)):
        grid[-t[0] + height] = grid[-t[0] + height][:t[1] + width] + str(9-i) + grid[-t[0] + height][t[1] + width + 1:]
    grid[-heads[0] + height] = grid[-heads[0] + height][:heads[1] + width] + 'H' + grid[-heads[0] + height][heads[1] + width + 1:]
    print('\n'.join(grid))


with open('input') as file:
    visited = {(0, 0)}
    snake = [[0, 0] for i in range(9)]
    head = [0, 0]
    changes = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}
    pattern = re.compile(r'(?P<dir>[A-Z]) (?P<amount>\d+)')
    for line in file.readlines():
        m = re.search(pattern, line)
        d, a = m.group('dir'), int(m.group('amount'))
        for i in range(a):
            head[0] += changes[d][0]
            head[1] += changes[d][1]
            c_head = head
            for tail in snake:
                dif = (c_head[0] - tail[0], c_head[1] - tail[1])
                if (dif[0] > 1 or dif[0] < -1) and dif[1] != 0:
                    tail[0] += dif[0] // 2
                    tail[1] += -1 if dif[1] == -2 else (1 if dif[1] == 2 else dif[1])
                elif (dif[1] > 1 or dif[1] < -1) and dif[0] != 0:
                    tail[1] += dif[1] // 2
                    tail[0] += -1 if dif[0] == -2 else (1 if dif[0] == 2 else dif[0])
                else:
                    tail[1] += 0 if dif[1] == -1 else (dif[1] // 2)
                    tail[0] += 0 if dif[0] == -1 else (dif[0] // 2)
                c_head = tail
            visited.add((snake[8][0], snake[8][1]))
            # show(head, snake)
            # print('==============')
            # time.sleep(0.01)

    print(len(visited))
