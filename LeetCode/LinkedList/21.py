from utils import *
from typing import Optional

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        
        head = None
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        last = head

        while l1 and l2:
            if l1.val > l2.val:
                last.next = l2
                l2 = l2.next
            else:
                last.next = l1
                l1 = l1.next

            last = last.next

        last.next = l1 if l1 else l2
        
        return head

print_ll(Solution().mergeTwoLists(array_to_ll([1,2,4]), array_to_ll([1,3,4])))
print_ll(Solution().mergeTwoLists(array_to_ll([]), array_to_ll([])))
print_ll(Solution().mergeTwoLists(array_to_ll([1]), array_to_ll([])))
print_ll(Solution().mergeTwoLists(array_to_ll([]), array_to_ll([0])))