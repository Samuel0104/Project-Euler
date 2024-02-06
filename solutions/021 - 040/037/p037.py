from eulerlib import time, isPrime
initial = time()

def left2right(n):
    if isPrime(int(n)):
        if len(n) == 1:
            return True
        else:
            return left2right(n[1:])
    return False
def right2left(n):
    if isPrime(int(n)):
        if len(n) == 1:
            return True
        else:
            return right2left(n[:-1])
    return False

count = 0
ans = 0
n = 23
while count < 11:
    if left2right(str(n)) and right2left(str(n)):
        count += 1
        ans += n
    if n%10 == 3: # Only numbers ending in 3 or 7 are considered
        n += 4
    else:
        n += 6
print(ans)

final = time()
print(f"Time: {final-initial}")