class Solution(object):
    def simplifyPath(self, path):
        stack = []
        for x in path.split('/'):
            if x == '..':
                if stack:
                    stack.pop()
            elif x == '' or x == '.':
                continue
            else:
                stack.append(x)

        return '/' + '/'.join(stack)