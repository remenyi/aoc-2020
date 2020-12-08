with open("day_8_input.txt") as ip:
    program = [{"op" : i[0:3], "val" : int(i[3:])} for i in ip.read().splitlines()]
    acc = 0
    pc = 0
    pcs = []
    while pc not in pcs:
        pcs.append(pc)
        instruction = program[pc]["op"]
        value = program[pc]["val"]
        if instruction == "nop":
            pc += 1
        elif instruction == "acc":
            acc += value
            pc += 1
        elif instruction == "jmp":
            pc += value
    print("acc: " + str(acc))