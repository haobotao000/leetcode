# Given a linked list, determine if it has a cycle in it.
# Solution 1: Two Pointers
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        fast = slow = head
        while fast != None or fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
# Solution 2: Hash Table
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hash_table = {}
        while head:
            if id(head) in hash_table:
                return True
            hash_table[id(head)] = True
            head = head.next
        return False