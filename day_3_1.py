with open("day_3_input.txt") as ip:
    lines = ip.read().splitlines()
    lines.pop(0)
    step = 3
    count = 0
    for l in lines:
        if l[step] == "#":
            count += 1
        step += 3
        if step >= len(l):
            step = step - len(l)
    print(count)
