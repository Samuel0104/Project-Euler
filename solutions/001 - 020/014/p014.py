from eulerlib import time, numCollatz
initial = time()

maxIter = 0
for start in range(3, 1000000):
    iters = numCollatz(start)
    if iters > maxIter:
        maxIter = iters
        ans = start
print(ans)

final = time()
print(f"Time: {final-initial}")