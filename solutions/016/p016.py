from eulerlib import time
initial = time()

ans = 0
for digit in str(2**1000):
    ans += int(digit)
print(ans)

final = time()
print(f"Time: {final-initial}")