from eulerlib import time, fact
initial = time()

ans = 0
for digit in str(fact(100)):
    ans += int(digit)
print(ans)

final = time()
print(f"Time: {final-initial}")