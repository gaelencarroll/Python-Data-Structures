names = [
            {'first': 'Ada', 'last': 'Lovelace'},
            {'first': 'Grace', 'last': 'Hopper'},
        ]

def extract_full_names(people):
    full_names = []
    for name in names:
        first_name = name.get('first')
        last_name = name.get('last')
        full_name = first_name + ' ' + last_name
        full_names.append(full_name)
    return(full_names)
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

