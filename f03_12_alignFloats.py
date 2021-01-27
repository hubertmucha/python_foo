def f03_12_alignFloats(l):
    """
    Prints a list floating point numbers aligned to the decimal point.
    Example:

[1.34124, 234.7, 0.32, 1010.12] -> 
   1.34124
 234.7
   0.32
1010.12

    Parameters
    ----------
    l : list
        List of floating point numbers

    Returns
    -------
    None.

    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 94
      (docstring and comments are ignored when counting)
    - do not use "import",
    """
    m = len(str(round(max(l))))
    for i in l:
        a = str(i).split(sep='.')
        print("{}{}.{}".format((m-len(str(a[0])))*" ",a[0],a[1]))
