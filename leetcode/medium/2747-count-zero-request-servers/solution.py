
class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])
        q = sorted((v, i) for i, v in enumerate(queries))
        ans = [0] * len(queries)
        count = {}
        j = left = active = 0

        for t, idx in q:
            while j < len(logs) and logs[j][1] <= t:
                s = logs[j][0]
                count[s] = count.get(s, 0) + 1
                if count[s] == 1:
                    active += 1
                j += 1

            while left < j and logs[left][1] < t - x:
                s = logs[left][0]
                count[s] -= 1
                if count[s] == 0:
                    active -= 1
                left += 1

            ans[idx] = n - active

        return ans
