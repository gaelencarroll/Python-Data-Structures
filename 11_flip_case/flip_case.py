def flip_case(phrase, to_swap):
    new = ''
    for char in phrase:
        if to_swap.lower() == char.lower():
            char = char.swapcase()
        new += char
    return(new)

    # print(to_swap.isupper())
    # if to_swap.isupper():
    #     phrase.replace(to_swap, to_swap.lower())
    #     print(phrase)
    #     phrase.replace(to_swap.lower(), to_swap)
    #     print(phrase)
    # elif to_swap.islower():
    #     phrase.replace(to_swap, to_swap.upper())
    #     phrase.replace(to_swap.upper(), to_swap)
    # return(phrase)
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
