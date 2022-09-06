from eulerlib import time
initial = time()

Fib = [1, 2]
ans = 2
while Fib[-1] < 4000000:
    Fib.append(Fib[-1] + Fib[-2])
    if Fib[-1]%2 == 0:
        ans += Fib[-1]
print(ans)

final = time()
print(f"\nTime: {final-initial}")
