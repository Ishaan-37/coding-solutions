# DOLL - Rating 838

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-03T07:45:42.015Z  

```cpp
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    m1, m2 = max(a), 0
    for x in a:
        if x != m1: m2 = max(m2, x)
    print(m1 + m2)
    t -= 1
```

---

[View on CodeChef](https://www.codechef.com/problems/DOLL)