from utils import *
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        temp = head
        while temp != None:
            cur = temp.next
            temp.next = last
            last = temp
            temp = cur

        return last

print_ll(Solution().reverseList(array_to_ll([1,2,3,4,5])))
print_ll(Solution().reverseList(array_to_ll([])))
print_ll(Solution().reverseList(array_to_ll([1, 2, 3])))
print_ll(Solution().reverseList(array_to_ll([])))