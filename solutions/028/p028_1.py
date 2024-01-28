from eulerlib import time
initial = time()

def prob028(n):
    if n == 1:
        return 1
    else:
        val = n**2
        s = val
        for i in range(3):
            val -= (n - 1)
            s += val
        return s + prob028(n - 2)
print(prob028(1001))

final = time()
print(f"Time: {final-initial}")