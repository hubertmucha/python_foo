def f03_10_printHisto(d):
    """
    Prints the histogram for the list of numbers.
    Examples:

    [0,1,0,1,2,5,5,4,6,0] ->
    0 xxx
    1 xx
    2 x
    3
    4 x
    5 xx
    6 x

    [1,1,2,1,10,10,11]
     0
     1 xxx
     2 x
     3
     4
     5
     6
     7
     8
     9
    10 xx
    11 x

    Parameters
    ----------
    d : list
        List of non-negative integers.

    Returns
    -------
    None.

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 92
      (docstring and comments are ignored when counting)
    - do not use "import"
    """
    for i in range(max(d)+1):
        f = '{:>%a} {}'%len('%a'%max(d))
        print(f.format(i,d.count(i)*'x'))
