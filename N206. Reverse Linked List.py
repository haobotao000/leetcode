# Reverse a singly linked list.
# Solution 1: iterative method
class Solution(object):
    def reverseList(self, head):
        prev, curr, next = None, head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        
# Solution 2: recursive method
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        next_node = head.next
        next_node.next = head
        head.next = None
        
        return new_head
            