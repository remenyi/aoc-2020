from re import match, findall

def l_to_s(l):
    return ''.join(map(str, l))

def make_regex(rule):
    global rules
    if rule == 11:
        return "@" # for splitting the regex
    if rules[rule] == 'a' or rules[rule] == 'b':
        return rules[rule] 
    if '|' in rules[rule]:
        paths = [x.strip() for x in rules[rule].split('|')]
        results = []
        for path in paths:
            new_rules = [int(x) for x in path.split(' ')]
            path_results = list(map(lambda x : make_regex(x) 
                                                if x != rule 
                                                else '+', new_rules))
            results.append(l_to_s(path_results) + '|')
        results[-1] = results[-1][:-1] # removing last '|'
        return "(" + l_to_s(results) + ")" if rule != 11 else "(" + l_to_s(results) + ")"
    else:
        new_rules = [int(x) for x in rules[rule].split(' ')]
        results = list(map(make_regex, new_rules))
        return l_to_s(results)

def tl_to_l(tl):
    return [tuple(j for j in i if j)[0] for i in tl]

def validate(line, front, back, regex_42, regex_31):
    results = []
    for i in range(1, 10): # magic number, I don't know how deep the nesting should go
        new_regex = front+(regex_42*i)+(regex_31*i)+back
        results.append(bool(match(new_regex, line)))
    return True in results

with open("day_19_input_2.txt") as ip:
    blocks = [x for x in ip.read().split('\n\n')]
    rules = {int(x.split(':')[0]) : x.split(':')[1].strip(' "') for x in blocks[0].splitlines()}
    messages = [x for x in blocks[1].splitlines()]
    regex_str = r"^" + make_regex(0) + r"$"
    r_split = regex_str.split('@')
    rule_42 = make_regex(42); rule_31 = make_regex(31)
    valid_messages = list(filter(lambda x: validate(x, r_split[0], r_split[1], rule_42, rule_31), messages))
    print("silver:", len(valid_messages))