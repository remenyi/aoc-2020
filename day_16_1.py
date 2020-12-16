def invalid(x):
    valid = False
    for k in ranges:
        if ranges[k][0][0] <= x <= ranges[k][0][1] or ranges[k][1][0] <= x <= ranges[k][1][1]:
            valid = True
    return x if not valid else None

with open("day_16_input.txt") as ip:
    blocks = [x for x in ip.read().split("\n\n")]
    ranges = {x.split(':')[0] : [(int(y.strip().split('-')[0]), int(y.strip().split('-')[1])) for y in x.split(':')[1].split('or')] for x in blocks[0].splitlines()}
    tickets = [[int(y) for y in x.split(',')] for x in blocks[2].splitlines()[1:]]
    errors = list(filter(invalid, [i for j in tickets for i in j]))
    print("silver:", sum(errors))