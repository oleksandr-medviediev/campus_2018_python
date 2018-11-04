from string_decomposer import string_decomposer
from triade_speller import spell_triade

magnitude_list = [
    '',
    'thousand',
    'million',
    'billion',
    'trillion',
    'quadrillion',
    'quintillion',
    'sextillion'
    ]


def number_speller(instring):
    """
    This function composes functionality of triade speller and string decomposer into
    final number speller
    """

    triades = string_decomposer(instring)

    triade_tokens = [spell_triade(triade) for triade in triades]

    zip_tokens = zip(triade_tokens, magnitude_list[len(triade_tokens) - 1:: -1])

    string_tokens = []

    for tuple in zip_tokens:

        if tuple[0] == 'zero':

            continue

        string_tokens.append(' '.join(tuple))
    
    string_tokens.append('\n')

    result = ' '.join(string_tokens)

    return result
