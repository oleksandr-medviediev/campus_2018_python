# Suits
DIAMONDS = 0
HEARTS = 1
SPADES = 2
CLUBS = 3

suit_convertation = {
    'D': DIAMONDS,
    'H': HEARTS,
    'S': SPADES,
    'C': CLUBS
}

#Combinations' priorities
HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_OF_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_KIND = 7
STRAIGHT_FLUSH = 8

#Card's weight
all_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def determine_suit(symbol):

    """ Function determines type of suit by passed symbol and return it

        Args:
            symbol(str): short name of suit

        Returns:
            int: type suit value
            
    """
    
    suit = suit_convertation.get(symbol, None)

    return suit

    
def determine_hand(string):

    """ Function parses string and return it as list of card

        Args:
            string(str): cards presented by string

        Returns:
            list[dictionary]: list of cards presented by dictionary
                              with next fields: value and suit
                              
    """

    card_string_list = string.split()

    card_list = []
    for i, el in enumerate(card_string_list):
        card_suit = determine_suit(el[-1])
        card_value = all_cards.index(el[:-1])
        card = { 'value': card_value,
                 'suit': card_suit }
        
        card_list.append(card)
        
    return card_list
    
    
def is_straight(hand):

    """ Function checks is this hand combination is straight. Return True,
        if successful, othersise = False.

        Args:
            hand(list[dictionary]): all cards of combination presented by
                                    list of dictionary with next fields:
                                    value and suit
        Returns:
            bool: if combination is straight return True, else - False.

    """
    
    card_values = []
    
    for i, el in enumerate(hand):
        card_values.append(el['value'])

    card_values.sort()

    is_difference_not_great_one = True

    for i in range(1, len(card_values)):
        if card_values[i] - card_values[i - 1] != 1:
            is_difference_not_great_one = False
            break

    # check small straight begins from ace
    if not is_difference_not_great_one and \
       all_cards.index('A') in card_values and \
       card_values[:-1] == [0, 1, 2, 3]:
        
        is_difference_not_great_one = True

    return is_difference_not_great_one

    
def determine_hand_combination(hand):

    """ Function determine hand combination to evaluate it with other.

        Args:
            hand(list[dictionary]): all cards of combination presented by
                                    list of dictionary with next fields:
                                    value and suit
        Returns:
            int: type of combination presented by constant

    """
    
    cards_values = {}
    cards_suits = {}

    for i, el in enumerate(hand):
        value = el['value']
        suit = el['suit']
        cards_values[value] = cards_values.get(value, 0) + 1
        cards_suits[suit] = cards_suits.get(suit, 0) + 1

    combination = HIGH_CARD
    
    #all cards are different
    if len(cards_values) == len(hand):
        is_flush = len(cards_suits) == 1
        if is_straight(hand) and is_flush:
            combination = STRAIGHT_FLUSH
        elif is_straight(hand):
            combination = STRAIGHT
        elif is_flush:
            combination = FLUSH

    elif len(cards_values) == 4:
        #one pair - one card is repeated
        combination = ONE_PAIR
    elif len(cards_values) == 3:
        #set or two pairs
        appearings = cards_values.values()
        is_set = 3 in appearings
        if is_set:
            combination = THREE_OF_KIND
        else:
            combination = TWO_PAIR

    elif len(cards_values) == 2:
        appearings = cards_values.values()
        is_four_of_kind = 4 in appearings

        if is_four_of_kind:
            combination = FOUR_OF_KIND
        else:
            combination = FULL_HOUSE
            
    return combination


def pick_best_poker_hands(hands_list):

    """ Function determine best hand combination(s).

        Args:
            hand_list(list[list[dictionary]]): all combinations need to evaluate
            
        Returns:
            list[list[dictionary]]: list of best combinations

    """
    
    hands = []
    evaluates = []
    for i, el in enumerate(hands_list):
        hand = determine_hand(el)
        hands.append(hand)
        evaluates.append(determine_hand_combination(hand))

    best_combination_value = max(evaluates)

    result_hands = []

    if evaluates.count(best_combination_value) == 1:
        best_combination_index = evaluates.index(best_combination_value)
        result_hands.append(hands_list[best_combination_index])
        
    else:
        best_combinations_list = []
        indices_list = []
        for i in range(len(evaluates)):
            if evaluates[i] == best_combination_value:
                best_combinations_list.append(hands[i])
                indices_list.append(i)
                
        cards_values_list = []

        for i, hand in enumerate(best_combinations_list):
            cards_values = []
            for i, card in enumerate(hand):
                cards_values.append(card['value'])

            cards_values_list.append(cards_values)

        for i, el in enumerate(cards_values_list):
            cards_values_list[i].sort(reverse=True)

        cards_stack = []
        indices_stack = []
        cards_stack.append(cards_values_list.pop())
        indices_stack.append(indices_list.pop())

        # after this cycle in cards_stack will be best combination
        # and in indices_stack their indices
        for i, el in enumerate(cards_values_list):
            if cards_stack[0] == el:
                cards_stack.append(el)
                indices_stack.append(i)
            elif cards_stack[0] < el:
                cards_stack.clear()
                cards_stack.append(el)
                indices_stack.clear()
                indices_stack.append(i)

        for i, index in enumerate(indices_stack):
            result_hands.append(hands_list[index])

    return result_hands
