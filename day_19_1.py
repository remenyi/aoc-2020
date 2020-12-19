from re import match

def l_to_s(l):
    return ''.join(map(str, l))

def make_regex(rule):
    global rules
    if rules[rule] == 'a' or rules[rule] == 'b':
        return rules[rule] 
    if '|' in rules[rule]:
        paths = [x.strip() for x in rules[rule].split('|')]
        results = []
        for path in paths:
            new_rules = [int(x) for x in path.split(' ')]
            path_results = list(map(make_regex, new_rules))
            results.append(l_to_s(path_results) + '|')
        results[-1] = results[-1][:-1] # removing last '|'
        return "(" + l_to_s(results) + ")"
    else:
        new_rules = [int(x) for x in rules[rule].split(' ')]
        results = list(map(make_regex, new_rules))
        return l_to_s(results)

with open("day_19_input_2.txt") as ip:
    blocks = [x for x in ip.read().split('\n\n')]
    rules = {int(x.split(':')[0]) : x.split(':')[1].strip(' "') for x in blocks[0].splitlines()}
    messages = [x for x in blocks[1].splitlines()]
    regex_str = r"^" + make_regex(0) + r"$"
    print(regex_str)
    valid_messages = list(filter(lambda x: match(regex_str, x), messages))
    print("silver:", len(valid_messages))