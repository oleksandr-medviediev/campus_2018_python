CARD_RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a')

COMBINATION_NAMES = ('High card', 'One pair', 'Two pairs',
                     'Three of a kind', 'Straight', 'Flush',
                     'Full house', 'Four of a kind', 'Straight flush')


def parse_hand(hand):
    """
    Return parsed hand.

    :param hand: hand to parse.
    :type hand: str.

    :return: parsed hand (rank, suite).
    :rtype: tuple(int, str).
    """
    parsed_hand = []

    hand = hand.lower()
    hand = hand.split()

    for card in hand:
        parsed_hand.append((CARD_RANKS.index(card[:-1]), card[-1]))

    return parsed_hand


def is_straight_flush(hand):
    """
    Return True if hand holds Straight Flush combination, False otherwise.

    :param hand: parsed hand.
    :type hand: tuple(int, str).

    :return: True if hand holds Straight Flush combination, False otherwise.
    :rtype: bool.
    """
    return is_straight(hand) and is_flush(hand)


def is_four_of_a_kind(hand):
    """
    Return True if hand holds Four of a Kind combination, False otherwise.

    :param hand: parsed hand.
    :type hand: tuple(int, str).

    :return: True if hand holds Four of a Kind combination, False otherwise.
    :rtype: bool.
    """
    result = False

    ranks = [card[0] for card in hand]

    for rank in ranks:

        if ranks.count(rank) == 4:

            result = True
            break

    return result


def is_full_house(hand):
    """
    Return True if hand holds Full House combination, False otherwise.

    :param hand: parsed hand.
    :type hand: tuple(int, str).

    :return: True if hand holds Full House combination, False otherwise.
    :rtype: bool.
    """
    result = True

    ranks = [card[0] for card in hand]

    for rank in ranks:

        if ranks.count(rank) != 3 and ranks.count(rank) != 2:

            result = False
            break

    return result


def is_flush(hand):
    """
    Return True if hand holds Flush combination, False otherwise.

    :param hand: parsed hand.
    :type hand: tuple(int, str).

    :return: True if hand holds Flush combination, False otherwise.
    :rtype: bool.
    """
    result = True
    suite = hand[0][1]

    for card in hand:

        if card[1] != suite:

            result = False
            break

    return result


def is_straight(hand):
    """
    Return True if hand holds Straight combination, False otherwise.

    :param hand: parsed hand.
    :type hand: tuple(int, str).

    :return: True if hand holds Straight combination, False otherwise.
    :rtype: bool.
    """
    result = True

    ranks = [card[0] for card in hand]
    ranks.sort()

    for index, rank in enumerate(ranks):

        if index < len(ranks) - 1 and ranks[index + 1] - rank != 1:

            result = False
            break

    return result


def is_three_of_a_kind(hand):
    """
    Return True if hand holds Three of a Kind combination, False otherwise.

    :param hand: parsed hand.
    :type hand: tuple(int, str).

    :return: True if hand holds Three of a Kind combination, False otherwise.
    :rtype: bool.
    """
    result = False
    ranks = [card[0] for card in hand]

    for rank in ranks:

        if ranks.count(rank) == 3:

            result = True
            break

    return result


def is_two_pairs(hand):
    """
    Return True if hand holds Two Pairs combination, False otherwise.

    :param hand: parsed hand.
    :type hand: tuple(int, str).

    :return: True if hand holds Two Pairs combination, False otherwise.
    :rtype: bool.
    """
    ranks = [card[0] for card in hand]

    number_of_cards_in_pair = 0

    for rank in ranks:

        if ranks.count(rank) == 2:

            number_of_cards_in_pair += 1

    return number_of_cards_in_pair == 4


def is_pair(hand):
    """
    Return True if hand holds One Pair combination, False otherwise.

    :param hand: parsed hand.
    :type hand: tuple(int, str).

    :return: True if hand holds One Pair combination, False otherwise.
    :rtype: bool.
    """
    result = False
    ranks = [card[0] for card in hand]

    for rank in ranks:

        if ranks.count(rank) == 2:

            result = True
            break

    return result


def is_high_card(hand):
    """
    Always returns True, because any poker hand holds High Card combination.

    :param hand: unused.

    :return: True.
    :rtype: bool.
    """
    return True


def determine_highest_card(hand):
    """
    Return rank of the highest card in the hand.

    :param hand: parsed hand.
    :type hand: tuple(int, str).

    :return: rank of the highest card in the hand.
    :rtype: int.
    """
    highest_rank = 0

    for card in hand:

        highest_rank = max(highest_rank, card[0])

    return highest_rank


def rate_hand_by_combinations(hand):
    """
    Return rank of the highest combination, held by the hand.

    :param hand: parsed hand.
    :type hand: tuple(int, str).

    :return: rank of the highest combination, held by the hand.
    :rtype: int.
    """
    functions = (is_high_card, is_pair, is_two_pairs,
                 is_three_of_a_kind, is_straight, is_flush,
                 is_full_house, is_four_of_a_kind, is_straight_flush)

    for i in reversed(range(len(functions))):

        if functions[i](hand):
            return i

    return 0


def determine_best_hands(hand_ratings):
    """
    Return best poker hands in hand_ratings.

    :param hand_ratings: dict of hands and their ratings.
    :type hand_ratings: dict{str: int}.

    :return: best poker hands in hand_ratings.
    :rtype: list.
    """
    best_rating = 0

    for rating in hand_ratings.values():
        best_rating = max(best_rating, rating)

    best_hands = []

    for hand, rating in hand_ratings.items():

        if rating == best_rating:
            best_hands.append(hand)

    return best_hands


def pick_best_poker_hand(hands):
    """
    Return best poker hands from hands.

    :param hands: array of poker hands.
    :type hands: iterable.

    :return: best poker hands from hands.
    :rtype: list.
    """
    hand_ratings_by_combinations = {}

    for hand in hands:
        hand_ratings_by_combinations[hand] = rate_hand_by_combinations(parse_hand(hand))

    best_hands = determine_best_hands(hand_ratings_by_combinations)

    hand_ratings_by_cards = {}

    for hand in best_hands:
        hand_ratings_by_cards[hand] = determine_highest_card(parse_hand(hand))

    best_hands = determine_best_hands(hand_ratings_by_cards)

    return best_hands


hands = ["4D 5S 6S 8D 3C", "2S 4C 7S 9H 10H", "3S 4S 5D 6H JH", "3H 4H 5C 6C JD"]
print(pick_best_poker_hand(hands))
