from eulerlib import time
initial = time()

a = 1
b = 2
ans = 2
while b < 4000000:
    a, b = b, a + b
    if b%2 == 0:
        ans += b
print(ans)

final = time()
print(f"\nTime: {final-initial}")