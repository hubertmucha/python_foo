def f02_04_countElemBetween1(l,a,b):
    """
    Count elements in the list that are within the range (a,b)

    Parameters
    ----------
    l : list
        List of numbers.
    a : number
    b : number

    Returns
    -------
    int
        Number of elements x in the input list such that a < x < b

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 66
      (docstring and comments are ignored when counting)
    - do not use "import"
    - do not use "for" loop
    """
    return sum(map(lambda x : a<x<b, l))
