def update_d(d, e, i):
    if e in d.keys():
        d[e][1] = d[e][0]
        d[e][0] = i
    else:
        d[e] = [i, i]
    return d

with open("day_15_input.txt") as ip:
    n = [int(i) for i in ip.read().splitlines()[0].split(',')]
    d = {x[1]:[x[0]+1, x[0]+1] for x in enumerate(n)} #{n: [last_spoken, first_spoken]}
    last = n[-1]
    for i in range(len(n)+1, 2020+1):
        if d[last][0] == d[last][1]:
            last = 0
            d = update_d(d, 0, i)
        else:
            last = d[last][0]-d[last][1]
            d = update_d(d, last, i)
    print("silver:", last)