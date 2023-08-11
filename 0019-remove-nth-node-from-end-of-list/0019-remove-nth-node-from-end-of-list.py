# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        #advance first pointer so that the gap between first and second is n nodes apart
        for _ in range(n + 1):
            first = first.next
            
        #move first to the end, maintaining the gap
        while first is not None:
            first = first.next
            second = second.next
            
        #remove the nth node from the end
        second.next = second.next.next
        
        return dummy.next