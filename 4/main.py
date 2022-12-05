import re
pattern = re.compile('(?P<ff>\d+)-(?P<ft>\d+),(?P<lf>\d+)-(?P<lt>\d+)')
with open('input') as file:
    c = 0
    for line in file.readlines():
        m = re.search(pattern, line)
        ff, ft, lf, lt = int(m.group('ff')), int(m.group('ft')), int(m.group('lf')), int(m.group('lt'))
        if ff >= lf and ff <=lt:
            c += 1
        elif lf >= ff and lf <= ft:
            c+= 1

    print(c)
