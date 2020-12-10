with open("day_10_input.txt") as ip:
    a = [int(i) for i in ip.read().splitlines()]
    a.append(0)
    a.append(max(a)+3)
    a.sort()
    d1 = len([(i, j) for i, j in zip(a, a[1:]) if j-i == 1])
    d3 = len([(i, j) for i, j in zip(a, a[1:]) if j-i == 3])
    print("silver: " + str(d1*d3))