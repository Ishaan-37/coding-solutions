class Solution(object):
    def permute(self, nums):
        result = []
        current = []
        def backtrack():
            if len(current) == len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                if nums[i] not in current:
                    current.append(nums[i])
                    backtrack()
                    current.pop()
        backtrack()
        return result