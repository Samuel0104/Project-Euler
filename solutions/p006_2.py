from eulerlib import time
initial = time()

"""
Summation formulas from 1 to n:
    
         n(n + 1)(2n + 1)
    i^2: ----------------
                6
                 
         n(n + 1)
      i: --------
            2
"""

sumOfSquares = 100*(100 + 1)*(2*100 + 1)//6
squareOfSum = (100*(100 + 1)//2)**2
print(squareOfSum - sumOfSquares)

final = time()
print(f"\nTime: {final-initial}")