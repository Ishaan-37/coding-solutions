class Solution(object):
    def reverseList(self, head):
        p = None
        c = head

        while c:
            n = c.next
            c.next = p
            p = c
            c = n

        return p
        