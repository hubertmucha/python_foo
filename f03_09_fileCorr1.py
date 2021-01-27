def f03_09_fileCorr1(f):
    """
    Prints the file, correcting spaces. The corrections are:
        - remove leading and trailing spaces from each line
        - remove spaces before comma and point (, .)
        - adding spaces, if necessary, after comma and point;
          there should be one space after each comma and point
          (not at the end of the line)

    Parameters
    ----------
    f : str
        Input file name

    Returns
    -------
    None.
    
    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 152
      (docstring and comments are ignored when counting)
    - use "import" one time
    - hint: use "re" module
    - hint: check the documentation:
      https://docs.python.org/3/library/re.html

    """
    from re import sub as s
    with open(f) as p:
        print(s(r"\s+\n\s+", r"\n", s(r"\s+\.", ".", s(r"\s+,", ",", s(r" +", " ", s(r"^\s+|\s+$", "", s(r",", ", ", s(r"\.", ". ", p.read()))))))))
