class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half_start = self.reverseList(slow)
        
        first_half_start = head
        second_half_iter = second_half_start
        while second_half_iter:
            if first_half_start.val != second_half_iter.val:
                return False
            first_half_start = first_half_start.next
            second_half_iter = second_half_iter.next
        
        self.reverseList(second_half_start)
        
        return True
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev