import re
import functools
import operator

def get_bag_no(ip, e):
    values = ip[e]
    if values[0][0] == "no other":
        return 0
    no = 0
    for l in values:
        no += get_bag_no(ip, l[0])*int(l[1])+int(l[1])
    return no

with open("day_7_input.txt") as ip:
    rules = {re.sub("bags", "", i.split("contain")[0]).strip() : \
        [[re.sub("[0-9]*|bag(s)*", "", j).strip(" ."), re.sub("[a-zA-Z]*", "", j).strip(" .")] for j in i.split("contain")[1].split(",")] \
        for i in ip.read().splitlines()}
    print(get_bag_no(rules, "shiny gold"))