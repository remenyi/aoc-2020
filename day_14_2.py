import re

def mask(m, n):
    b = str(bin(n))[2:]
    b = b[::-1]
    m = m[::-1]
    nn = ''
    for i,j in enumerate(m):
        if j == '0' and i < len(b):
            nn += b[i]
        elif j == '0' and i >= len(b):
            nn += '0'
        elif j == '1':
            nn += '1'
        else:
            nn += 'X'
    nn = nn[::-1]
    return nn

def mask_array(m):
    if m.find('X') == -1:
        return [int(m, 2)]
    m0 = m
    m0 = m0.replace('X', '0', 1)
    m1 = m
    m1 = m1.replace('X', '1', 1)
    ma = []
    ma += mask_array(m0)
    ma += mask_array(m1)
    return ma

with open("day_14_input.txt") as ip:
    l = [(i.split(" ")[0], i.split(" ")[-1]) for i in ip.read().splitlines()]
    m = ''
    d = dict()
    for i, j in l:
        if i == 'mask':
            m = j
        else:
            idx = int(re.search(r"\d+", i).group())
            for k in mask_array(mask(m, idx)):
                d[k] = int(j)
    print("gold", sum([d[i] for i in d]))