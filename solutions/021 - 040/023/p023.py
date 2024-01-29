from eulerlib import time, divisorSum
initial = time()

def abundantSum(n):
    for i in abundants:
        if n - i in abundants:
            return True
    return False

abundants = set()
ans = 0
for i in range(1, 20162): # According to Wolfram, the limit can be reduced
    if not abundantSum(i):
        ans += i
    if divisorSum(i) > i:
        abundants.add(i)
print(ans)

final = time()
print(f"Time: {final-initial}")