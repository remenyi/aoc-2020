from math import prod

def get_neighbor_count(edges):
    global tile_edges
    count = [-1]*len(edges)
    for i, e in enumerate(edges):
        count[i] += len(list(filter(lambda te: e in tile_edges[te], tile_edges)))
    return count

def get_edges(tile):
    edges = [tile[0], 
            ''.join([tile[i][-1] for i in range(len(tile))]),
            tile[-1],
            ''.join([tile[i][0] for i in range(len(tile))])]
    [edges.append(edges[i][::-1]) for i in range(4)]
    return edges

with open("day_20_input_ex.txt") as ip:
    tiles = {int(x.splitlines()[0].split(' ')[1][:-1]): x.splitlines()[1:] for x in ip.read().split('\n\n')}
    tile_edges = dict(map(lambda x: (x[0], get_edges(x[1])), tiles.items()))
    neighbor_counts = dict(map(lambda x: (x[0], get_neighbor_count(x[1])), tile_edges.items()))
    corners = dict(filter(lambda x: x[1].count(0) == 4, neighbor_counts.items()))
    print('silver:', prod(list(corners.keys())))