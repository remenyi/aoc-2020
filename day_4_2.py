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
                pred = False
                if e == "byr" and len(l[e]) == 4 and int(l[e]) and int(l[e]) >= 1920 and int(l[e]) <= 2002:
                    pred = True
                if e == "iyr" and len(l[e]) == 4 and int(l[e]) and int(l[e]) >= 2010 and int(l[e]) <= 2020:
                    pred = True
                if e == "eyr" and len(l[e]) == 4 and int(l[e]) and int(l[e]) >= 2020 and int(l[e]) <= 2030:
                    pred = True
                if e == "hgt" and (l[e][-2:] == "cm" or l[e][-2:] == "in"):
                    if l[e][-2:] == "cm" and int(l[e][:-2]) and int(l[e][:-2]) >= 150 and int(l[e][:-2]) <= 193:
                        pred = True
                    if l[e][-2:] == "in" and int(l[e][:-2]) and int(l[e][:-2]) >= 59 and int(l[e][:-2]) <= 76:
                        pred = True
                if e == "hcl" and l[e][0] == '#' and len(l[e]) == 7:
                    numbers = []
                    for i in range(10):
                        numbers.append(str(i))
                    characters = ["a", "b", "c", "d", "e", "f"]
                    p = True
                    for i in l[e][1:]:
                        if i not in numbers and i not in characters:
                            p = False
                    if p:        
                        pred = True
                if e == "ecl" and l[e] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    pred = True
                if e == "pid" and len(l[e]) == 9:
                    pred = True
                if pred:
                    count += 1
                    print(e + " valid:\t" + l[e])
                else:
                    print(e + " invalid:\t" + l[e])
        print("\n")
        if count == len(valid):
            v_count += 1
            #print("valid: " + str(l))
        #else:
            #print("invalid: " + str(l))
    return v_count



with open("day_4_input.txt") as ip:
    lines = ip.read().splitlines()
    print("valid count: " + str(check_valid(parse(lines))))
