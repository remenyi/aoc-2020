def validate_pairing(pairing):
    global lines
    for line in lines:
        if pairing[0] not in line[0] and pairing[1] in line[1]:
            return True
    return False

def valid_list():
    global lines
    valid_dict = dict()
    for line in lines:
        for i in line[0]:
            invalid_n = 0
            for a in line[1]:
                pairing = (i, a)
                if validate_pairing(pairing):
                    invalid_n += 1
            if invalid_n == len(line[1]):
                if i not in valid_dict.keys():
                    valid_dict[i] = (False, 1)
                else:
                    t = valid_dict[i]
                    valid_dict[i] = (t[0] or False, t[1]+1)
            else:
                if i not in valid_dict.keys():
                    valid_dict[i] = (True, 1)
                else:
                    t = valid_dict[i]
                    valid_dict[i] = (t[0] or True, t[1]+1)
    return valid_dict

def get_allergens():
    global lines
    allergens = set()
    for line in lines:
        allergens.update(line[1])
    return allergens

def get_valid_pairs(valid_items):
    global lines
    pairings = []
    for i in valid_items:
        l = [i]
        for a in get_allergens():
            if not validate_pairing((i, a)):
                l.append(a)
        pairings.append(l)
    pairings = sorted(pairings)
    acc = []
    flatten = lambda t: [val for sublist in t for val in sublist]
    for i in range(len(pairings)-1):
        acc.append(pairings[i][1:])
        acc = flatten(acc)
        for j in range(i+1, len(pairings)):
            for k in acc:
                if k in pairings[j]:
                    pairings[j].remove(k)
        pairings = pairings[:i+1] + sorted(pairings[i+1:], key=lambda x: len(x))
    print(pairings)
    return pairings

with open("day_21_input.txt") as ip:
    lines = [[[i.strip() for i in x.split('(')[0].strip().split(' ')], [a.strip() for a in x.split('contains')[1].strip(' )').split(',')]] for x in ip.read().splitlines()]
    valid_dict = valid_list()
    valid_pairs = get_valid_pairs([x for x in valid_dict if valid_dict[x][0]])
    valid_pairs.sort(key=lambda x: x[1])
    print("gold:", ''.join([str(x[0])+"," for x in valid_pairs])[:-1])