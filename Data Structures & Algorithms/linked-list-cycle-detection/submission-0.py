# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # i will cycle thr the linkedList, saving the node in dict
        # until i either find the nxt node in the dict or head.next == None

        listDict = {}
        while head:
            if head in listDict:
                return True
            
            if head.next == None:
                return False
                
            listDict[head] = head
            head = head.next
            
        return False

            
