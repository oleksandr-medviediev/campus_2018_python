
score_of_one_card = { '2': 2 , '3': 3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, '1':10, 'J':11, 'Q':12, 'K':13, 'A':14}
card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_suits = ['D', 'S', 'C', 'H']


def hends_parse(hand):
    """
    Parse hand into two dictinary firs -> {rank, [cards]}, second -> {suit, [cards]}
    :tparam hand: str
    :param hand: poker hand "2S 4C 7S 9H 10H"
    :treturn: [ {} , {} ] firs -> {rank, [cards]}, second -> {suit, [cards]}
    """
    hand = hand.split()
    hand_ranks = dict([card[:len(card) - 1], []] for card in hand)
    hand_suits = dict([card[len(card) - 1], []] for card in hand)

    for card in hand:
        hand_ranks[card[:len(card) - 1]].append(card)
        hand_suits[card[len(card) - 1]].append(card)

    return [hand_ranks, hand_suits]


def _check_straight(ranke_keys):
    result = False
    if len(ranke_keys) == 5:
        result = True if ranke_keys[0] + ranke_keys[4] == 2 * ranke_keys[2] else False
    return result


def _check_flush(dict_suit):
    result = True if len(dict_suit.keys()) == 1 else False
    return result


def hands_score(hand):
    score = 0.0
    dicts_list = hends_parse(hand)
    ranke_keys = [score_of_one_card[val] for val in dicts_list[0].keys()]
    ranke_keys_len = len(ranke_keys)
    ranke_values = list(dicts_list[0].values())

    ranke_keys.sort()
    ranke_values.sort()

    #Check Straight Flush
    if _check_flush(dicts_list[1]) and _check_straight(ranke_keys):
        score = 9.0 + ranke_keys[ranke_keys_len - 1] / 15
    #Check care
    elif ranke_keys_len == 2 and len(ranke_values[1]) == 4:
        card_in_care = ranke_values[1][0]
        score = 8.0 + score_of_one_card[card_in_care[0]] / 15
    #Check full house
    elif ranke_keys_len == 2 and len(ranke_values[1]) == 3:
        card_in_three = ranke_values[1][0]
        score = 7.0 + score_of_one_card[card_in_three[0]] / 15
    #Flush
    elif _check_flush(dicts_list[1]):
        score = 6.0 + ranke_keys[ranke_keys_len - 1] / 15
    #Straight
    elif _check_straight(ranke_keys):
        score = 5.0 + ranke_keys[ranke_keys_len - 1] / 15
    #Check three
    elif len(ranke_values[ranke_keys_len - 1]) == 3:
        card_in_three = ranke_values[2][0]
        score = 4.0 + score_of_one_card[card_in_three[0]] / 15
    #Check two pairs
    elif ranke_keys_len == 3 and len(ranke_values[2]) == 2:
        cars_in_first_pair = ranke_values[1][0]
        cars_in_second_pair = ranke_values[2][0]
        score = 3.0 + score_of_one_card[cars_in_first_pair[0]] / 30 + score_of_one_card[cars_in_second_pair[0]] / 30
    #Check pair
    elif ranke_keys_len == 4:
        card_in_pair = ranke_values[3][0]
        score = 4.0 + score_of_one_card[card_in_pair[0]] / 15
    else:
        score = 1.0 + ranke_keys[ranke_keys_len - 1] / 15

    return score


def pick_best_poker_hands(hands):
    best_csore = 0
    best_hands = []

    for hand in hands:
        new_score = hands_score(hand)

        if (best_csore < new_score):
            best_csore = new_score
            best_hands = [hand]
        elif abs(best_csore - new_score) < 0.00001:
            best_hands.append(hand)

    return best_hands



hands = ["4D 5S 6S 8D 3C",
"2S 4C 7S 9H 10H",
"3S 4S 5D 6H JH",
"3H 4H 5C 6C JD"]
print(pick_best_poker_hands(hands))