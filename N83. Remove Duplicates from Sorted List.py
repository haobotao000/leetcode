# Given a sorted linked list, delete all duplicates such that each element appear only once.
# Solutions:
class Solution(object):
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        y = head
        while y.next != None:
            if y.val == y.next.val:
                y.next = y.next.next
            else:
                y = y.next
        return head