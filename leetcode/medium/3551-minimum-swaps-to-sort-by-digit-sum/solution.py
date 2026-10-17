class Solution(object):
    def minSwaps(self, nums):
        digit = lambda n: sum(int(d) for d in str(n))
        target = sorted(nums, key=lambda x: (digit(x), x))
        pos = {v: i for i, v in enumerate(nums)}
        ans = 0
        for i in range(len(nums)):
            if nums[i] != target[i]:
                j = pos[target[i]]
                pos[nums[i]] = j
                pos[target[i]] = i
                nums[i], nums[j] = nums[j], nums[i]
                ans += 1
        return ans