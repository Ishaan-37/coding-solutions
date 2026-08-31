class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for x in s:
            if x in '({[':
                stack.append(x)
            else:
                if not stack or stack.pop() != pairs[x]:
                    return False
        return not stack