class Solution(object):
    def generate(self, numRows):
        ans = []  #Jab tumhe loop ke andar results collect karne ho
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                left = ans[i-1][j-1]
                right = ans[i-1][j]
                row[j] = left + right
            ans.append(row)
        return ans
        