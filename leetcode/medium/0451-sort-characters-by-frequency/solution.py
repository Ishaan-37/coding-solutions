class Solution(object):
    def frequencySort(self, s):
        d = {}

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        return ''.join(ch * d[ch] for ch in sorted(d, key=d.get, reverse=True))