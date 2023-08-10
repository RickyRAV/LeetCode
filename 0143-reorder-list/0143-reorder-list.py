# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        #step 1: split the list into two halves.
        #use the slow and fastest pointer approach to find the middle of the linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            
        #"second" now points to the head of the second half 
        second = slow.next
        #break the linked list
        slow.next = None
        
        #step 2: reverse the second half
        prev, curr = None, second
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        second = prev
        
        #step 3: merge the lists alternately
        first, curr = head, head
        while second:
            #store the next pointers
            next_first = first.next
            next_second = second.next
            
            #adjust the next pointers for reordering
            first.next = second
            second.next = next_first
            
            #move the pointers forward
            first = next_first
            second = next_second
        