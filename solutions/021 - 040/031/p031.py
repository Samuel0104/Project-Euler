from eulerlib import time
initial = time()

sums = [1] + [0]*200
for i in [1, 2, 5, 10, 20, 50, 100, 200]:
    for j in range(i, 201):
        sums[j] += sums[j - i]
print(sums[200])

final = time()
print(f"Time: {final-initial}")