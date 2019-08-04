# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        i = 0
        ret = head
        temp = head
        while(temp):
            count += 1
            temp = temp.next
        calc = int(count/2) + 1
        while(ret):
            i = i + 1
            if(i<calc):
                ret = ret.next
            else:
                break
        return ret 
