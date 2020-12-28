def stringMod(str):
    """
    Modifies the input string in the following way:
        - removes all the white characters from the beginning and the end of the string
        - first (non-white) character should be uppercase
        - if the first character is "B" or "b", it should be converted to "H"
        - all other characters should be lowercase
        - all spaces in the string should be replaced with '-' (minus) sings
        - last character should be replaced with "!"
    
    Parameters
    -------
    arg : string
    
    Returns
    -------
    Modified string

    """
    str = str.strip()
    str = str.lower()
    newstr = str[1:]
    str = str[0]
    newstr = str.upper()+newstr
    if(newstr[0]=='B'):
        str = newstr[1:]
        char = "H"
        newstr = char+str
    newstr= newstr.replace(' ', '-')
    newstr = newstr[:-1]+"!"

    return newstr
