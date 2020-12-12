def new_pos(a, v, ew, ns):
    if a == 'N':
        ns += v
    elif a == 'S':
        ns -= v
    elif a == 'E':
        ew += v
    elif a == 'W':
        ew -= v
    return (ew, ns)

with open("day_12_input.txt") as ip:
    n = [(i[0], int(i[1:])) for i in ip.read().splitlines()]
    d = 'E'
    ew = 10
    ns = 1
    x = y = 0
    for a, v in n:
        ew, ns = new_pos(a, v, ew, ns)
        if a == 'F':
            x += ns*v
            y += ew*v
        if a == 'L' or a == 'R':
            if v == 270:
                v = 90
                a = 'L' if a == 'R' else 'R'
            if v == 180:
                ew = -ew
                ns = -ns
            elif v == 90 and a == 'R':
                ew, ns = ns, -ew
            elif v == 90 and a == 'L':
                ew, ns = -ns, ew
    print("silver: ", abs(x)+abs(y))