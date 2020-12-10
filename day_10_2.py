with open("day_10_input.txt") as ip:
    a = [int(i) for i in ip.read().splitlines()]
    a.append(0)
    a.append(max(a)+3)
    a.sort()
    #linear programming
    c = [1, 1]
    #sorry
    c.append(sum(c[3-len( \
        [j for j in range(0, 3) if j in a[:3] ] \
            ):]))
    for i, e in enumerate(n:=a[3:], 3):
        c.append(sum(c[i-len( \
            [j for j in range(e-3, e) if j in a[i-3:i]] \
                ):]))
    print("gold: " + str(c[-1]))