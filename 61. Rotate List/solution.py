    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(k == 0):
            return head
        length = 0
        current = head
        while(current is not None):
            length += 1
            current = current.next
        if(length == 0):
            return head
        k = k % length
        if(k == 0):
            return head
        slow = head
        fast = head
        for i in range(0,k):
            fast = fast.next
        storageSlow = head
        storageFast = head
        while(fast is not None):
            storageSlow = slow
            slow = slow.next
            storageFast = fast
            fast = fast.next
        storageFast.next = head
        storageSlow.next = None
        return slow 
