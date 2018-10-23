def two_pow(pow):
	"""
	two_pow(pow)
	This function returns 2 in pow 'pow'

    Args:
        pow (int): pow to perform

    Returns:
        int: result of performing pow 'pow' on base 2
    """
	return 2**pow

def allergies(score):
	"""
	allergies(score)
	This function returns list of person's allergies

    Args:
        score (int): cumulated allergy score

    Returns:
        list: list of allergies
    """

	allergies = {
	'eggs' : 1,
	'peanuts' : 2,
	'shellfish' : 4,
	'strawberries' : 8,
	'tomatoes' : 16,
	'chocolate' : 32,
	'pollen' : 64,
	'cats' : 128
	}
	
	bin_score_list = []

	while score > 0:

		bin_score_list.append(score % 2)
		score //= 2

	patient_allergies = []

	for i in range(len(bin_score_list)):
		two_in_i = two_pow(i)

		list_allergies_values = list(allergies.values())

		if bin_score_list[i] > 0 and two_in_i in list_allergies_values:

			index_to_look_for = list_allergies_values.index(two_in_i)
			list_allergies_keys = list(allergies.keys())
			patient_allergies.append(list_allergies_keys[index_to_look_for])

	return patient_allergies
