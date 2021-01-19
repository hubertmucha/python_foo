def f02_06_findCommonEls1(a,b):
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
    - target number of non-white characters for the code: 69
      (docstring and comments are ignored when counting)
    - do not use "import"
    """
    return sorted(set(a) & set(b),reverse=1)
