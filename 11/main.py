import math
import re
import time

pattern = re.compile(
    'Monkey \d:\n +Starting items: (?P<items>(?:\d,? ?)+)\n +Operation: new = old (?P<op>.) (?P<target>.+)\n + Test: divisible by (?P<divide>\d+)\n +If true: throw to monkey (?P<m1>\d)\n +If false: throw to monkey (?P<m2>\d)\n')


def update(old, op, target):
    val = old if target == 'old' else int(target)
    if op == '*':
        return old * val
    elif op == '+':
        return old + val
    else:
        return old - val


with open('input') as file:
    monkeys = []
    for m in re.finditer(pattern, file.read()):
        monkey = {"divide": int(m.group('divide')), "true": int(m.group('m1')), "false": int(m.group('m2')),
                  "items": [], "checks": 0, "op": m.group('op'), "target": m.group('target')}
        for mi in re.finditer(r'(?P<item>\d+)', m.group('items')):
            monkey["items"].append(int(mi.group('item')))
        monkeys.append(monkey)
    for i in range(20):
        for j, monkey in enumerate(monkeys):
            for item in monkey['items']:
                monkey['checks'] += 1
                item = update(item, monkey['op'], monkey['target'])
                item = item // 3
                if item % monkey['divide'] == 0:
                    monkeys[monkey['true']]['items'].append(item)
                else:
                    monkeys[monkey['false']]['items'].append(item)
            monkey['items'] = []
    checks = sorted([monkey['checks'] for monkey in monkeys], reverse=True)
    print(checks)
    print(checks[0] * checks[1])

with open('input') as file:
    monkeys = []
    for m in re.finditer(pattern, file.read()):
        monkey = {"divide": int(m.group('divide')), "true": int(m.group('m1')), "false": int(m.group('m2')),
                  "items": [], "checks": 0, "op": m.group('op'), "target": m.group('target')}
        for mi in re.finditer(r'(?P<item>\d+)', m.group('items')):
            monkey["items"].append(int(mi.group('item')))
        monkeys.append(monkey)

    common = monkeys[0]['divide']
    for m in monkeys[1:]:
        common = common * m['divide']
    print(math.prod([monkey['divide'] for monkey in monkeys]))
    print(common)

    for i in range(10000):
        for j, monkey in enumerate(monkeys):
            for item in monkey['items']:
                monkey['checks'] += 1
                item = item % common
                item = update(item, monkey['op'], monkey['target'])
                # item = item // 3
                if item % monkey['divide'] == 0:
                    monkeys[monkey['true']]['items'].append(item)
                else:
                    monkeys[monkey['false']]['items'].append(item)
            monkey['items'] = []
    checks = sorted([monkey['checks'] for monkey in monkeys], reverse=True)
    print(checks)
    print(checks[0] * checks[1])
