def f02_07_findCommonEls2(a,b):
    """
    Find common elements of two unique lists. Gives reverse sorted output.

    Parameters
    ----------
    a : list
        List of unique integers (can be empty).
    b : list
        List of unique integers (can be empty).

    Returns
    -------
    list
        List of the integers that are common for both input lists,
        sorted in the descending order.

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 72
      (docstring and comments are ignored when counting)
    - do not use "import", "set"
    """
    return sorted([e for e in a if e in b],reverse=1)
