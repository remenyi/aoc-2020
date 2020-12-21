
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

with open("day_21_input.txt") as ip:
    lines = [[[i.strip() for i in x.split('(')[0].strip().split(' ')], [a.strip() for a in x.split('contains')[1].strip(' )').split(',')]] for x in ip.read().splitlines()]
    valid_dict = valid_list()
    print("silver:", sum([valid_dict[x][1] for x in valid_dict if not valid_dict[x][0]]))