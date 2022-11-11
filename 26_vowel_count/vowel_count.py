def vowel_count(phrase):
    vowels = {}
    phrase = phrase.lower()
    for let in phrase:
        if let in 'aeiou':
                vowels[let] = vowels.get(let,0) + 1

    return vowels
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """