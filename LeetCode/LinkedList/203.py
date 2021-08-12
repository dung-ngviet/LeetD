from utils import *
from typing import Optional

# Loop solution
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         my_head = ListNode(next = head)
#         head = my_head
#         while head and head.next:
#             if head.next.val == val:
#                 head.next = head.next.next
#             else:
#                 head = head.next
#         return my_head.next

# Recursion solution
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: return None
        
        next_head = self.removeElements(head.next, val)
        if head.val == val: 
            return next_head
        else:
            head.next = next_head

        return head

print_ll(Solution().removeElements(array_to_ll([1,2,6,3,4,5,6]), 6))
print_ll(Solution().removeElements(array_to_ll([1,1,1,3,4,5,6]), 1))
print_ll(Solution().removeElements(array_to_ll([]), 6))
print_ll(Solution().removeElements(array_to_ll([7,7,7,7]), 6))
print_ll(Solution().removeElements(array_to_ll([7,7,7,7]), 7))
print_ll(Solution().removeElements(array_to_ll([7,7,7,7]), 0))