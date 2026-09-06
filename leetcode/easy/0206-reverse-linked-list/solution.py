
class Solution(object):
    def reverseList(self, head):
        a = None
        b = head
        while b:
            n = b.next
            b.next = a
            a = b
            b = n
        return a