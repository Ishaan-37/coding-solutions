class Solution(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        even, odd = 1, 0   # prefix sums seen so far (empty prefix = even)
        parity = 0
        res = 0
        for x in arr:
            parity = (parity + x) % 2
            if parity:          # odd prefix -> pair with earlier even prefixes
                res += even
                odd += 1
            else:               # even prefix -> pair with earlier odd prefixes
                res += odd
                even += 1
        return res % MOD