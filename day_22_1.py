with open("day_22_input.txt") as ip:
    block = [x for x in ip.read().split('\n\n')] 
    player_1 = [int(x) for x in block[0].splitlines() if x[0] != 'P']
    player_2 = [int(x) for x in block[1].splitlines() if x[0] != 'P']
    while player_1 != [] and player_2 != []:
        a = player_1.pop(0)
        b = player_2.pop(0)
        if a > b:
            player_1.append(a)
            player_1.append(b)
        else:
            player_2.append(b)
            player_2.append(a)
    winner_deck = player_1 if player_1 != [] else player_2
    print("silver:", sum(y*(x+1) for x, y in enumerate(reversed(winner_deck))))