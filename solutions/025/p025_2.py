from eulerlib import time

initial = time()

a, b = 1, 1
ans = 2
while len(str(b)) < 1000:
    a, b = b, a + b
    ans += 1
print(ans)

final = time()
print(f"Time: {final-initial}")