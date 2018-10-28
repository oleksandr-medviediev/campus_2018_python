m_cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
    "F": 15,  # joker
}


def get_highest(values, types=None):
    """
    Args:
        values (list): list of int of values.

    Returns:
        Highest value.
    """
    cvalues = values.copy()
    cvalues.sort()
    return cvalues[-1]


def is_fiveofakind(values, types):
    """
    Args:
        values (list): list of int of card values.
        types (list): list of card types.

    Returns:
        Value = V1 if cards: T1:V0, T2:V0, T3:V0, T4:V0, T0:V1.
        False otherwise.
    """
    # as Joker is max val - don;t need to check the order
    for i in values[:-1]:
        if i != values[0]:
            return False
    return values[-1] if values[-1] == m_cards['F'] else False


def is_straight(values, types):
    """
    Args:
        values (list): list of int of card values.
        types (list): list of card types.

    Returns:
        Value = V0 if cards: Tany:V0, Tany:V0 - 1, ..., Tany:V0 - 4.
        False otherwise.
    """
    for el, i in enumerate(values):
        if el + i != values[0]:
            return False
    return values[0]


def is_straightflush(values, types):
    """
    Args:
        values (list): list of int of card values.
        types (list): list of card types.

    Returns:
        Value = V0 if cards: T0:V0, T0:V0 - 1, ..., T0:V0 - 4.
        False otherwise.
    """
    if types.count(types[0]) != 5:
        return False
    return is_straight(values, types)


def is_fourofakind(values, types):
    """
    Args:
        values (list): list of int of card values.
        types (list): list of card types.

    Returns:
        Value = any: V if cards: T0:V1, T1:V1, T2:V1, T3:V1, anyt:anyv, anyv > V1.
        False otherwise.
    """
    for i in values[:-1]:
        if i != values[0]:
            return False
    return values[-1] if values[-1] != m_cards['F'] else False


def is_fullhouse(cvalues, types):
    """
    Args:
        values (list): list of int of card values.
        types (list): list of card types.

    Returns:
        Value = any: V if cards: T0:V0, T1:V0, T3:V0, Ti:V1, Tj:V1.
        False otherwise.
    """
    values = cvalues.copy()
    if values.count(values[0]) != 2 and values.count(values[0]) != 3:
        return False

    values.sort()
    if values[0] == values[1] and values[1] == values[2]:
        if values[3] == values[4]:
            return values[0] if values[0] > values[1] else values[3]
        else:
            return False
    elif values[0] == values[1]:
        if values[2] == values[3] == values[4]:
            return values[0] if values[0] > values[1] else values[3]
        else:
            return False
    return False


def is_flush(values, types):
    """
    Args:
        values (list): list of int of card values.
        types (list): list of card types.

    Returns:
        Value = highest value if all of same type.
        False otherwise.
    """
    if types.count(types[0]) != 5:
        return False
    return get_highest(values)


def is_threeofakind(values, types):
    """
    Args:
        values (list): list of int of card values.
        types (list): list of card types.

    Returns:
        Value = highest value if there are three same values.
        False otherwise.
    """
    mset = set(values)
    if len(mset) == 2:
        return get_highest(values)
    return False


def is_twopair(values, types):
    """
    Args:
        values (list): list of int of card values.
        types (list): list of card types.

    Returns:
        Value = highest value if there are two pairs.
        False otherwise.
    """
    mset = set(values)
    pair_count = 0
    for i in mset:
        if values.count(i) == 2:
            pair_count += 1
    return get_highest(values) if pair_count == 2 else False


def is_pair(values, types):
    """
    Args:
        values (list): list of int of card values.
        types (list): list of card types.

    Returns:
        Value = highest value if there is pair.
        False otherwise.
    """
    mset = set(values)
    for i in mset:
        if values.count(i) == 2:
            return get_highest(values)
    return False


def filter_cards(mstr):
    """
    Args:
        mstr (str): string of cards.
    Returns:
        (Values, Types).
    """
    mlist = mstr.split()
    values = [m_cards[i[:-1]] for i in mlist]
    types = [i[-1:] for i in mlist]
    return (values, types)


def pick_best_poker_hands(hands):
    """
    Picks best hand among given. Hand consists of 5 cards, has template: 
    ValueCode:Type, value codes from m_cards dictionary, Type - D,S,H,C.

    Args:
        hands (list): list of hands.

    Returns:
        None
    """

    functions = [is_fiveofakind, is_straightflush, is_fourofakind, is_fullhouse, 
        is_flush, is_straight, is_threeofakind, is_twopair, is_pair, get_highest]
    labels = ["five of a kind", "straight flush", "4 of a kind", "full house",
        "flush", "straight", "3 of a kind", "2 pair", "1 pair", "not your day, no combo"]

    lowest_index = len(functions)
    highest_score = -1
    winner_hand = None
    for hand in hands:
        mcontainer = filter_cards(hand)

        # Couldn't get it to work with enumerate
        i = 0
        for func in functions:
            res = func(mcontainer[0], mcontainer[1])

            if res is not False:
                # if 2 same values - picks last
                if lowest_index > i:
                    lowest_index = i
                    winner_hand = hand
                elif lowest_index == i and highest_score < res:
                    lowest_index = i
                    winner_hand = hand

                print(labels[i])
                print(res)
                break
            i += 1


    print("Winner is: ")
    print(winner_hand)


hands = ["4D 5S 6S 8D 3C",
"2S 4C 7S 9H 10H",
"3S 4S 5D 6H JH"]
pick_best_poker_hands(hands)
        