from time import time

def isPal(string: str) -> bool:
    """
    Tests if a string
    is a palindrome
    """
    return string == string[::-1]
