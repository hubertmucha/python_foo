def f02_10_groupListN(l, n):
    """
    Groups the elements in the input list in the chunks of a given size.

    Parameters
    ----------
    l : list
        List of an type (can be empty)
    n : int
        Size of the chunk in the output list

    Returns
    -------
    list
        List of the lists. Each chunk is of the lenght of n.
        E.g.:
        f02_10_groupListN([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 65
      (docstring and comments are ignored when counting)
    - do not use "import", "while"
    """
    return [l[i:i+n] for i in range(0, len(l), n)]
