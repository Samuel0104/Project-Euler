from eulerlib import time
initial = time()

ans = 0
for num in range(10, 1000000): # 999999 > 6 x 9^5
    s = sum(int(digit)**5 for digit in str(num))
    if s == num:
        ans += num
print(ans)

final = time()
print(f"Time: {final-initial}")