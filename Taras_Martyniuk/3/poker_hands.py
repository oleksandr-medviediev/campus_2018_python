from itertools import groupby
from collections import Counter


"""
    poker hand types
"""
HighCard, Pair, TwoPair, Three, Straight, Flush, FullHouse, Four, StraightFlush, RoyalFlush = range(10)

high_ranks = {
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 14
}

suits = {'D', 'S', 'C', 'H'}
HAND_SIZE = 5


def most_common(collection):
    """
        returns the most frequently encountered element 
    """
    data = Counter(collection)
    return max(collection, key=data.get)


def parse_card(card):
    """
        parses hand from string to tuples of rank and suit,
        non-digit ranks are parsed into digit counterparts

        :param hand: string in form [Rank-Int][Suit Char]
        :returns: list of tuples
    """
    rank_char = card[0]
    res = None
    
    if rank_char in high_ranks:
        assert len(card) == 2
        res = high_ranks[rank_char], card[1]

    elif rank_char == '1':
        assert len(card) == 3
        res = (int(card[0:2]) , card[2])

    else:
        assert len(card) == 2
        res = int(rank_char), card[1]

    if res[1] not in suits:
        raise "Wrong suit char"
    
    return res


def get_hand_type(hand):
    """
        gets poker combination type from hand string

        :param hand: string listing the card in form [Rank-Int][Suit Char]
        :returns: poker hand enum
    """
    cards = map(parse_card, hand.split(' '))
    ranks, suits = zip(*cards)
    assert len(ranks) == 5 and len(suits) == 5
    ranks = list(ranks)
    ranks.sort()

    counter = Counter(ranks)
    commonnest_rank_count = counter.most_common(1)[0][1]
    second_commonnest_rank_count = counter.most_common(2)[1][1]

    is_straight = ranks[-1] - ranks[0] == HAND_SIZE - 1
    is_flush = len(set(suits)) == 1

    hand_type = -1

    if is_straight and is_flush:
        royal_start = 10
        hand_type = RoyalFlush if ranks[0] == royal_start else StraightFlush

    elif commonnest_rank_count == 4:
        hand_type = Four
    
    elif commonnest_rank_count == 3 and second_commonnest_rank_count == 2:
        hand_type = FullHouse

    elif is_flush:
        hand_type = Flush

    elif is_straight:
        hand_type = Straight

    elif commonnest_rank_count == 3:
        hand_type = Three
    
    elif commonnest_rank_count == 2:
        hand_type = TwoPair if second_commonnest_rank_count == 2 else Pair

    else:
        hand_type = HighCard

    return hand_type


def get_upper_hand(hands):
    """
        :param: list of strings denoting poker hands
        "returns: highest rank hand
    """
    types = [get_hand_type(h) for h in hands]
    max_hand_type = max(types)
    max_type_hand_indices = [i for i, t in enumerate(types) if t == max_hand_type]
    
    return [hands[i] for i in max_type_hand_indices] 


hands = ["10D QS 6S 8D 3C", # high
         "2S 4C 7S 10S 10H", # pair
         "3S 3D 3C 9H 9S", # full house
         "10S JS QS KS AS"] # royal flush



print(get_upper_hand(hands))

