class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head                               # BASE CASE
        newHead = self.reverseList(head.next)   # RECURSIVE CALL
        head.next.next = head                    # WORK
        head.next = None                         # WORK
        return newHead