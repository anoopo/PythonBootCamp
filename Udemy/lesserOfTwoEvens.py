def lesser_of_two_evens(a,b):
    """
    DOCSTRING : Takes two numbers and returns:
                 a) lesser of two numbers if both are even
                 b) greater of two numbers if one is odd
    INPUT : two integers
    OUTPUT : one integer
    """
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print (lesser_of_two_evens(0,4))
