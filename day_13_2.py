from math import prod


def inverse(Ni, m):
    Ni = Ni % m
    x = 0
    while (Ni*x) % m != 1:
        x += 1
    return x


with open("day_13_input.txt") as ip:
    lines = ip.read().splitlines()
    d = [(i, int(j)) for i, j in enumerate(lines[1].split(',')) if j != 'x']
    # Solved with the chinese remainder theorem
    N = prod([k[1] for k in d])
    X = 0
    for i in d:
        Ni = int(N/i[1])
        X += (i[1]-i[0])*Ni*inverse(Ni, i[1])
    print("gold:", X % N)
