def listSumN(list,n):
    """
    Sum of every N-th element in the list

    Parameters
    ----------
    l : list
        List of the numbers (can be empty)
    n : int
        Number of sums that should be created for the list.
        n > 0

    Returns
    -------
    [sum0, sum1, ..., sum(N-1)] : list
        where:
            sum0 = l[0] + l[0+N] + l[0+2*N] ...
            sum1 = l[1] + l[1+N] + l[1+2*N] ...
            ...
            sum(N-1) = l[N-1] + l[N-1+N] + l[N-1+2*N] ...

    """
    sumlist = []
    for m in range(0,n):
        buf = 0
        for i in range(m,len(list),n):
            buf = buf+list[i]
        sumlist.append(buf)
    return sumlist
