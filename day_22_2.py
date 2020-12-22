from copy import deepcopy

def recursive_game(deck_1, deck_2):
    game_history = []
    while deck_1 != [] and deck_2 != []:
        if (deck_1, deck_2) in game_history:
            return (deck_1, 1)
        else:
            game_history.append((deepcopy(deck_1), deepcopy(deck_2)))
        a = deck_1.pop(0)
        b = deck_2.pop(0)
        if len(deck_1) >= a and len(deck_2) >= b:
            _, round_winner = recursive_game(deck_1[:a], deck_2[:b])
            if round_winner == 1:
                deck_1.append(a)
                deck_1.append(b)
            else:
                deck_2.append(b)
                deck_2.append(a)
        elif a > b:
            deck_1.append(a)
            deck_1.append(b)
        else:
            deck_2.append(b)
            deck_2.append(a)
    return (deck_1 if deck_1 != [] else deck_2, 1 if deck_1 != [] else 2)

with open("day_22_input.txt") as ip:
    block = [x for x in ip.read().split('\n\n')] 
    deck_1 = [int(x) for x in block[0].splitlines() if x[0] != 'P']
    deck_2 = [int(x) for x in block[1].splitlines() if x[0] != 'P']
    winner_deck, _  = recursive_game(deck_1, deck_2)
    print("gold:", sum(y*(x+1) for x, y in enumerate(reversed(winner_deck))))