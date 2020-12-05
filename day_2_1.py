filename = "day_2_input.txt"
with open(filename) as f:
    lines = f.read().splitlines()
valid_pwd_count = 0
for l in lines:
    sp = l.split("-")
    min = int(sp[0])
    sp2 = str(sp[1]).split(" ")
    max = int(sp2[0])
    letter = sp2[1][0] 
    pwd = str(sp2[2])
    c_count = 0
    for c in pwd:
        if letter == c:
            c_count += 1
    if c_count >= min and c_count <= max:
        valid_pwd_count += 1
print(valid_pwd_count)   


