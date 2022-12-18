import re

pattern = re.compile('(?P<size>\d+) (?P<name>[a-zA-Z]+(.[a-zA-Z]+))\n')
dir_pattern = re.compile('(dir|\$ cd) (?P<name>[a-zA-Z]+)')


def rec_dirs(ds):
    totals = [ds['size']]
    for d in ds['dirs'].values():
        totals = totals + rec_dirs(d)
    return totals


with open('input') as file:
    dirs = {'dirs': {}, 'files': {}, 'size': 0}
    tree = None
    for line in file.readlines():
        if line.startswith('$ cd /'):
            tree = [dirs]
        elif line.startswith('$ cd ..'):
            tree.pop(0)
        elif line.startswith('$ cd '):
            tree.insert(0, tree[0]['dirs'][re.search(dir_pattern, line).group('name')])
        elif line.startswith('dir'):
            tree[0]['dirs'][re.search(dir_pattern, line).group('name')] = {'dirs': {}, 'files': {}, 'size': 0}
        elif line.startswith('$ ls'):
            pass
        else:
            m = re.search(pattern, line)
            if m.group('name') not in tree[0]['files']:
                size = int(m.group('size'))
                tree[0]['files'][m.group('name')] = size
                for entry in tree:
                    entry['size'] += size
    sizes = rec_dirs(dirs)
    total_size = sizes.pop(0)
    to_remove = total_size - 40000000
    print(to_remove)
    print(sorted(filter(lambda x: x >= to_remove, sizes))[0])
