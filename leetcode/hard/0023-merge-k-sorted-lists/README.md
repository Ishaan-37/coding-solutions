# Merge k Sorted Lists

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

 *Merge all the linked-lists into one sorted linked-list and return it.* 

 

 **Example 1:** 

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

```

 **Example 2:** 

```
Input: lists = []
Output: []

```

 **Example 3:** 

```
Input: lists = [[]]
Output: []

```

 

 **Constraints:** 

- k == lists.length
- 0 <= k <= 104
- 0 <= lists[i].length <= 500
- -104 <= lists[i][j] <= 104
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 104.

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 98.98%)  
**Memory:** 20.5 MB (beats 12.50%)  
**Submitted:** 2026-09-14T18:33:50.122Z  

```py
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
        
```

---

[View on LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)