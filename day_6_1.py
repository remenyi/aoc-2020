with open("day_6_input.txt") as ip:
    lines = [i.replace("\n", "") for i in ip.read().split("\n\n")]
    sets = list(map(lambda x : {i for i in x}, lines))
    counts = list(map(lambda x : len(x), sets))
    print("Sum: " + str(sum(counts)))