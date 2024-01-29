from eulerlib import time
initial = time()

seq = set()
for a in range(2, 101):
    for b in range(2, 101):
        seq.add(a**b)
print(len(seq))

final = time()
print(f"Time: {final-initial}")