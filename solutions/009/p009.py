from eulerlib import time
initial = time()

for a in range(1, 333): # if a < b < c, the maximum possible value for a is 332
    for b in range(a + 1, 500): # Same goes for b with the number 499
        c = ((a**2) + (b**2))**0.5
        if a + b + c == 1000:
            print(int(a*b*c))
            break

final = time()
print(f"\nTime: {final-initial}")