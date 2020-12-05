filename = "input.txt"
with open(filename) as f:
    lines = f.read().splitlines()
print("valami")
for i in range(0, len(lines)-1):
    for j in range(i+1, len(lines)):
        if int(lines[i]) + int(lines[j]) == 2020:
            print ("number: " + str(int(lines[i]) * int(lines[j])))
