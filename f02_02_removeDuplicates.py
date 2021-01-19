def f02_02_removeDuplicates(l):
    """
    Removing duplicates from the input list
 
    Parameters
    ----------
    x : list
         list of numbers or strings (can be empty)

    Returns
    -------
    list
        list with removed duplicates
        
    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 58
      (docstring and comments are ignored when counting)
    - do not use import
    """
    return list(dict.fromkeys(l))
