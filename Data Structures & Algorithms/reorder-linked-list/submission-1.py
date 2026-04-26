# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
save the nodes in an array bcos i need to know the tail and pretail
make pointer to the curr head for return
while ansHead.nxt & ansHead.nxt.nxt
save the ansHead.next in tmpHead(nxtHead)
pop out the curr tail and point the head.nxt to the tail
point the ansHead.nxt.nxt = tmpHead
peek at the nxt tail and point it to None
then ansHead to the tmpHead
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        i = 0
        tmp1Head = head
        ansHead = head
        while tmp1Head:
            arr.append(tmp1Head)
            tmp1Head = tmp1Head.next
        
        # print([i.val for i in arr])
        while ansHead.next and ansHead.next.next:
            tHead = ansHead.next
            tail = arr.pop()
            ansHead.next = tail
            ansHead.next.next = tHead
            nxtTail = arr[-1]
            nxtTail.next = None
            ansHead = tHead