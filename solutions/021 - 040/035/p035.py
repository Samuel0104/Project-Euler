from eulerlib import time, isPrime
initial = time()

def isCirc(n):
    rot = str(n)
    for i in range(len(rot)):
        rot = rot[1:] + rot[0]
        if not isPrime(int(rot)):
            return False
    return True

ans = 13
for n in range(101, 1000000, 2):
    if isCirc(n):
        ans += 1
print(ans)

final = time()
print(f"Time: {final-initial}")