from math import sqrt
from copy import deepcopy
import re

def get_edges(tile):
    edges = [tile[0], 
            ''.join([tile[i][-1] for i in range(len(tile))]),
            tile[-1],
            ''.join([tile[i][0] for i in range(len(tile))])]
    return edges

def rotate(tile):
    new_tile = []
    for i in range(len(tile[0])):
        new_row = []
        for j in range(len(tile)):
            new_row.append(tile[j][i])
        new_tile.append(''.join(new_row[::-1]))
    return new_tile

def rotate_n(tile, n):
    new_tile = tile
    for i in range(n):
        new_tile = rotate(tile)
    return new_tile

def flip_h(tile):
    new_tile = tile[::-1]
    return new_tile

def flip_v(tile):
    new_tile = []
    for t in tile:
        new_tile.append(t[::-1])
    return new_tile

def to_dir(n):
    dirs = ['n', 'e', 's', 'w']
    return dirs[n]

def to_num(d):
    dirs = ['n', 'e', 's', 'w']
    return dirs.index(d)

def check_matching(e1, e2):
    if e1[0] == e2[2]:
        return e1[0]
    elif e1[1] == e2[3]:
        return e1[1]
    elif e1[2] == e2[0]:
        return e1[2]
    elif e1[3] == e2[1]:
        return e1[3]
    else:
        return None

def get_neighbors(tile):
    global tiles
    edges = get_edges(tiles[tile])
    neighbors = []
    tiles_minus_tile = list((i for i in tiles if i != tile))
    for t in tiles_minus_tile:
        n_candidate = tiles[t]
        for i in range(4):
            t_edges = get_edges(n_candidate)
            matching_sides = check_matching(edges, t_edges)
            if matching_sides:
                dir_transformed = edges.index(matching_sides)
                neighbors.append((t, i, dir_transformed))
                break
            t_edges = get_edges(flip_h(n_candidate))
            matching_sides = check_matching(edges, t_edges)
            if matching_sides:
                dir_transformed = edges.index(matching_sides)
                neighbors.append((t, str(i)+"h", dir_transformed))
                break
            t_edges = get_edges(flip_v(n_candidate))
            matching_sides = check_matching(edges, t_edges)
            if matching_sides:
                dir_transformed = edges.index(matching_sides)
                neighbors.append((t, str(i)+"v", dir_transformed))
                break
            t_edges = get_edges(flip_v(flip_h(n_candidate)))
            matching_sides = check_matching(edges, t_edges)
            if matching_sides:
                dir_transformed = edges.index(matching_sides)
                neighbors.append((t, str(i)+"hv", dir_transformed))
                break
            t_edges = get_edges(flip_h(flip_v(n_candidate)))
            matching_sides = check_matching(edges, t_edges)
            if matching_sides:
                dir_transformed = edges.index(matching_sides)
                neighbors.append((t, str(i)+"vh", dir_transformed))
                break
            t_edges = get_edges(flip_v(flip_h(flip_v(n_candidate))))
            matching_sides = check_matching(edges, t_edges)
            if matching_sides:
                dir_transformed = edges.index(matching_sides)
                neighbors.append((t, str(i)+"vhv", dir_transformed))
                break
            t_edges = get_edges(flip_h(flip_v(flip_h(n_candidate))))
            matching_sides = check_matching(edges, t_edges)
            if matching_sides:
                dir_transformed = edges.index(matching_sides)
                neighbors.append((t, str(i)+"hvh", dir_transformed))
                break
            n_candidate = rotate(n_candidate)
    return neighbors


def transform(tile, rules):
    for r in rules:
        if r == 'h':
            tile = flip_h(tile)
        elif r == 'v':
            tile = flip_v(tile)
        else:
            tile = rotate_n(tile, int(r))            
    return tile

def transformdir(dir, rules):
    for r in rules:
        if r == 'h':
            if dir == 0:
                dir = 2
            elif dir == 2:
                dir = 0
        elif r == 'v':
            if dir == 1:
                dir = 3
            elif dir == 3:
                dir = 1
        else:
            dir = (int(r)+dir)%4
    return dir


def build_map(tile, rules, x, y):
    global tile_stack
    global tiles
    global picture
    if tile in tile_stack:
        return
    tile_stack.append(tile)
    transformed_tile = transform(tiles[tile], rules)
    picture[(x,y)] = transformed_tile
    neighbors = get_neighbors(tile)
    for n in neighbors:
        transformed_dir = transformdir(n[2], rules)
        if transformed_dir == 0:
            build_map(n[0], str(n[1])+rules, x, y-1)
        if transformed_dir == 1:
            build_map(n[0], str(n[1])+rules, x+1, y)
        if transformed_dir == 2:
            build_map(n[0], str(n[1])+rules, x, y+1)
        if transformed_dir == 3:
            build_map(n[0], str(n[1])+rules, x-1, y)

def find_min_max_x_y(pic):
    x_val = []; y_val = []
    for k in pic:
        x_val.append(k[0])
        y_val.append(k[1])
    return (min(x_val), max(x_val), min(y_val), max(y_val))

def join_lines(line):
    ret = []
    for i in range(1, len(line[0])-1):
        nl = ''
        for j in range(len(line)):
            nl += line[j][i][1:-1] 
        ret.append(nl)
    return ret



def generate_map(pic):
    map = []
    map_size = int(sqrt(len(tiles)))
    min_x, max_x, min_y, max_y = find_min_max_x_y(pic)
    big_map = []
    for y in range(min_y, max_y+1):
        line = []
        for x in range(min_x, max_x+1):
            line.append(pic[(x, y)])
        big_map.append(join_lines(line))
    return big_map

def monster_count_alt(sea):
    head = r'(\.|#){18,}#(\.|#)+'
    body = r'(\.|#)*#(\.|#){4}##(\.|#){4}##(\.|#){4}###(\.|#)*'
    legs = r'(\.|#)+#(\.|#){2}#(\.|#){2}#(\.|#){2}#(\.|#){2}#(\.|#){2}#(\.|#){3,}'
    count = 0
    for i in range(2, len(sea)):
        j = 0
        while j+20 < len(sea[0]):
            j += 1
            has_head = re.search(head, sea[i-2][j:j+20])
            has_body = re.search(body, sea[i-1][j:j+20])
            has_legs = re.search(legs, sea[i][j:j+20])
            if has_body and has_head and has_legs:
                count += 1
    return count

def list_to_string(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1  

with open("day_20_input.txt") as ip:
    tiles = {int(x.splitlines()[0].split(' ')[1][:-1]): x.splitlines()[1:] for x in ip.read().split('\n\n')}
    tile_stack = []
    picture = dict()
    build_map(list(tiles.keys())[3], '', 0, 0)

    flatten = lambda t: [item for sublist in t for item in sublist]
    flat_map = flatten(generate_map(picture))
    
    sea_monsters = 0
    sea_monsters_h = 0
    for i in range(4):
        sea_monsters = monster_count_alt(flat_map)
        if sea_monsters > sea_monsters_h:
            sea_monsters_h = sea_monsters
        flat_map = rotate(flat_map)

    flat_map = flip_h(flat_map)
    for i in range(4):
        sea_monsters = monster_count_alt(flat_map)
        if sea_monsters > sea_monsters_h:
            sea_monsters_h = sea_monsters
        flat_map = rotate(flat_map)

    hashmarks = sum(list(map(lambda x: x.count("#"), flat_map)))
    print("gold:", hashmarks-(sea_monsters_h*15))