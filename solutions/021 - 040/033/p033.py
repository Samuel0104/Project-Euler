from eulerlib import time, gcd
initial = time()

prodNum = 1
prodDen = 1
for common in range(1, 10):
    for i in range(1, 10):
        for j in range(1, 10):
            for num in [str(common) + str(i), str(i) + str(common)]:
                for den in [str(common) + str(j), str(j) + str(common)]:
                    if int(num)/int(den) == i/j < 1:
                        prodNum *=i
                        prodDen *=j
print(prodDen//gcd(prodNum, prodDen))

final = time()
print(f"Time: {final-initial}")