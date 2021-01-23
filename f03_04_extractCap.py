def f03_04_extractCap(s):
    """
    The function returns the list of the words with the first letter
    capitalized (A-Z) in the input string

    Parameters
    ----------
    s : str
        Any string (can be empty)

    Returns
    -------
    list
        List of words in the string starting with A-Z

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 63
      (docstring and comments are ignored when counting)
    - use "import" one time
    - hint: use "re" module
    """
    import re
    return re.findall('[A-Z]\w*',s)
