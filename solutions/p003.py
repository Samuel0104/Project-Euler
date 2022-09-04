from eulerlib import time
initial = time()

n = 600851475143
ans = 1
while n > 1:
    ans += 1
    while n%ans == 0:
        n /= ans
print(ans)

final = time()
print(f"\nTime: {final-initial}")