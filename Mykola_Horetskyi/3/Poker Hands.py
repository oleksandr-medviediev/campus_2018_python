card_suits = ("H", "S", "C", "D")
card_values = ("A","K","Q","J","10","9","8","7","6","5","4","3","2")


def is_straight_flush(hand):
    """
    Checks whether poker hand is straight flush

    Args:
    hand (str) string represanting poker hand
    
    Returns:
    (bool) result of mentioned check
    """

    result = is_straight(hand) and is_flush(hand)

    return result


def is_straight(hand):
    """
    Checks whether poker hand is straight

    Args:
    hand (str) string represanting poker hand
    
    Returns:
    (bool) result of mentioned check
    """

    consequtive_values_count = 0

    for value in card_values:
        if value in hand:
            consequtive_values_count += 1
            if consequtive_values_count == 5:
                break;
        else:
            consequtive_values_count = 0

    result = consequtive_values_count == 5

    return result


def is_flush(hand):
    """
    Checks whether poker hand is flush

    Args:
    hand (str) string represanting poker hand
    
    Returns:
    (bool) result of mentioned check
    """

    result = False

    for suit in card_suits:
        if hand.count(suit) == 5:
            result = True
            break

    return result



def is_four_of_a_kind(hand):
    """
    Checks whether poker hand is four of a kind

    Args:
    hand (str) string represanting poker hand
    
    Returns:
    (bool) result of mentioned check
    """

    result = False

    for value in card_values:
        if hand.count(value) == 4:
            result = True
            break

    return result


def compare_four_of_a_kind(hand1, hand2):
    """
    Compares two "four of a kind" poker hands

    Args:
    hand1, hand2 (str) string represanting "four of a kind" poker hand
    
    Returns:
    (int) returns 1 if first hand is greater,
          returns 0 if hands are of the same value
          returns -1 if second hand greater
    """
    compare_specific_count_high_card(hand1, hand2, 4)
     
    return 0


def is_full_house(hand):
    """
    Checks whether poker hand is straight

    Args:
    hand (str) string represanting poker hand
    
    Returns:
    (bool) result of mentioned check
    """
    
    has_three_of_a_kind = False
    has_two_of_a_kind = False

    for value in card_values:
        if hand.count(value) == 3:
            has_three_of_a_kind = True
        elif hand.count(value) == 2:
            has_two_of_a_kind = True

    result = has_three_of_a_kind and has_two_of_a_kind

    return result


def compare_full_house(hand1, hand2):
    """
    Compares two full house poker hands

Args:
    hand1, hand2 (str) string represanting full house poker hand
    
Returns:
    (int) returns 1 if first hand is greater,
          returns 0 if hands are of the same value
          returns -1 if second hand greater
"""

    result = compare_specific_count_high_card(hand1, hand2, 3)
    
    if result == 0:
        result = compare_specific_count_high_card(hand1, hand2, 2)
    
    return result


def is_three_of_a_kind(hand):
    """
    Checks whether poker hand is three of a kind

    Args:
    hand (str) string represanting poker hand
    
    Returns:
    (bool) result of mentioned check
    """
    
    three_of_a_kind = False
    two_of_a_kind = False
    
    for value in card_values:
        if hand.count(value) == 3:
            three_of_a_kind = True
        elif hand.count(value) == 2:
            two_of_a_kind = True

    result = three_of_a_kind and not two_of_a_kind

    return result


def compare_three_of_a_kind(hand1, hand2):
    """
    Compares two "three of a kind" poker hands

    Args:
    hand1, hand2 (str) string represanting "three of a kind" poker hand
    
    Returns:
    (int) returns 1 if first hand is greater,
          returns 0 if hands are of the same value
          returns -1 if second hand greater
    """

    result = compare_specific_count_high_card(hand1, hand2, 3)
    
    if result == 0:
        result == compare_specific_count_high_card(hand1, hand2, 1)
    
    return result


def is_two_pair(hand):
    """
    Checks whether poker hand is two pair

    Args:
    hand (str) string represanting poker hand
    
    Returns:
    (bool) result of mentioned check
    """

    pair_count = 0
    
    for value in card_values:
        if hand.count(value) == 2:
            pair_count += 1
            
    result = pair_count == 2
    
    return result


def compare_pairs(hand1, hand2):
    """
    Compares two "two pair" poker hands

    Args:
    hand1, hand2 (str) string represanting "two pair" poker hand
    
    Returns:
    (int) returns 1 if first hand is greater,
          returns 0 if hands are of the same value
          returns -1 if second hand greater
    """

    result = compare_specific_count_high_card(hand1, hand2, 2)
    
    if result == 0:
        result == compare_specific_count_high_card(hand1, hand2, 1)
    
    return result


def is_one_pair(hand):
    """
    Checks whether poker hand is two pair

    Args:
    hand (str) string represanting poker hand
    
    Returns:
    (bool) result of mentioned check
    """
    pair_count = 0
    
    for value in card_values:
        if hand.count(value) == 2:
            pair_count += 1
            
    result = pair_count == 1
    
    return result


def compare_high_card(hand1, hand2):
    """
    Compares highest ranking cards of two poker hands,
    if the are of the same value compares second-high ranking cards
    and etc.

    Args:
    hand1, hand2 (str) string represanting straight poker hand
    
    Returns:
    (int) returns 1 if first hand is greater,
          returns 0 if hands are of the same value
          returns -1 if second hand greater
    """
        
    result = 0

    for value in card_values:
        
        if value in hand1:
            if not value in hand2:
                result = 1
                break
            
        else:
            if value in hand2:
                result = -1
                break
    
    return result

def compare_specific_count_high_card(hand1, hand2, number):
    """
    Compares highest ranking cards that inluded certain number of times
    in each of of two poker hands,
    if the are of the same value compares second-high ranking cards
    that are included same number of times and etc
    (with 5 card hand this is possible only for count 1 and 2)

    Args:
    hand1, hand2 (str) string represanting straight poker hand
    number (int) how many cards of value must be in hand
    
    Returns:
    (int) returns 1 if first hand is greater,
          returns 0 if hands are of the same value
          returns -1 if second hand greater
    """
    result = 0

    for value in card_values:
        
        if hand1.count(value) == number:
            if not hand2.count(value) == number:
                result = 1
                break
            
            if (number > 2):
                break
            
        else:
            if and2.count(value) == number:
                result = -1
                break
    
    return result
    


def compare_two_hands(hand1, hand2):
    """
    Compares two poker hands

    Args:
    hand1, hand2 (str) string represanting poker hand
    
    Returns:
    (int) returns 1 if first hand is greater,
          returns 0 if hands are of the same value
          returns -1 if second hand greater
    """

    result = 0

    if is_straight_flush(hand1):
        if not is_straight_flush(hand2):
            result = 1
        else:
            result = compare_high_card(hand1, hand2)
            
    elif is_straight_flush(hand2):
        result = -1

    elif is_straight(hand1):
        if not is_straight(hand2):
            result = 1
        else:
            result = compare_high_card(hand1, hand2)

    elif is_straight(hand1):
        result = -1

    elif is_flush(hand1):
        if not is_flush(hand2):
            result = 1
        else:
            result = compare_high_card(hand1, hand2)
            
    elif is_flush(hand2):
        result = -1

    elif is_four_of_a_kind(hand1):
        if not is_four_of_a_kind(hand2):
            result = 1
        else:
            result = compare_four_of_a_kind(hand1, hand2)
            
    elif is_four_of_a_kind(hand2):
        result = -1

    elif is_full_house(hand1):
        if not is_full_house(hand2):
            result = 1
        else:
            result = compare_full_house(hand1, hand2)

    elif is_full_house(hand2):
        result = -1

    elif is_three_of_a_kind(hand1):
        if not is_three_of_a_kind(hand2):
            result = 1
        else:
            result = compare_three_of_a_kind(hand1, hand2)

    elif is_three_of_a_kind(hand2):
        result = -1

    elif is_two_pair(hand1):
        if not is_two_pair(hand2):
            result = 1
        else:
            result = compare_pairs(hand1, hand2)

    elif is_two_pair(hand2):
        result = -1

    elif is_one_pair(hand1):
        if not is_one_pair(hand2):
            result = 1
        else:
            result = compare_pairs(hand1, hand2)
            
    elif is_one_pair(hand2):
        result = -1

    else:
        result = compare_high_card(hand1, hand2)

    return result

def pick_best_poker_hands(hands):
    """
    Returns the greatest hand from the list

    Args:
    hands (list of str) list of strings represanting poker hands

    Returns
    (str) string represanting the poker hand from the list
    with the highest value
    """

    while len(hands) > 1:
        if compare_two_hands(hands[0], hands[1]) == 1:
            hands.pop(1)
        else:
            hands.pop(0)

    return hands[0]
