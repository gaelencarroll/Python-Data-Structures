def mode(nums):

    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    mode_dict = {}
    for num in nums:
        if num in mode_dict:
            mode_dict[num] += 1
        else:
            mode_dict[num] = 1
    ans = [key for key in mode_dict.keys() if mode_dict[key] == max(mode_dict.values())]
    return(ans[0])
