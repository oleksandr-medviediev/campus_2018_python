from hand_shuffle import card_values


combination_priority = ['Royal flush', 'Straight flush', 'Four of a kind', 'Full house', 'Flush', 'Straight', 'Three of a kind', 'Two pair', 'Pair', 'High Card']


def decompose_hand_from_string(instring):
    """
    Decomposing input hand-string into tockens to evaluate
    """
    if not isinstance(instring, str):

        print('Wrong input!')
        return None

    card_tokens = str(instring).split(' ')

    cards = [[token[0:-1], token[-1]] for token in card_tokens]

    return cards


def delta_index(face_a, face_b):
    """
    Calculating deltha in card rank
    """
    result = card_values.index(face_a) - card_values.index(face_b)
    return result


def is_flush(token_hand):
    """
    Check for flush. If so - returns corresponding list with values
    Otherwise - False
    """
    suits = {suit for face, suit in token_hand}
    sorted_hand = sorted(token_hand, key = lambda card: card_values.index(card[0]))
    values = [face for face, suit in sorted_hand]

    if len(suits) == 1:

        result = ['Flush', *values]
        return result 

    else:

        return False


def is_straight(token_hand):
    """
    Check for Straight. If so - returns corresponding list with values
    Otherwise - False
    """
    sorted_hand = sorted(token_hand, key = lambda card: card_values.index(card[0]))

    prev_card = sorted_hand[0]
    
    for card in sorted_hand[1:]:

        if delta_index(card[0], prev_card[0]) != 1:

            break

        prev_card = card

    else:

        result = ['Straight', sorted_hand[0][0]]
        return result

    return False


def countable_combinations(token_hand):
    """
    Check for all countable combos - full-house, four of kind, etc.
    """
    sorted_hand = sorted(token_hand, key = lambda card: card_values.index(card[0]))
    values = [face for face, suit in token_hand]

    values_set = set(values)

    if len(values_set) == 2:

        for type in values_set:

            if values.count(type) == 4:

                result = ['Four of a kind', type]

        else:

            types = ['','']
            for type in values_set:

                if values.count(type) == 3:

                    types[0] = type

                elif values.count(type) == 2:

                    types[1] = type

            result = ['Full house', *types]

    elif len(values_set) == 3:

        for type in values_set:

            if values.count(type) == 3:

                result = ['Three of a kind', type]
                break

        else:

            types = []

            for type in values_set:

                if values.count(type) == 2:

                    types.append(type)

            if delta_index(types[0], types[1]) > 0:

                types = [types[1], types[0]]

            for type in values:

                if values.count(type) == 1:

                    types.append(type)

            result = ['Two pair', *types]

    elif len(values_set) == 4:
        
        for type in values_set:

            if values.count(type) == 2:

                pair_type = type
                result = ['Pair', pair_type]

        types = filter(lambda x: x != pair_type, [card[0] for card in sorted_hand])

        result += types

    else:

        types = [card[0] for card in sorted_hand]
        result = ['High Card', *types]

    return result



def evaluate_one_hand(token_hand):
    """
    Determines rank of combo in given hand
    """
    is_flush_result = is_flush(token_hand)
    is_straight_result = is_straight(token_hand)

    if is_flush_result and is_straight_result:

        if is_straight_result[1] == 'A':

            result = ['Royal flush']

        else:

            result = ['Straight flush'] + is_straight_result[1:]

    elif is_straight_result:

        result = is_straight_result

    elif is_flush_result:

        result = is_flush_result

    else:

        result = countable_combinations(token_hand)

    return result


def evaluate_hands(hands):
    """
    Process incoming list of strings into evaluated hands
    """
    result_list = []

    for hand in hands:

        decomposed_hand = decompose_hand_from_string(hand)
        result_list.append([hand, evaluate_one_hand(decomposed_hand)])

    return result_list


def pick_winner_hands(evaluated_hands):
    """
    Picks most powerful combo/combos from given evaluated hands list
    """
    highest_rank_hands = [evaluated_hands[0]]

    for hand in evaluated_hands[1:]:

        current_highest_rank = combination_priority.index(highest_rank_hands[0][1][0])
        hands_rank = combination_priority.index(hand[1][0])
        deltha_priority = current_highest_rank - hands_rank

        if deltha_priority > 0:

             highest_rank_hands = [hand]

        elif deltha_priority == 0:

            for face_a, face_b in zip(highest_rank_hands[0][1][1:], hand[1][1:]):

                deltha = delta_index(face_a, face_b)
                if deltha > 0:

                    highest_rank_hands = [hand]
                    break

                elif deltha < 0:

                    break

            else:

                highest_rank_hands += [hand]

    return highest_rank_hands

