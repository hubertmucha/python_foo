def f02_12_evenFromList(l):
    """
    Returns even numbers from the list of integers.

    Parameters
    ----------
    l : list
        List of integetrs (can be empty)

    Returns
    -------
    list
        List of the even integers from the input list in the
        original order

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 62
      (docstring and comments are ignored when counting)
    - do not use "import", "for", "while"
    """
    return list(filter(lambda x: x % 2 == 0, l))
