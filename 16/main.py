import math
import re

with open('input') as file:
    pattern = re.compile(
        r'Valve (?P<valve>[A-Z]{2}) has flow rate=(?P<flow>\d+); tunnels? leads? to valves? (?P<tunnels>([A-Z]{2}(, )?)+)')
    t_pattern = re.compile(r'(?P<tunnel>[A-Z]{2})')
    valves = {}
    for m in re.finditer(pattern, file.read()):
        valve = m.group('valve')
        if valve not in valves:
            valves[valve] = {'tunnels': [], 'flow': 0, 'routes': {}}
        valves[valve]['tunnels'] = [mt.group('tunnel') for mt in re.finditer(t_pattern, m.group('tunnels'))]
        valves[valve]['flow'] = int(m.group('flow'))

    for vid, valve in valves.items():
        valve['routes'] = {v: {'d': 1, 'next': v} for v in valve['tunnels']}

    update = True
    while (update):
        update = False
        for vid, valve in valves.items():
            for tid in valve['tunnels']:
                for ttid, route in valve['routes'].items():
                    if ttid not in valves[tid]['routes']:
                        valves[tid]['routes'][ttid] = {'d': route['d'] + 1, 'next': vid}
                        update = True
                    elif ttid in valves[tid]['routes'] and valves[tid]['routes'][ttid]['d'] > route['d'] + 1:
                        valves[tid]['routes'][ttid]['d'] = route['d'] + 1
                        valves[tid]['routes'][ttid]['next'] = vid
                        update = True
    open_valves = []
    released = 0
    remaining = 30
    move_to = None
    current = 'AA'
    minutes = 30


    def value(tup):
        target, r = tup
        if target in open_valves:
            return 0
        return remaining * valves[target]['flow'] - (r['d'] + 1) * valves[target]['flow']


    vs = dict(filter(lambda x: x[1]['flow'] > 0, valves.items()))
    keys = list(vs.keys())
    edges = [{'chain': [vid], 'time': valves['AA']['routes'][vid]['d'] + 1, 'points': 0} for vid, valve in vs.items()]
    for edge in edges:
        edge['points'] = (minutes - edge['time']) * valves[edge['chain'][-1]]['flow']

    result = 0
    while len(edges) > 0:
        n_edges = []
        for edge in edges:
            c = edge['chain'][-1]
            valve = valves[c]
            for k in filter(lambda x: x not in edge['chain'], keys):
                if valve['routes'][k]['d'] + 1 < minutes - edge['time']:
                    r = edge['time'] + valve['routes'][k]['d'] + 1
                    n_edges.append({'chain': edge['chain'] + [k], 'time': r,
                                    'points': edge['points'] + (minutes - r) * valves[k]['flow']})
            if edge['points'] > result:
                result = edge['points']
        edges = n_edges
        print(len(edges))
    print(f"First result {result}")
    minutes = 26

    edges = [{'visited': [vid], 'pos': [vid], 'times': [valves['AA']['routes'][vid]['d'] + 1], 'points': 0} for
             vid, valve in vs.items()]
    all_edges = []
    for edge in edges:
        for el in filter(lambda x: x not in edge['visited'], keys):
            e = {'visited': edge['visited'] + [el], 'pos': edge['pos'] + [el],
                 'times': edge['times'] + [valves['AA']['routes'][el]['d'] + 1], 'points': 0}
            e['points'] += (minutes - e['times'][0]) * valves[e['pos'][0]]['flow']
            e['points'] += (minutes - e['times'][1]) * valves[e['pos'][1]]['flow']
            all_edges.append(e)
    edges = all_edges
    while len(edges) > 0:
        n_edges = []
        prune = 0
        for edge in edges:
            i = sorted(enumerate(edge['times']), key=lambda x: x[1])[0][0]
            valve = valves[edge['pos'][i]]
            for k in filter(lambda x: x not in edge['visited'], keys):
                if valve['routes'][k]['d'] + 1 < minutes - edge['times'][i]:
                    r = edge['times'][i] + valve['routes'][k]['d'] + 1
                    pos = edge['pos'][:]
                    pos[i] = k
                    times = edge['times'][:]
                    times[i] = r
                    e = {'visited': edge['visited'] + [k], 'pos': pos, 'times': times,
                         'points': edge['points'] + (minutes - r) * valves[k]['flow']}
                    times = e['times'][:]
                    optimal = e['points']
                    for l in sorted(filter(lambda x: x not in e['visited'], keys), key=lambda x: valves[x]['flow'], reverse=True):
                        times.sort()
                        if times[0] < minutes - 2:
                            optimal += valves[l]['flow'] * (minutes - (times[0] + 2))
                            times[0] += 2
                        else:
                            break
                    if result < optimal:
                        n_edges.append(e)
                    else:
                        prune += 1
            if edge['points'] > result:
                result = edge['points']
        edges = n_edges
        print(len(edges))
        print(f"Pruned {prune}")

    print(result)
