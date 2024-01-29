from eulerlib import time, comb
initial = time()

size = 20
print(comb(2*size, size)) # Vertical axis of Pascal's triangle

final = time()
print(f"Time: {final-initial}")