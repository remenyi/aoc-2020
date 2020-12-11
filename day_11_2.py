from copy import deepcopy
import os

def next_step(x, y, s, c):
    #north
    nd = [i[y] for i in s[:x]]
    nds = ''.join(map(str, nd)).strip('.')
    n = nds[-1] if x>0 and len(nds) else None

    #north-east
    ned = [i[y+j+1] for j, i in enumerate(s[:x][::-1]) if j+1 <= len(s[x][y:])-1]
    neds = ''.join(map(str, ned)).strip('.')
    ne = neds[0] if x>0 and y<len(s[0])-1 and len(neds)>0 else None

    #east
    e = s[x][y+1:].strip('.')[0] if y<len(s[0])-1 and len(s[x][y+1:].strip('.')) > 0 else None

    #south-east
    sed = [i[y+j+1] for j, i in enumerate(s[x+1:]) if j+1 <= len(s[x][y:])-1]
    seds = ''.join(map(str, sed)).strip('.')
    se = seds[0] if y<len(s[0])-1 and x<len(s)-1 and len(seds)>0 else None

    #south
    sod = [i[y] for i in s[x+1:]]
    sods = ''.join(map(str, sod)).strip('.')
    so = sods[0] if x<len(s)-1 and len(sods)>0 else None

    #east-west
    ewd = [i[y-j-1] for j, i in enumerate(s[x+1:]) if j <= len(s[x][:y])-1]
    ewds = ''.join(map(str, ewd)).strip('.')
    ew = ewds[0] if y>0 and x<len(s)-1 and len(ewds)>0 else None

    #west
    w = s[x][:y].strip('.')[-1] if y>0 and len(s[x][:y].strip('.'))>0 else None

    #north-west
    nwd = [i[y-j-1] for j, i in enumerate(s[:x][::-1]) if j <= len(s[x][:y])-1]
    nwds = ''.join(map(str, nwd)).strip('.')
    nw = nwds[0] if y>0 and x>0 and len(nwds)>0 else None

    l = [n,ne,e,se,so,ew,w,nw]
    if c == 'L' and '#' not in l:
        return '#'
    elif c == '#' and l.count('#') >= 5:
        return 'L'
    else:
        return c

with open("day_11_input.txt") as ip:
    s = ip.read().splitlines()
    print(s)
    o = []
    while o != s:
        s = deepcopy(o) if o != [] else s
        o = []
        for i, j in enumerate(s):
            l = ''
            for n, m in enumerate(j):
                l += next_step(i, n, s, m)
            o.append(l)
        os.system('cls' if os.name == 'nt' else 'clear')
        [print(i) for i in o]
    print("gold: " + str(sum(i.count('#') for i in o)))