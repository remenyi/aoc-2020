import re
from functools import reduce

def get_bag_no(ip, e):
    values = ip[e]
    if values[0][0] == "no other":
        return 0
    return reduce(lambda x, y: x + get_bag_no(ip, y[0])*int(y[1])+int(y[1]), values, 0)

with open("day_7_input.txt") as ip:
    rules = {re.sub("bags", "", i.split("contain")[0]).strip() : \
        [[re.sub("[0-9]*|bag(s)*", "", j).strip(" ."), re.sub("[a-zA-Z]*", "", j).strip(" .")] for j in i.split("contain")[1].split(",")] \
        for i in ip.read().splitlines()}
    print("bag no.: " + str(get_bag_no(rules, "shiny gold")))