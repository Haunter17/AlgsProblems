class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        prev = head
        curr = head.next
        head.next = None

        while curr is not None and curr.next is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        curr.next = prev
        return curr

    def reverseBetween(self, head, m, n):
        pass
node1 = ListNode(1)
node2  = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

soln = Solution()
soln.reverse(node1)

curr = node5
while curr is not None:
    print curr.val
    curr = curr.next