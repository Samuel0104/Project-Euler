from eulerlib import time, isPal
initial = time()

def prob004():
    for number in range(997799, 10000, -1): # 100 x 100 = 10000 and 999 x 999 = 998001
        if isPal(str(number)):
            for factor in range(999, 99, -1):
                if number%factor == 0 and len(str(number//factor)) == 3:
                    return number
print(prob004())

final = time()
print(f"\nTime: {final-initial}")