class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []

        for x in s:
            if stack and stack[-1][0] == x:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([x, 1])

        return ''.join(x * count for x, count in stack)