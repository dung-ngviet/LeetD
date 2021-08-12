from utils import *
from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        origin_head = head

        while head:
            next = head.next
            if next != None and head.val == next.val:
                head.next = next.next
            else:
                head = next

        return origin_head

print_ll(Solution().deleteDuplicates(array_to_ll([])))
print_ll(Solution().deleteDuplicates(array_to_ll([1])))
print_ll(Solution().deleteDuplicates(array_to_ll([1,1,2])))
print_ll(Solution().deleteDuplicates(array_to_ll([1,1,1,1,1,2])))
print_ll(Solution().deleteDuplicates(array_to_ll([1,1,2,3,3])))
print_ll(Solution().deleteDuplicates(array_to_ll([1,2,3,4,5,6])))