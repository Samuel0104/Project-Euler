from eulerlib import time, fact
initial = time()

"""
There are 9! permutations that start with a 0, 9! permutations
that start with a 1 and so on. After choosing the first digit,
there will be 8! permutations for each remaining digit.

This program uses integer division to find the next number until
there is only 0! = 1 permutation left (one remaining digit).
"""

digits = [x for x in range(10)]
n = 1000000
ans = ""
for i in range(9, -1, -1):
    pos = (n - 1)//fact(i)
    n %= fact(i)
    ans += str(digits[pos])
    digits.remove(digits[pos])
print(ans)

final = time()
print(f"Time: {final-initial}")