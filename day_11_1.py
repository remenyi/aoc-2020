from copy import deepcopy

def next_step(x, y, s, c):
    n = s[x-1][y] if x>0 else None
    ne = s[x-1][y+1] if x>0 and y<len(s[0])-1 else None
    e = s[x][y+1] if y<len(s[0])-1 else None
    se = s[x+1][y+1] if y<len(s[0])-1 and x<len(s)-1 else None
    so = s[x+1][y] if x<len(s)-1 else None
    ew = s[x+1][y-1] if y>0 and x<len(s)-1 else None
    w = s[x][y-1] if y>0 else None
    nw = s[x-1][y-1] if y>0 and x>0 else None
    l = [n,ne,e,se,so,ew,w,nw]
    if c == 'L' and '#' not in l:
        return '#'
    elif c == '#' and l.count('#') >= 4:
        return 'L'
    else:
        return c

with open("day_11_input.txt") as ip:
    s = ip.read().splitlines()
    o = []
    while o != s:
        s = deepcopy(o) if o != [] else s
        o = []
        for i, j in enumerate(s):
            l = []
            for n, m in enumerate(j):
                l.append(next_step(i, n, s, m))
            o.append(l)
    print("silver: " + str(sum(i.count('#') for i in o)))