class Solution:
    def backspaceCompare(self, s, t):

        # Pointers starting from the end
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:

            # Find next valid character in s
            skip = 0
            while i >= 0:
                if s[i] == "#":
                    skip += 1
                    i -= 1
                elif skip > 0:
                    skip -= 1
                    i -= 1
                else:
                    break

            # Find next valid character in t
            skip = 0
            while j >= 0:
                if t[j] == "#":
                    skip += 1
                    j -= 1
                elif skip > 0:
                    skip -= 1
                    j -= 1
                else:
                    break

            # Compare current valid characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False

            # One string has a character left, the other doesn't
            elif i >= 0 or j >= 0:
                return False

            # Move to previous character
            i -= 1
            j -= 1

        return True