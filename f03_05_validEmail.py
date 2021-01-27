def f03_05_validEmail(s):
    """
    Checks if the string is a valid email.

    Parameters
    ----------
    s : str
        Email to test.

    Returns
    -------
    bool
        True if the email has correct format <NAME>@<DOMAIN>.
        <NAME> - can include the characters: a-z A-Z 0-9 _ .
               - the first character can not be: _ .
        <DOMAIN> - can include the characters: a-z A-Z 0-9 _ .
                 - last domain part must have 2 or 3 characters e.g. .com .io
                 - characters of the last domain part must be: a-z A-Z
                 - must have at least one dot: .
                 - must not have two consecutive dots: ..
   
    Implementation constraints
    --------------------------
    - target number of non-white characters for the code: 108
      (docstring and comments are ignored when counting)
    - use "import" one time
    - hint: use "re" module
      https://www.w3schools.com/python/python_regex.asp
    """
    import re
    return bool(re.match("^[A-Za-z0-9]+[\w.]+[@][\w][\w.]+[\w][.][\D]{2,3}$", s))
