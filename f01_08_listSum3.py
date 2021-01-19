def listSum3(list):
    """
    Sum of every third element in the list

    Parameters
    ----------
    l : list
        List of the numbers (can be empty)

    Returns
    -------
    [sum0, sum1, sum2] : list
        where:
            sum0 = l[0] + l[3] + l[6] ...
            sum1 = l[1] + l[4] + l[7] ...
            sum2 = l[2] + l[5] + l[8] ...

    """
    sumlist = [0,0,0]
    for n in range(0,3):
        for i in range(n,len(list),3):
            sumlist[n] = sumlist[n]+list[i]
    return sumlist
