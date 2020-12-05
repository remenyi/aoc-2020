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
    if (pwd[min-1] == letter) != (pwd[max-1] == letter):
        valid_pwd_count += 1
print(valid_pwd_count)   

