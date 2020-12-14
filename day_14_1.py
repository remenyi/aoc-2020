import re

def mask(m, n):
    b = str(bin(n))[2:]
    b = b[::-1]
    m = m[::-1]
    nn = ''
    for i,j in enumerate(m):
        if i < len(b):
            nn += b[i] if j ==  'X' else j
        else:
            nn += '0' if j == 'X' else j
    nn = nn[::-1]
    return int("0b" + nn, 2)

with open("day_14_input.txt") as ip:
    l = [(i.split(" ")[0], i.split(" ")[-1]) for i in ip.read().splitlines()]
    m = ''
    d = dict()
    for i, j in l:
        if i == 'mask':
            m = j
        else:
            idx = int(re.search(r"\d+", i).group())
            d[idx] = mask(m, int(j))
    print("silver:", sum([d[i] for i in d]))