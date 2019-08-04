# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(None)
        node = ListNode(None)
        if(l1.val == l2.val):
            head.val = l1.val
            node = head
            head.next = ListNode(l2.val)
            head=head.next
            l1 = l1.next
            l2 = l2.next
        elif(l1.val<l2.val):
            head.val = l1.val
            node = head
            l1 = l1.next
        elif(l2.val<l1.val):
            head.val = l2.val
            node = head
            l2 = l2.next
        while(l1 is not None and l2 is not None):
            if(l1.val == l2.val):
                head.next = ListNode(l1.val)
                head = head.next
                head.next = ListNode(l2.val)
                head = head.next
                l1 = l1.next
                l2 = l2.next
            elif(l1.val<l2.val):
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next
            elif(l2.val<l1.val):
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next
        if(l1 is not None):
            while(l1 is not None):
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next
        if(l2 is not None):
            while(l2 is not None):
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next
return node
