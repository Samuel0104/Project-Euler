from eulerlib import time, isPal
initial = time()

ans = 0
for n in range(1, 1000000, 2): # If n is even, it will end with 0 in base 2
    if isPal(str(n)) and isPal(bin(n)[2:]):
        ans += n
print(ans)

final = time()
print(f"Time: {final-initial}")