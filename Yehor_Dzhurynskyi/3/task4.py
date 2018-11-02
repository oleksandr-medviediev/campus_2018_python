CARDS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')


def values_is_straight(values):
    """
    checks whether given values is straight
        :param list values: values of hand
        "return: whether values are straight
        :rtype: bool
    """

    bias = CARDS.index(values[0])
    is_straight = all(values[index] == CARDS[bias + index] for index in range(5))
    is_straight = is_straight or values == ['2', '3', '4', '5', 'A']

    return is_straight


def determine_hand_rank(values, suits):
    """
    determines rank of card-combination
        :param list values: values of hand
        :param list suits: suits of hand
        :return: rank of combination
        :rtype: int
    """

    is_flush = len(set(suits)) == 1
    is_straight = values_is_straight(values)
    unique_values_count = len(set(values))

    first_value_count = values.count(values[0])
    if is_straight and is_flush:
        rank = 9
    elif unique_values_count == 2:
        rank = 8 if first_value_count == 4 or first_value_count == 1 else 7
    elif is_flush:
        rank = 6
    elif is_straight:
        rank = 5
    elif unique_values_count == 3:
        rank = 4 if any(values.count(value) == 3 for value in values) else 3
    elif unique_values_count == 4:
        rank = 2
    elif unique_values_count == 5:
        rank = 1

    return rank


def determine_hand_magnitude(values):
    """
    determines hand values magnitudes
        :param list values: values of hand
        :return: sorted list of hand magnitudes
        :rtype: list
    """

    magnitudes = [CARDS.index(value) for value in reversed(values)]

    return magnitudes


def pick_best_poker_hands(hands):
    """
    determine best hand from hands collection in poker session
        :param list hands: collection of hands in poker session
        :return: best hands in poker session
        :rtype: list
    """

    ranks = []
    for hand in hands:

        cards = hand.split(' ')
        values = [card[0:-1] for card in cards]
        suits = [card[-1] for card in cards]

        values.sort(key=lambda value: CARDS.index(value))

        rank_of_hand = determine_hand_rank(values, suits)
        magnitude = determine_hand_magnitude(values)

        ranks.append(tuple((rank_of_hand, magnitude)))

    highest_rank_hands = [hand for index, hand in enumerate(hands) if ranks[index] == max(ranks)]

    return highest_rank_hands
