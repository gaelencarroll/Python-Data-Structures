def multiple_letter_count(phrase):
    occurences = {}
    for char in phrase:
        if char in occurences:
            occurences[char] += 1
        else:
            occurences[char] = 1
    return(occurences)
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """