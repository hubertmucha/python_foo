def listCross2(l1,l2):
    """
    Returns sorted list of the words which begin with the same
    characters, common for two lists.

    Parameters
    ----------
    l1 : list of strings
    l2 : list of strings

    Returns
    -------
    Reversely sorted, unique list of words from the lists, that have the
    corresponding words beginning with the same two letters in another
    list, e.g.:
        l1 = ['Anna','Monika', 'Marek', 'Janusz']
        l2 = ['Gabriela', 'Marta', 'Maria','Antonina']
        -> ['Marta', 'Marek', 'Maria', 'Antonina', 'Anna']
    """
    newlist = []
    for el1 in l1:
        for el2 in l2:
            if(el1[:2]==el2[:2]):
                newlist.append(el1)
                newlist.append(el2)
    newlist = list(dict.fromkeys(newlist))
    newlist.sort(reverse=True)
    return newlist
