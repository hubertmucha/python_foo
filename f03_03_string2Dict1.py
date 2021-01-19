def f03_03_string2Dict1(s):
    """
    The function counts the occurences of the characters in the string
    and returns the dictionary where the key is a character and the value
    is the number of occurences.

    Parameters
    ----------
    s : str
        Any string (can by empty).

    Returns
    -------
    dict
        The keys of the dictionary are the chars from the string. The
        value is the number of the occurencies of the char in the string.
        The dictionary is sorted by keys in the ascending order, using
        standard sorted() function.

   Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 66
      (docstring and comments are ignored when counting)
    - do not use "import"
    """
    return {c:s.count(c) for c in sorted(set(s))}
