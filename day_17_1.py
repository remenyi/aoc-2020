def neighbor_count(grid, box):
    nc =  len(list(filter(lambda x: -1 <= x[0]-box[0] <= 1 and
                            -1 <= x[1]-box[1] <= 1 and
                            -1 <= x[2]-box[2] <= 1
                    , grid)))
    return nc - 1 if box in grid else nc
        
def neighbors(box):
    n = set()
    for x in range(-1, 1+1):
        for y in range(-1, 1+1):
            for z in range(-1, 1+1):
                n.add((box[0]+x, box[1]+y, box[2]+z))
    n.remove(box)
    return n

def next_state(grid):
    remainsactive = set(filter(lambda x: 2 <= neighbor_count(grid, x) <=3, grid))
    candidates = list(map(lambda x: neighbors(x), grid))
    candidates = {i for s in candidates for i in s}
    filtered_candidates = set(filter(lambda x: neighbor_count(grid, x) == 3, candidates))
    return remainsactive | filtered_candidates

with open("day_17_input.txt") as ip:
    ip = [i for i in ip.read().splitlines()]
    grid = set()
    for x, l in enumerate(ip):
        for y, e in enumerate(l):
            if e == '#':
                grid.add((0, x, y))
    for i in range(6):
        grid = next_state(grid)
    print("silver:", len(grid))