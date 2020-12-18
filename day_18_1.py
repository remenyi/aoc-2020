import re

def matching_parentheses(x):
    n = 0
    for i, e in enumerate(x):
        if e == '(':
            n += 1
        elif e == ')':
            n -= 1
        if n == 0:
            return i

def eval_list(l):
    if re.match(r'^\d*$', l): # if constant (recursion terminates)
        return int(l)
    if re.search(r'^\d*\s\+', l): # if addition
        exprs = l.split(' + ', 1)
        if re.match(r'^\(', exprs[1]):
            eval_sum = int(exprs[0]) + eval_list(exprs[1][:matching_parentheses(exprs[1])+1])
            rest = exprs[1][matching_parentheses(exprs[1])+1:]
            return eval_list(str(eval_sum) + rest) if rest != [] else eval_sum
        else:
            rhs = re.findall(r'^\d*', exprs[1])[0]
            res = str(int(exprs[0]) + int(rhs))
            return eval_list(res+exprs[1][len(rhs):])
    if re.search(r'^\d*\s\*', l): # if multiplication
        exprs = l.split(' * ', 1)
        if re.match(r'^\(', exprs[1]):
            eval_prod = int(exprs[0]) * eval_list(exprs[1][:matching_parentheses(exprs[1])+1])
            rest = exprs[1][matching_parentheses(exprs[1])+1:]
            return eval_list(str(eval_prod) + rest) if rest != [] else eval_prod
        else:
            rhs = re.findall(r'^\d*', exprs[1])[0]
            res = str(int(exprs[0]) * int(rhs))
            return eval_list(res+exprs[1][len(rhs):])
    if re.search(r'^\(', l): # if parentheses
        inp = l[1:matching_parentheses(l)]
        rest = l[matching_parentheses(l)+1:]
        inp_eval = eval_list(inp)
        all_eval = eval_list(str(inp_eval) + rest)
        return all_eval
    
with open("day_18_input.txt") as ip:
    lines = ip.read().splitlines()
    results = list(map(eval_list, lines))
    print("silver:", sum(results))