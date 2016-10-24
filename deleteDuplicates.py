class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
        	return
        if head.next is None:
        	return head

        second = head.next
        if head.val != second.val:
        	head.next = self.deleteDuplicates(second)
        	return head

       	while head and second and head.val == second.val:
       		head = head.next
       		second = second.next
       	return self.deleteDuplicates(second)
