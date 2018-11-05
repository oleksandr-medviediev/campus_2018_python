def is_hand_flush(hand):
    """
    Checks if combination of cards is flush

    :param hand: hand of cards
    :return: combination of cards is flush
    :rtype: bool
    """

    suits = {
        'd': 0,
        's': 0,
        'c': 0,
        'h': 0
    }

    is_flush = False
    cards = hand.split(' ')

    for card in cards:
        suits[card[-1]] += 1

    for suit in suits.keys():
        if suits[suit] == 5:
            is_flush = True
            break

    return is_flush


def get_card_rank(card):
    """
    Gets string that describes a card, returns integer representation of cards rank

    :param card: string representing a card: rank and suit letters
    :return: integer representation of a rank: 2 to 14(higher is better)
    :rtype: int
    """

    highest_ranks = {
        'a': 14,
        'k': 13,
        'q': 12,
        'j': 11,
    }

    try:
        rank = int(card[:-1])

    except ValueError:
        rank = highest_ranks[card[:-1]]

    return rank


def get_hand_rank_value(hand):
    """
    Returns tuple of hand category(from 1 to 9(higher is better) and it's integer value(higher is better)

    :param hand: string with cards
    :return: rank and value
    :rtype: tuple
    """

    value = 0
    occurrences = {}

    categories = {
        'straight flush': 9,
        'four of a kind': 8,
        'full house': 7,
        'flush': 6,
        'straight': 5,
        'three of a kind': 4,
        'two pair': 3,
        'one pair': 2,
        'high card': 1
    }

    is_flush = is_hand_flush(hand)
    cards = hand.split(' ')

    for card in cards:
        rank = get_card_rank(card)

        try:
            occurrences[rank] += 1

        except KeyError:
            occurrences.setdefault(rank, 1)

    pair_found = False
    two_pairs_found = False
    three_of_a_kind_found = False

    for key in occurrences.keys():

        if occurrences[key] == 4:
            rank = categories['four of a kind']
            value = key * 4
            break

        elif occurrences[key] == 3:
            value += key * 3

            if pair_found:
                rank = categories['full house']
                break
            else:
                three_of_a_kind_found = True

        elif occurrences[key] == 2:
            value += key * 2

            if three_of_a_kind_found:
                rank = categories['full house']
                break

            elif pair_found:
                two_pairs_found = True

            else:
                pair_found = True

    else:
        keys = list(occurrences.keys())
        keys.sort()

        is_straight = all(f == s for f, s in enumerate(keys, keys[0]))

        if is_flush and is_straight:
            rank = categories['straight flush']
            value = sum(keys)

        elif is_flush:
            rank = categories['flush']
            value = sum(keys)

        elif is_straight:
            rank = categories['straight']
            value = sum(keys)

        elif three_of_a_kind_found:
            rank = categories['three of a kind']

        elif two_pairs_found:
            rank = categories['two pair']

        elif pair_found:
            rank = categories['one pair']

        else:
            rank = categories['high card']
            value = max(keys)

    result = (rank, value)
    return result


def pick_best_poker_hands(hands):
    """
    Pick the best hand(s) from a list of poker hands

    :param hands: list of hands
    :return: best hand(s)
    :rtype: list
    """

    priced_hands = []
    total_priced = {}

    for hand in hands:
        rank_and_value = get_hand_rank_value(hand.lower())
        total_priced.setdefault(rank_and_value, [])

        priced_hands.append(rank_and_value)
        total_priced[rank_and_value].append(hand)

    priced_hands.sort(reverse=True)
    best_hands = total_priced[priced_hands[0]]

    return best_hands


if __name__ == "__main__":
    hands_list = ["4D 5d 6d 8D 7d",
                  "4s 5s 6s 8s 7s",
                  "9D 5d 6d 8D 7d",
                  "3S 4S 5D 6H 2H",
                  "3S 4S 5D 6H JH",
                  "2c 4C 7c 9c 10c",
                  "jS 4S 4D 4H jH",
                  "3H 3H 3C 3C JD"]
    res = pick_best_poker_hands(hands_list)
    print(res)
