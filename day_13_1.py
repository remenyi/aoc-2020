with open("day_13_input.txt") as ip:
    lines = ip.read().splitlines()
    t = int(lines[0])
    d = [int(i) for i in lines[1].split(',') if i != 'x']
    dist = list(map(lambda x: x-(t%x), d))
    print("silver:", min(dist)*d[dist.index(min(dist))])
