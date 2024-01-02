from pelib.basic import timed

def process_hand(hand):
    mapper = {'A': 14, 'T': 10, 'J': 11, 'Q': 12, 'K': 13} | {str(x): x for x in range(2, 10)}
    hand = sorted([(mapper[x[0]], x[1]) for x in hand])
    flush = 1 if all([hand[0][1] == x[1] for x in hand]) else 0
    straight = 1 if all([hand[i][0] + 1 == hand[i + 1][0] for i in range(len(hand) - 1)]) else 0
    if hand[0][0] == 1 and hand[4][0] == 13:
        straight = 2 if all([hand[i][0] + 1 == hand[i + 1][0] for i in range(1, len(hand) - 1)]) else 0      
    if straight == 2 and flush: 
        return (10, 14 if hand[0][0] == 1 else hand[4][0])
    if straight and flush:
        return (9, hand[4][0])
    if flush:
        return (6, hand[4][0])
    if straight == 2:
        return (5, 14)
    if straight:
        return (5, hand[4][0])
    counts = {}
    for card in hand:
        if not counts.get(card[0], False):
            counts[card[0]] = 0
        counts[card[0]] += 1
        if counts[card[0]] == 4:
            return (8, 14 if card[0] == 1 else card[0])
    
    for card in counts:
        if counts[card] == 3:
            if len(counts) == 2:
                return (7, 14 if card == 1 else card)
            else:
                return (4, 14 if card == 1 else card)
    
    max_ = 0
    for card in counts:
        if counts[card] == 2:
            if card > max_:
                max_ = 14 if card == 1 else card
    if max_:
        if len(counts) == 3:
            return (3, max_)
        else:
            return (2, max_)
    return (1, 14 if hand[0][0] == 1 else hand[4][0])
    
    

@timed
def process():
    hands = open("input.txt").read().split("\n")
    hands = [(x.split(" ")[:5], x.split(" ")[5:]) for x in hands]
    count = 0
    for hand in hands:
        score_one = process_hand(hand[0])
        score_two = process_hand(hand[1])
        if score_one[0] > score_two[0]:
            count += 1
        elif score_one[0] < score_two[0]:
            continue
        else:
            if score_one[1] > score_two[1]:
                count += 1
    return count

process()