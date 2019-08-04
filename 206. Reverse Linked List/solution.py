# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previousNode = None
        while(head):
            currentNode = head
            head = head.next
            currentNode.next = previousNode
            previousNode= currentNode
        return previousNode 
