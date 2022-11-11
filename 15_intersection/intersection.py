def intersection(l1, l2):
    l1_set = set(l1)
    l2_set = set(l2)
    new_set = l1_set & l2_set
    lst = list(new_set)
    return(lst)
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """