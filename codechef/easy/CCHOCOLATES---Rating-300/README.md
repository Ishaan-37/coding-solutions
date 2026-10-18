# CCHOCOLATES - Rating 300

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-18T17:01:05.040Z  

```py

t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    nums = [a, b, c]
    nums.sort()
    print(nums[1])
    t -= 1

```

---

[View on CodeChef](https://www.codechef.com/problems/CCHOCOLATES)