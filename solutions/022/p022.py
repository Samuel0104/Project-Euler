from eulerlib import time
initial = time()

with open("names.txt") as file:
    names = file.read()
names = names.replace('"',"").split(",")
names = sorted(names)

ans = 0
for index, word in enumerate(names):
    score = 0
    for letter in word:
        score += ord(letter) - 64
    score *= (index + 1)
    ans += score
print(ans)

final = time()
print(f"Time: {final-initial}")