class Solution(object):
    def removeInvalidParentheses(self, s):

        result = set()

        def dfs(i, path, balance, left_remove, right_remove):

            if i == len(s):
                if balance == 0 and left_remove == 0 and right_remove == 0:
                    result.add("".join(path))
                return

            ch = s[i]

            # Case 1: character is '('
            if ch == '(':

                # Remove it
                if left_remove > 0:
                    dfs(i + 1, path, balance,
                        left_remove - 1, right_remove)

                # Keep it
                path.append(ch)
                dfs(i + 1, path, balance + 1,
                    left_remove, right_remove)
                path.pop()

            # Case 2: character is ')'
            elif ch == ')':

                # Remove it
                if right_remove > 0:
                    dfs(i + 1, path, balance,
                        left_remove, right_remove - 1)

                # Keep it only if valid
                if balance > 0:
                    path.append(ch)
                    dfs(i + 1, path, balance - 1,
                        left_remove, right_remove)
                    path.pop()

            # Case 3: normal letter
            else:
                path.append(ch)
                dfs(i + 1, path, balance,
                    left_remove, right_remove)
                path.pop()

        # Count how many '(' and ')' must be removed
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        dfs(0, [], 0, left_remove, right_remove)

        return list(result)