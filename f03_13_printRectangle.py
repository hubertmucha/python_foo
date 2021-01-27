def f03_13_printRectangle(a,b):
    """
    Prints the rectangle of a given size, using ASCII characters.
    Example:
3,5 -> 
+-+
| |
| |
| |
+-+

5,3 -> 
+---+
|   |
+---+

    Parameters
    ----------
    a : int
        Rectangle size in x.
    b : int
        Rectangle size in y.

    Returns
    -------
    None.

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 84
      (docstring and comments are ignored when counting)
    - do not use "import"
    """
    c = a-2
    h = "+%s+" % (c*'-')
    print(h)
    for i in range(1,b-1):
        print("|%s|"% (c*' '))
    print(h)
