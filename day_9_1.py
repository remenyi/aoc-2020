from itertools import combinations

with open("day_9_input.txt") as ip:
    l = [int(i) for i in ip.read().splitlines()]
    i = p = 25
    q = l[0:p]
    while (n := l[i]) in [i+j for i, j in combinations(q, 2)]:
        q.pop(0)
        q.append(n) 
        i += 1
    print("silver: " + str(n))