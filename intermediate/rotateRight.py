# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        # Compute the length of the list and get the tail
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        
        # Connect the tail to the head to make it circular
        tail.next = head
        
        # Find the new tail: (length - k % length - 1)th node
        # and the new head: (length - k % length)th node
        k = k % length
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        # Break the circle
        new_tail.next = None
        
        return new_head