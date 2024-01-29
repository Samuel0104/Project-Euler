from eulerlib import time
initial = time()

ans = 11 # One Thousand
for i in range(1, 1000):
    n = str(i)
    
    
    if len(n) > 1 and n[-2] == "1": # Tens
        
        if n[-1] == "0":
            ans += 3 # Ten
        elif n[-1] == "1" or n[-1] == "2":
            ans += 6 # Eleven, twelve
        elif n[-1] == "5" or n[-1] == "6":
            ans += 7 # Fifteen, sixteen
        elif n[-1] == "3" or n[-1] == "4" or n[-1] == "8" or n[-1] == "9":
            ans += 8 # Thirteen, fourteen, eighteen, nineteen
        else:
            ans += 9 # Seventeen
            
            
    else: # Units and tens
        
        if n[-1] == "1" or n[-1] == "2" or n[-1] == "6":
            ans += 3 # One, two, six
        elif n[-1] == "4" or n[-1] == "5" or n[-1] == "9":
            ans += 4 # Four, five, nine
        elif n[-1] == "3" or n[-1] == "7" or n[-1] == "8":
            ans += 5 # Three, seven, eight
            
        if len(n) > 1:
            if n[-2] == "4" or n[-2] == "5" or n[-2] == "6":
                ans += 5 # Forty, fifty, sixty
            elif n[-2] == "2" or n[-2] == "3" or n[-2] == "8" or n[-2] == "9":
                ans += 6 # Twenty, thirty, eighty, ninety
            elif n[-2] == "7":
                ans += 7 # Seventy
                
                
    if len(n) > 2: # Hundreds
        
        if n[-3] == "1" or n[-3] == "2" or n[-3] == "6":
            ans += 10 # One undred, two hundred, six hundred
        elif n[-3] == "4" or n[-3] == "5" or n[-3] == "9":
            ans += 11 # Four hundred, five hundred, nine hundred
        elif n[-3] == "3" or n[-3] == "7" or n[-3] == "8":
            ans += 12 # Three hundred, seven hundred, eight hundred
            
        if n[-1] != "0" or n[-2] != "0":
            ans += 3 # And
print(ans)

final = time()
print(f"Time: {final-initial}")