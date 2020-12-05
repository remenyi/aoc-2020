def parse(ip):
    out = []
    i = 0
    d = {}
    while i < len(ip):
        if len(ip[i]) == 0:
            out.append(d)
            d = {}
            i += 1
        sp = ip[i].split(" ")
        l = list(map(lambda i: (i.split(":")), sp))
        for e in l:
            d[e[0]] = e[1]
        i += 1    
    out.append(d)
    return out

def check_valid(ip):
    valid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    v_count = 0
    for l in ip:
        count = 0
        for e in l:
            if e in valid:
                count += 1
        if count == len(valid):
            v_count += 1
    return v_count



with open("day_4_input.txt") as ip:
    lines = ip.read().splitlines()
    print(parse(lines))
    print(check_valid(parse(lines)))
