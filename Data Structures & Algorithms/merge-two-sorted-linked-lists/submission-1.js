/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        let merged = new ListNode()
        let r = merged

        while (list1 && list2){
            if (list1.val > list2.val){
                merged.next = new ListNode(list2.val)
                list2 = list2.next
            }else if (list1.val < list2.val) {
                merged.next = new ListNode(list1.val)
                list1 = list1.next
            }else{
                merged.next = new ListNode(list1.val)
                merged = merged.next
                merged.next = new ListNode(list2.val)
                list1 = list1.next
                list2 = list2.next
            }
            merged = merged.next
            
        }

        if(list1){
            merged.next = list1
        }else{
            merged.next = list2
        }

        return r.next
        
    }
}
