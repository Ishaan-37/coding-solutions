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
