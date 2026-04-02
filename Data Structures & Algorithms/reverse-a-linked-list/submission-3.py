class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next    # remember next node
            curr.next = prev   # reverse pointer
            prev = curr        # advance prev
            curr = nxt         # move to next node
            
        return prev