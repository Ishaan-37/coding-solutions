class Solution(object):
    def subsets(self, nums):
        result = []
        current = []
        def backtrack(i):
            if i == len(nums):                   # Base case
                result.append(current[:])  #Jo subset abhi bana,uski copy answer mein save karo.
                return
            backtrack(i + 1)  # Choice 1: DON'T take nums[i]
            current.append(nums[i])     # Choice 2: TAKE nums[i]
            backtrack(i + 1)           
            current.pop()    # Backtrack
        backtrack(0)
        return result