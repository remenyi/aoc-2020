from math import prod

def validate(x):
    valid = True
    for e in x:
        valid_e = False
        for k in ranges:
            if ranges[k][0][0] <= e <= ranges[k][0][1] or ranges[k][1][0] <= e <= ranges[k][1][1]:
                valid_e = True
        valid = valid and valid_e
    return x if valid else None

def get_idxes(x):
    valid_idxs = []
    for i in range(len(tickets[0])):
        valid = True
        for ticket in valid_tickets:
            if not (x[0][0] <= ticket[i] <= x[0][1] or x[1][0] <= ticket[i] <= x[1][1]):
                valid = False
        if valid:
            valid_idxs.append(i)
    return valid_idxs

def narrow_idx(idx_ks):
    ret = set(field_idxes[idx_ks[0]])
    for idxes in idx_ks[1:]:
        ret -= (set(field_idxes[idxes]))
    return list(ret)[0]

with open("day_16_input.txt") as ip:
    blocks = [x for x in ip.read().split("\n\n")]
    ranges = {x.split(':')[0] : [(int(y.strip().split('-')[0]), int(y.strip().split('-')[1])) for y in x.split(':')[1].split('or')] for x in blocks[0].splitlines()}
    my_ticket = [int(x) for x in blocks[1].splitlines()[1].split(',')]
    tickets = [[int(y) for y in x.split(',')] for x in blocks[2].splitlines()[1:]]
    tickets.append(my_ticket)
    valid_tickets = list(filter(validate, tickets))
    field_idxes = {f : get_idxes(ranges[f])  for f in ranges}
    field_idxes_sorted = sorted(field_idxes, key=lambda x: len(field_idxes[x]), reverse=True)
    narrowed_idx = {f : narrow_idx(field_idxes_sorted[field_idxes_sorted.index(f):])  for f in field_idxes_sorted}
    depart_fields = list(filter(lambda x: x.startswith("departure"), narrowed_idx))
    depart_my_ticket = list(map(lambda x: my_ticket[narrowed_idx[x]], depart_fields))
    print("gold:", prod(depart_my_ticket))