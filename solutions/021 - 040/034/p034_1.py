from eulerlib import time, fact
initial = time()

ans = 0
for num in range(10, 10000000): # 9999999 > 7 x 9!
    s = sum(fact(int(digit)) for digit in str(num))
    if s == num:
        ans += num
print(ans)

final = time()
print(f"Time: {final-initial}")