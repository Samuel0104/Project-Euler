from time import time

def isPal(string: str) -> bool:
    """
    Tests if a string
    is a palindrome
    """
    return string == string[::-1]

def gcd(a: int, b: int) -> int:
    """
    Returns the greatest common
    divisor of a and b
    """
    if a%b == 0:
        return abs(b)
    return gcd(b, a%b)

def lcm(a: int, b: int) -> int:
    """
    Returns the lowest positive
    common multiple of a and b
    """
    return abs(a*b//gcd(a, b))
