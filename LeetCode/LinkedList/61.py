from utils import *
from typing import Optional

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return head

        temp = head
        count = 1
        while temp.next != None: temp = temp.next; count += 1

        actual_rotate = k % count
        if actual_rotate == 0: return head
        
        temp1 = head
        while count - actual_rotate > 1:
            temp1 = temp1.next
            count -= 1
        
        temp.next, head = head, temp1.next
        temp1.next = None

        return head

# Output: [4,5,1,2,3]
print_ll(Solution().rotateRight(array_to_ll([1,2,3,4,5]), 2))

# Output: [2,0,1]
print_ll(Solution().rotateRight(array_to_ll([0,1,2]), 4))

# Output: [0,1,2]
print_ll(Solution().rotateRight(array_to_ll([0,1,2]), 0))
print_ll(Solution().rotateRight(array_to_ll([0,1,2]), 3))

# Output: []
print_ll(Solution().rotateRight(array_to_ll([]), 4))

# Output: [1]
print_ll(Solution().rotateRight(array_to_ll([1]), 4))
print_ll(Solution().rotateRight(array_to_ll([1]), 0))

# Output: [1,2,0]
print_ll(Solution().rotateRight(array_to_ll([0,1,2]), 2000000000))