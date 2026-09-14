class Solution(object):
    def mergeKLists(self, lists):
        arr = [] #Empty array banaya
        for head in lists:   #Har linked list par ja rahe ho
            while head:
                arr.append(head.val)  #Value array mein daalo
                head = head.next      #Next node par move karo
        arr.sort()
        dummy = ListNode(0)        #Ek temporary/dummy node banaya
        curr = dummy
        for x in arr:
            curr.next = ListNode(x)   #New node banao
            curr = curr.next
        return dummy.next
        