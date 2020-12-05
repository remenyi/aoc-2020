import functools
import math

def bsp(f, p):
    if p == "F" or p == "L":
        return (f[0], math.floor((f[0]+f[1])/2))
    else:
        return (math.ceil((f[0]+f[1])/2), f[1])


with open("day_5_input.txt") as ip:
    lines = ip.read().splitlines()
    seat_ids = []
    for l in lines:
        rows = functools.reduce(bsp, l[:7], (0, 127))[0]
        cols = functools.reduce(bsp, l[-3:], (0, 7))[0]
        seat_ids.append(rows*8+cols)
    seat_ids.sort()
    for i in range(0, 7):
        if i in seat_ids:
            seat_ids.remove(i)
        if 127*8+7-i in seat_ids:
            seat_ids.remove(127*8+7-i)
    for i in range(1, len(seat_ids)):
        if seat_ids[i] - seat_ids[i-1] >= 2:
            print("my seat id: " + str(seat_ids[i]-1))