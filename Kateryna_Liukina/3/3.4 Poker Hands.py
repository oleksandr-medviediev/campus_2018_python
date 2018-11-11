from functools import total_ordering
from typing import DefaultDict

def are_consecutive(numbers):
    """
    Function verify if list represents consecutive numbers.
    Args:
        numbers(list(int)): string to verify brackets
    Returns:
         bool: True if list represents consecutive numbers.
    """
    return list(range(numbers[0], numbers[-1]+1)) == numbers


def multimax(iterable, key):
    """
    Function return item with highest value of key(item)
    Args:
        key(lambda): function returns score of item
        iterable(list): list of items
    Returns:
         list: list of all maximum values.
    """
    item_scores = [(key(item), item) for item in iterable]
    max_key = None
    items = []
    for score,item in item_scores:
        if max_key == None:
            max_key = score
            items.append(item)
        elif score[0] > max_key[0]:
            max_key = score
            items.clear()
            items.append(item)
        elif score[0] == max_key[0] and score[1][0][0] > max_key[1][0][0]:
            max_key = score
            items.clear()
            items.append(item)
        elif score[0] == max_key[0] and score[1][0][0] == max_key[1][0][0]:
            items.append(item)

    return items



high_card = 1
one_pair = 2
two_pair = 3
three_of_a_kind = 4
straight = 5
flush = 6
full_house = 7
four_of_a_kind = 8
straight_flush = 9


def group_cards_by_rank(cards):
    """
    Function groups cards by rank
    Args:
        cards(list): list of card
    Returns:
         list(list): list of card lists grouped by rank.
    """
    def len_and_vals(cards):
        return len(cards), cards

    cards_by_rank = DefaultDict(list)

    for card in cards:
        cards_by_rank[card[0]].append(card)

    return sorted(cards_by_rank.values(), key=len_and_vals, reverse=True)


def get_same_rank_score(cards):
    """
    Function returns same rank score
    Args:
        cards(list): list of card
    Returns:
         tuple: score for full house, 3/4 of a kind, pairs, or high card.
    """
    rank_groups = group_cards_by_rank(cards)
    cards = []
    for l in rank_groups:
        for c in l:
            cards.append(c)
    most, second_most = len(rank_groups[0]), len(rank_groups[1])
    if most == 4:
        return tuple([four_of_a_kind, cards])
    elif most == 3:
        if second_most == 2:
            return tuple([full_house, cards])
        else:
            return tuple([three_of_a_kind, cards])
    elif most == 2:
        if second_most == 2:
            return tuple([two_pair, cards])
        else:
            return tuple([one_pair, cards])
    else:
        return tuple([high_card, cards])


def get_flush_score(cards):
    """
    Function returns flush score or None.
    Args:
        cards(list): list of card
    Returns:
         Score or None: flush score or None.
    """
    all_suits_match = len(set(c[1] for c in cards)) == 1
    if all_suits_match:
        return tuple([flush, sorted(cards, reverse=True)])


def get_straight_score(cards):
    """
    Function returns straight score or None.
    Args:
        cards(list): list of card
    Returns:
         Score or None: straight score or None.
    """
    cards = sorted(cards, reverse=True)
    values = sorted(card[0] for card in cards)
    first_val, *rest_vals = values
    first_card, *rest_cards = cards
    if first_val == 15 and are_consecutive(rest_vals):
        return tuple([straight, rest_cards + [first_card]])
    elif are_consecutive(values):
        return tuple([straight, cards])


def get_straight_flush_score(cards):
    """
    Function returns straight flush score or None.
    Args:
        cards(list): list of card
    Returns:
         Score or None: straight flush score or None.
    """
    flush_score = get_flush_score(cards)
    straight_score = get_straight_score(cards)
    if flush_score and straight_score:
        return tuple([straight_flush, straight_score[1]])


def score_hand(hand):
    """
    Function count hand score.
    Args:
        hand(tuple(str, str)): tuple of cards
    Returns:
         Score: hand score.
    """
    scores = [
        get_same_rank_score(hand),
        get_straight_score(hand),
        get_flush_score(hand),
        get_straight_flush_score(hand),
    ]
    max_item = None
    for score in scores:
        if max_item == None:
            max_item = score
        elif score and score[0] > max_item[0]:
            max_item = score

    return max_item


def poker(hands):
    """
    Function returns a list of all hands with the maximum score..
    Args:
        hands(list(str): list of hands
    Returns:
         list(tuple(str, str)): list of all hands with the maximum score..
    """
    VALUES = '23456789TJQKA'
    hands = [[(VALUES.index(card[0]) + 2,  card[1]) for card in hand] for hand in hands]
    best_hands =  [[(VALUES[card[0] - 2] + str(card[1])) for card in hand] for hand in multimax(hands, key=score_hand)]
    return best_hands
