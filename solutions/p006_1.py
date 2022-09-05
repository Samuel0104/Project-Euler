from eulerlib import time
initial = time()

a, b = 0, 0
for i in range(101):
    a += i
    b += i**2
print((a**2) - b)

final = time()
print(f"\nTime: {final-initial}")