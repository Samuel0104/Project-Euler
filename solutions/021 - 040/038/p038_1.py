from eulerlib import time, isPandig
initial = time()

"""
The problem already states that the product of 9 and
(1, 2, 3, 4, 5) is pandigital, so we only check for numbers
starting with 9.

Numbers between 91 and 98 form 8-digit numbers when concatenated
as a product with (1, 2, 3), and the product of (1, 2) and
any number between 912 and 987 forms a 7-digit number. In any
case, it's not possible to continue without exceeding nine
digits so we only check for 4-digit numbers starting with 9.
"""

ans = 0
for n in range(9183, 9876): # The example starts with 9182
    p = ""
    i = 1
    while len(p) < 9:
        p += str(i*n)
        i += 1
    if len(p) == 9 and isPandig(p):
        ans = max(ans, int(p))
print(ans)

final = time()
print(f"Time: {final-initial}")