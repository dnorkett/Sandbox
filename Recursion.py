def mult_iter(a,b):
    """Performs iterative multiplication by adding variable a to itself b times"""
    result = 0
    while b > 0:
        result+=a
        b-=1
    return result

def mult(a,b):
    """Performs recursive multiplication"""
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)

def fact(n):
    """Performs recursive factorial"""
    if n == 1:
        return 1
    else:
        return n*fact(n-1)