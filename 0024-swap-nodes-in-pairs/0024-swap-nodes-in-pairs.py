class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #dummy node
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            #swapping
            first.next = second.next  
            second.next = first       
            prev.next = second        
            
            prev = first
        
        #new head
        return dummy.next