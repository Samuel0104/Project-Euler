from eulerlib import time, numPyth
initial = time()

maxSol = 0
for perim in range(6, 1001, 2): # If the perimeter is odd, some sides won't be integers
    sols = numPyth(perim)
    if sols > maxSol:
        maxSol = sols
        ans = perim
print(ans)

final = time()
print(f"Time: {final-initial}")