def sum_up_diagonals(matrix):
    sum_diagonals = 0
    length = len(matrix)
    for n in range(length):
        sum_diagonals += matrix[n][n]
        sum_diagonals += matrix[n][-1-n]
    return sum_diagonals
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    m1 = [
             [1,   2],
             [30, 40],
         ]

    m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
         ]