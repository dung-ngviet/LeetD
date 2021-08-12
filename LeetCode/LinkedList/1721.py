from utils import *
from typing import Optional

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        origin_head = head

        kth_begin = None
        kth_end = head
        while head != None:
            count += 1
            if count == k:
                kth_begin = head
            elif count >=k:
                kth_end = kth_end.next

            head = head.next
        
        kth_begin.val, kth_end.val = kth_end.val, kth_begin.val

        return origin_head

# class Solution:
#     def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if not head:
#             return None
#         ptr1=head
#         while k>1:
#             ptr1=ptr1.next
#             k-=1
#         j=ptr1.next
#         ptr2=head
#         while j:
#             j=j.next
#             ptr2=ptr2.next
#         ptr1.val,ptr2.val=ptr2.val,ptr1.val

#         return head

print_ll(Solution().swapNodes(array_to_ll([1,2,3,4,5]), 2))
print_ll(Solution().swapNodes(array_to_ll([1,2,3,4,5]), 3))
print_ll(Solution().swapNodes(array_to_ll([1,2,3,4,5]), 5))
print_ll(Solution().swapNodes(array_to_ll([7,9,6,6,7,8,3,0,9,5]), 5))
print_ll(Solution().swapNodes(array_to_ll([1]), 1))
print_ll(Solution().swapNodes(array_to_ll([1,2]), 1))
print_ll(Solution().swapNodes(array_to_ll([1,2,3]), 2))