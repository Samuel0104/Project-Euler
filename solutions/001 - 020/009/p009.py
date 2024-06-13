from eulerlib import time
initial = time()

def prob009():
    for a in range(1, 333): # If a < b < c, the maximum possible value for a is 332
        for b in range(a + 1, 500): # Same goes for b with the number 499
            c = (a**2 + b**2)**0.5
            if a + b + c == 1000:
                return int(a*b*c)
print(prob009())

final = time()
print(f"\nTime: {final-initial}")
