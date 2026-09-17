class Solution(object):
    def isIsomorphic(self, s, t):
        map = {}          # stores: character from s -> character from t
        have = set()      # stores characters from t that are already used
        for i in range(len(s)):    # traverse both strings using the same index
            if s[i] in map:        # has this character from s been mapped before?
                if map[s[i]] != t[i]:   # existing mapping is different
                    return False        # example: o -> a already, but now o -> r
            else:                 # s[i] has no mapping yet
                if t[i] in have:  # is this t character already used by another s character?
                    return False  # example: a -> c and b -> c
                map[s[i]] = t[i]  # create the mapping
                have.add(t[i])    # remember that this t character is now used
        return True               # all characters followed the rules