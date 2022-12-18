import json
import re
from functools import cmp_to_key

l_pattern = re.compile(r'\[(?P<values>.+)]')


def compare(f, s):
    if isinstance(f, int) and isinstance(s, int):
        return 0 if f == s else (1 if f > s else -1)
    elif isinstance(f, list) and isinstance(s, int):
        s = [s]
    elif isinstance(f, int) and isinstance(s, list):
        f = [f]
    for i, element in enumerate(s):
        if i >= len(f):
            return -1
        res = compare(f[i], element)
        if res != 0:
            return res
    return 0 if len(f) == len(s) else (1 if len(f) > len(s) else -1)


with open('input') as file:
    first, second = None, None
    c = 1
    pairs = []
    all_pairs = []
    for line in file.readlines():
        if line == '\n':
            first, second = None, None
            c += 1
        elif first is None:
            first = json.loads(line)
            all_pairs.append(first)
        elif second is None:
            second = json.loads(line)
            all_pairs.append(second)
            res = compare(first, second)
            if res <= 0:
                pairs.append(c)
    all_pairs.append([[2]])
    all_pairs.append([[6]])
    s_pairs = sorted(all_pairs, key=cmp_to_key(compare))
    print((s_pairs.index([[2]]) + 1) * (s_pairs.index([[6]]) + 1))
    print(sum(pairs))
