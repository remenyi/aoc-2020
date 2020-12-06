with open("day_6_input.txt") as ip:
    lines = [i.splitlines() for i in ip.read().split("\n\n")]
    counts = list(map(lambda x: len(set.intersection(*map(set, x))), lines))
    print("Sum: " + str(sum(counts)))