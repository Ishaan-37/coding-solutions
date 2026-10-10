
class Solution(object):
    def minInsertions(self, s):
        insertions = 0
        need = 0

        for ch in s:
            if ch == '(':
                # Previous opening bracket needs one more ')'
                if need % 2 == 1:
                    insertions += 1
                    need -= 1

                # Every '(' needs two ')'
                need += 2

            else:  # ch == ')'
                need -= 1

                # Extra ')' without a matching '('
                if need < 0:
                    insertions += 1
                    need = 1

        # Insert any missing closing brackets
        return insertions + need
