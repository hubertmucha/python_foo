def f02_13_removeDupl2D(l):
    """
    Removes duplicates from a 2-D list

    Parameters
    ----------
    l : list
        2-dimentional list (list of lists)
    
    Returns
    -------
    list
        2-D list with the duplicated elements removed, in the original order
        
    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 66
      (docstring and comments are ignored when counting)
    - do not use "import"
    """
    a = []
    for i in l:
        if i not in a:
            a.append(i)
    return a
