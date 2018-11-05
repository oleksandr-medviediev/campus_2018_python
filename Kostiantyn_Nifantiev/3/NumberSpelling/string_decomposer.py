def string_decomposer(instring):
    """
    This function decomposes string into numeric triades,
    compatible with spell_triade function
    """
    if not type(instring) is str:

        print('Input must be string!')
        return None

    if len(instring) < 1:

        print('Empty input!')
        return None

    elif len(instring) > 24:

        print('Too long string!')
        return None

    if not str(instring).isdecimal():

        print('Input string should be decimal only!')
        return None

    #String lengh should be multiple or three to proceed. So, fill the blanks with zeroes
    zeroes_to_add = (3 - len(instring) % 3) if len(instring) % 3 else 0
    instring = ''.join(['0' * zeroes_to_add, instring])

    numbers_list = [int(num) for num in instring]

    triades = [numbers_list[x: x + 3] for x in range(0, len(numbers_list), 3)]

    return triades
