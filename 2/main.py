score = 0
beats = {'A': 'C', 'B': 'A', 'C': 'B'}
loses = {'C': 'A', 'A': 'B', 'B': 'C'}
values  = {'A': 1, 'B': 2, 'C': 3}
transpose = {'X': 'A', 'Y': 'B', 'Z': 'C'}
with open('input') as file:
    for line in file.readlines():
        them, me = line[0], line[2]
        if me == 'X':
            me = beats[them]
        elif me == 'Y':
            me = them
        else:
            me = loses[them]
        score += values[me]
        if them == me:
            score += 3
        elif beats[me] == them:
            score += 6
print(score)
