def listFirstLastSwap(list):
    """
    Swaps first and last element on the list

    Parameters
    ----------
    l : list
        Any list (can be empty)

    Returns
    -------
    The list with the first and last elements swapped.

    """
    buf = list[0]
    list[0] = list[-1]
    list[-1] = buf
    return list
