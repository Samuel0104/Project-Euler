from eulerlib import time
initial = time()

seq = [1, 2]
ans = 2
while seq[-1] < 4000000:
    seq.append(seq[-2] + seq[-1])
    if seq[-1]%2 == 0:
        ans += seq[-1]
print(ans)

final = time()
print(f"\nTime: {final-initial}")
