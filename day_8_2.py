import copy

def find_loop(program):
    acc = 0
    pc = 0
    pcs = []
    while pc not in pcs:
        pcs.append(pc)
        instruction = program[pc].get("ins")
        value = program[pc].get("val")
        if instruction == "nop":
            pc += 1
        elif instruction == "acc":
            acc += value
            pc += 1
        elif instruction == "jmp":
            pc += value
    return {"pc": pc, "acc": acc, "pcs": pcs}

def run_p(program):
    acc = 0
    pc = 0
    pcs = []
    while (pc not in pcs) and (pc < len(program)):
        pcs.append(pc)
        instruction = program[pc].get("ins")
        value = program[pc].get("val")
        if instruction == "nop":
            pc += 1
        elif instruction == "acc":
            acc += value
            pc += 1
        elif instruction == "jmp":
            pc += value
    return {"res" : pc >= len(program), "acc" : acc}

with open("day_8_input.txt") as ip:
    program = [{"ins" : i[0:3], "val": int(i[3:])} for i in ip.read().splitlines()]
    pcs = find_loop(program)["pcs"]
    i = len(pcs)-1
    new_program = program.copy()
    while not run_p(new_program)["res"]:
        new_program = copy.deepcopy(program)
        if new_program[pcs[i]]["ins"] == "nop":
            new_program[pcs[i]]["ins"] = "jmp"
        if new_program[pcs[i]]["ins"] == "jmp":
            new_program[pcs[i]]["ins"] = "nop"
        i -= 1
    print("acc: " + str(run_p(new_program)["acc"]))