hex_map = {
    "2": "0", "3": "1", "4": "2", "5": "3", "6": "4", "7": "5", "8": "6", "9": "7", "T": "8", "J": "9", "Q": "A", "K": "B", "A": "C"
}

def rank_hand(item):
    """Generates a unique rank for a poker hand"""
    hand = item[0]
    value = ""
    composition = {
        "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "T": 0, "J": 0, "Q": 0, "K": 0, "A": 0
    }
    for card in hand:
        value += hex_map[card]
        composition[card] += 1
    # 5 of a kind
    if any([composition[card] == 5 for card in composition]): rank = 7
    # 4 of a kind
    elif any([composition[card] == 4 for card in composition]): rank = 6
    elif any([composition[card] == 3 for card in composition]):
        # Full house
        if any([composition[card] == 2 for card in composition]): rank = 5
        # 3 of a kind
        else: rank = 4
    elif any([composition[card] == 2 for card in composition]):
        # 2 pairs
        if sum([composition[card] == 2 for card in composition]) == 2: rank = 3
        # 1 pair
        else: rank = 2
    # High card
    else: rank = 1
    return int(str(rank) + value, 13)

with open("input.txt") as f:
    total = 0
    hands = []
    for line in f.readlines():
        hands.append(line.rstrip().split(" "))
    hands.sort(key=rank_hand)
    for i, (hand, bid) in enumerate(hands):
        total += (i + 1) * int(bid)

print(total)
