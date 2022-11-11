def is_palindrome(phrase):
    lowercase = phrase.lower()
    new_phrase = lowercase.replace(' ','')
    ans = new_phrase == new_phrase[::-1]
    return(ans)
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
