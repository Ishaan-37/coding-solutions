class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):

        ans1 = need1 * cost1 + need2 * cost2

        ans2 = max(need1, need2) * costBoth

        ans3 = min(need1, need2) * costBoth

        if need1 > need2:
            ans3 += (need1 - need2) * cost1
        else:
            ans3 += (need2 - need1) * cost2

        return min(ans1, ans2, ans3)