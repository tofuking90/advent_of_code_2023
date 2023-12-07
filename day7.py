##### Day 7 #####
from collections import Counter
import numpy as np

cdict = {'A':14,'K':13,'Q':12,'J':11,'T':10}
def parse_hand(hand, cdict):
    hand_out = []
    for card in hand:
        hand_out.append(cdict[card] if card in 'AKQJT' else int(card))
    return np.array(hand_out)

hands = []
bids = []
with open("day7.txt","r") as f:
    for line in f:
        hands.append(line[:5])
        bids.append(int(line.rstrip('\n')[5:]))

hand_bids = []
for hand, bid in zip(hands,bids):
    # 5 of a kind, 4 of a kind, full house, trips, two pair, pair, high card
    phand = parse_hand(hand,cdict)
    enum = sorted(Counter(phand).values())
    if enum == [5]:
        hand_bids.append(list(phand+10**7)+[bid])
    elif enum == [1,4]:
        hand_bids.append(list(phand+10**6)+[bid])
    elif enum == [2,3]:
        hand_bids.append(list(phand+10**5)+[bid])
    elif enum == [1,1,3]:
        hand_bids.append(list(phand+10**4)+[bid])
    elif enum == [1,2,2]:
        hand_bids.append(list(phand+10**3)+[bid])
    elif enum == [1,1,1,2]:
        hand_bids.append(list(phand+10**2)+[bid])
    else:
        hand_bids.append(list(phand)+[bid])

print(sum([x[-1]*y for x,y in zip(sorted(hand_bids),range(1,len(hands)+1))]))

### 7b
cdict_joker = {'A':14,'K':13,'Q':12,'J':1,'T':10}

hands = []
bids = []
with open("day7.txt","r") as f:
    for line in f:
        hands.append(line[:5])
        bids.append(int(line.rstrip('\n')[5:]))

hand_bids = []
for hand, bid in zip(hands,bids):
    # 5 of a kind, 4 of a kind, full house, trips, two pair, pair, high card
    num_jokers = hand.count('J')
    if num_jokers == 5:
        enum = [5]
    else:
        no_joker_hand = hand.replace('J','')
        p_no_joker_hand = parse_hand(no_joker_hand,cdict_joker)
        enum = sorted(Counter(p_no_joker_hand).values())
        enum[-1] += num_jokers
    phand = parse_hand(hand,cdict_joker)
    if enum == [5]:
        hand_bids.append(list(phand+10**7)+[bid])
    elif enum == [1,4]:
        hand_bids.append(list(phand+10**6)+[bid])
    elif enum == [2,3]:
        hand_bids.append(list(phand+10**5)+[bid])
    elif enum == [1,1,3]:
        hand_bids.append(list(phand+10**4)+[bid])
    elif enum == [1,2,2]:
        hand_bids.append(list(phand+10**3)+[bid])
    elif enum == [1,1,1,2]:
        hand_bids.append(list(phand+10**2)+[bid])
    else:
        hand_bids.append(list(phand)+[bid])

print(sum([x[-1]*y for x,y in zip(sorted(hand_bids),range(1,len(hands)+1))]))
