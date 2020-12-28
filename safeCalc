def safeCalc(a,b,op):
    """
    Function to do safe aritmetic operations. 
    Returns NaN if trying to divide by 0.

    Parameters
    ----------
    a : number (float or int)
    b : number (float or int)
    op : string, operation code
        
    Returns
    -------
    a + b when op == "add"
    a - b when op == "sub"
    a * b when op == "mul"
    a / b when op == "div"
    NaN (float type) in all other cases

    """
    if(op =="add"):
        return a+b
    elif(op=="sub"):
        return a-b
    elif(op=="mul"):
        return a*b
    elif(op=="div" and b!=0):
        return a/b
    else:
        return float("NaN")
