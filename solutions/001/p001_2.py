from eulerlib import time
initial = time()

print(sum(n for n in range(1000) if (n%3 == 0 or n%5 == 0)))

final = time()
print(f"\nTime: {final-initial}")
