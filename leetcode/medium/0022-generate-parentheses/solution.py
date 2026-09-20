class Solution(object):
    def generateParenthesis(self, n):
        result = []
        current = []
        def backtrack(oc, cc):          
            if oc == n and cc == n:         # Base case
                result.append("".join(current))
                return          
            if oc < n:       # Add opening bracket
                current.append("(")
                backtrack(oc + 1, cc)
                current.pop()         
            if cc < oc:      # Add closing bracket
                current.append(")")
                backtrack(oc, cc + 1)
                current.pop()
        backtrack(0, 0)
        return result