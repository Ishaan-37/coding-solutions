class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        current = []
        def backtrack(start, target):
            if target == 0:
                result.append(current[:])
                return 
            for i in range(start , len(candidates)):
                if candidates[i] > target:
                    continue
                current.append(candidates[i])
                backtrack(i, target - candidates[i])
                current.pop()
        backtrack(0, target)
        return result