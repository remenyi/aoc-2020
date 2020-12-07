import re

def get_keys(ip, e):
    out = []
    for k in ip:
        if e in ip[k]:
            out.append(k)
    return out

def get_containers(ip, e):
    containers = get_keys(ip, e)
    if containers == []:
        return set()
    containers = set(containers)
    new_containers = set()
    for l in containers:
        new_containers.update(get_containers(ip, l))
    containers.update(new_containers)
    return containers

with open("day_7_input.txt") as ip:
    rules = {re.sub("bags", "", i.split("contain")[0]).strip() : \
        [re.sub("[0-9]*|bag(s)*", "", j).strip(" .") for j in i.split("contain")[1].split(",")] \
        for i in ip.read().splitlines()}
    print(len(get_containers(rules, "shiny gold")))