# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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
            if len(arr) == 0:
                break
            nxtTail = arr[-1]
            nxtTail.next = None
            ansHead = tHead
            print(ansHead.val)
            print([i.val for i in arr])
            print("---------------------")