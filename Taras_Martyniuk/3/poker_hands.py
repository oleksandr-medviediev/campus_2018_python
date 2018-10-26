# span 
HighCard, Pair, TwoPair, Three, Straight, Flush, FullHouse, Four, StraightFlush, Five = range(10)

ranks = {
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 14
}


def parse_card(card):
    """
        parses hand from string to tuples of rank and suit,
        non-digit ranks are parsed into digit counterparts

        :param hand: string in form [Rank-Int][Suit Char]
        :returns: list of tuples
    """
    rank_char = card[0]
    res = None
    
    if rank_char in ranks:
        assert len(card) == 2
        res = ranks[rank_char], card[1]

    elif rank_char == '1':
        assert len(card) == 3
        res = (int(card[0:2]) , card[2])

    else:
        assert len(card) == 2
        res = int(rank_char), card[1]
    
    return res


def get_hand_type(hand):
    """
        gets poker combination type from hand string

        :param hand: string listing the card in form [Rank-Int][Suit Char]
        :returns: poker hand enum
    """
    cards = map(parse_card, hand.split(' '))

    for card in cards:
        print(card)

    print('\n\n')

    return HighCard


def get_upper_hand(hands):
    """
        :param: list of strings denoting poker hands
        "returns: highest rank hand
    """
    types = [get_hand_type(h) for h in hands]
    max_hand_type = max(types)

    max_type_hand_indices = [i for i, t in enumerate(types) if t == max_hand_type]
    # if more than one, compare between hands



    
hands = ["10D 5S 6S 8D 3C",
         "2S 4C 7S 9H 10H",
         "7S 7C 7H 9D 9H",
         "3S 4S 5D 6H JH"]



get_upper_hand(hands)

