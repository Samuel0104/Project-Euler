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

def isPrime(n: int) -> bool:
    """
    Tests if n is a
    prime number
    """
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(3, int(n**0.5) + 1, 2):
        if n%i == 0:
            return False
    return True
