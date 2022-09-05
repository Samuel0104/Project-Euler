from eulerlib import time, lcm
initial = time()

ans = 1
for i in range(1, 21):
    ans = lcm(ans, i)
print(ans)

final = time()
print(f"\nTime: {final-initial}")