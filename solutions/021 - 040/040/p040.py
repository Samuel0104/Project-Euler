from eulerlib import time
initial = time()

decimal = ""
n = 0
while len(decimal) < 1000000:
    n += 1
    decimal += str(n)

ans = 1
for j in range(7):
    ans *= int(decimal[10**j - 1])
print(ans)

final = time()
print(f"Time: {final-initial}")