# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2

        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1

        head = ListNode()
        curr = head

        if l1.val <= l2.val:
            head.val, l1 = l1.val, l1.next
        else:
             head.val, l2 = l2.val, l2.next

        while l1 != None and l2 != None: 
            curr.next = ListNode()
            curr = curr.next

            if l1.val <= l2.val:
                curr.val =  l1.val
                l1 = l1.next
            elif l2.val < l1.val: 
                curr.val = l2.val
                l2 = l2.next

        while l1 != None: 
            curr.next = ListNode()
            curr = curr.next
            
            curr.val, l1 =  l1.val, l1.next

        while l2 != None: 
            curr.next = ListNode()
            curr = curr.next
            
            curr.val, l2 =  l2.val, l2.next
            
        return head




