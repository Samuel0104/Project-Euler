from eulerlib import time
initial = time()

ans = 1
for n in range(2, 1001, 2):
    val = (n - 1)**2
    for i in range(4):
        val += n
        ans += val
print(ans)

final = time()
print(f"Time: {final-initial}")