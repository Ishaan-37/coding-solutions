class Solution(object):
    def createGrid(self, m, n):
        return ["." * n] + [".".rjust(n, "#")] * (m - 1)