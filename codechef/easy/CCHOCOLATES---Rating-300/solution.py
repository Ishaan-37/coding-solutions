
t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    nums = [a, b, c]
    nums.sort()
    print(nums[1])
    t -= 1
