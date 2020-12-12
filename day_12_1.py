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

def new_dir(a, d, deg):
    deg = int(deg/90)
    dirs = ['N', 'E', 'S', 'W']
    i = (dirs.index(d)+deg)%4 if a == 'R' else dirs.index(d)-deg
    return dirs[i]

with open("day_12_input.txt") as ip:
    n = [(i[0], int(i[1:])) for i in ip.read().splitlines()]
    d = 'E'
    ew = ns = 0
    for a, v in n:
        ew, ns = new_pos(a, v, ew, ns)
        if a == 'F':
            ew, ns = new_pos(d, v, ew, ns)
        if a == 'L' or a == 'R':
            d = new_dir(a, d, v)
    print("silver: ", abs(ew)+abs(ns))

        