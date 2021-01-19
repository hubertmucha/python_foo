def f01_14_charListIndex(inputList,e):
    """
    Creating a list of index where particular 'element' is located in inputList.
    E.g.
        ['e','x','a','m','l','e'], 'e'
        returns: [0,5]

    Parameters
    ----------
    l : list
        List of chars (can be empty)
    e : char

    Returns
    -------
    r : list
        List of indexes.
    """
    outputList = []
    for i in range(0,len(inputList)):
        if (inputList[i] == e):
            outputList.append(i)
    return outputList
