def f02_14_listModNoFor(l):
    """
    Increments the list of integers except for the last element,
    which is decremented.

    Parameters
    ----------
    l : list
        list of integers (can be empty)
    
    Returns
    -------
    list
        list, where all the input elements are incremented and
        the last one is decremented.
        
    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 94
      (docstring and comments are ignored when counting)
    - do not use "import", "for", "while"
    Hint: use map + enumerate
    """
    a = list(map(lambda x : x+1,l))[0:-1]
    if len(l)>0:
        a.append(l[-1]-1)
    return a
