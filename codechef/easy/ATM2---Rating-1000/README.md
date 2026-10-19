# ATM2 - Rating 1000

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T09:55:41.064Z  

```py
t = int(input())
while t > 0:
    n = int(input())
    s = input()
    count = 0
    for ch in s:
        if ch not in "aeiou":
            count += 1
        else:
            count = 0
        if count == 4:
            break
    if count == 4:
        print("NO")
    else:
        print("YES")
    t -= 1

```

---

[View on CodeChef](https://www.codechef.com/problems/ATM2)