from time import time

def isPal(string: str) -> bool: # 4
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

def lcm(a: int, b: int) -> int: # 5
    """
    Returns the lowest positive
    common multiple of a and b
    """
    return abs(a*b//gcd(a, b))

def isPrime(n: int) -> bool: # 7, 10
    """
    Tests if n is a
    prime number
    """
    if n == 2:
        return True
    if n < 2 or n%2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n%i == 0:
            return False
    return True

def numDivisors(n: int) -> int: # 12
    """
    Returns the number of
    positive divisors of n
    """
    decomp = 1
    exp = 0
    while n%2 == 0:
        n /= 2
        exp += 1
    decomp *= exp + 1

    factor = 3
    while n > 1:
        exp = 0
        while n%factor == 0:
            n /= factor
            exp += 1
        decomp *= exp + 1
        factor += 2
    return decomp
