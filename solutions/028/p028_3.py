from eulerlib import time
initial = time()

"""
Rearranging the sum:
    
1 + 3 + 5 + 7 + 9 + 13 + 17 + 21 + 25 + ...
= 1 + (3 + 5 + 7 + 9) + (13 + 17 + 21 + 25) + ...
= 1 + ((2 + 4 + 6 + 8) + 4) + ((12 + 16 + 20 + 24) + 4) + ...
= 1 + (2(1 + 2 + 3 + 4) + 4) + (4(3 + 4 + 5 + 6) + 4) + ...

And note that:
    
    n((n - 1) + n + (n + 1) + (n + 2)) + 4
    = n(4n + 2) + 4
    = 4n^2 + 2n + 4
"""

ans = 1
for n in range(2, 1001, 2):
    ans += 4*n**2 + 2*n + 4
print(ans)

final = time()
print(f"Time: {final-initial}")