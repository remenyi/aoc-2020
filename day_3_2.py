def tree_enc(map, right, down):
    count = 0
    step = right
    for i in range(down, len(map), down):
        if map[i][step] == "#":
            count += 1
        step += right
        if step >= len(map[0]):
            step = step - len(map[0])
    return count

with open("day_3_input.txt") as ip:
    lines = ip.read().splitlines()
    product = tree_enc(lines, 1, 1) * tree_enc(lines, 3, 1) * tree_enc(lines, 5, 1) * tree_enc(lines, 7, 1) * tree_enc(lines, 1, 2)
    print(product)
