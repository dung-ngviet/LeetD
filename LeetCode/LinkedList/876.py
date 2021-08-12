from utils import array_to_ll
from utils import ListNode
from typing import Optional

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = head
        result = head
        while temp != None:
            count += 1
            if count % 2 == 0: result = result.next
            temp = temp.next

        return result

print(Solution().middleNode(array_to_ll([1])).val)
print(Solution().middleNode(array_to_ll([1,2])).val)
print(Solution().middleNode(array_to_ll([1,2,3])).val)
print(Solution().middleNode(array_to_ll([1,2,3,4,5])).val)
print(Solution().middleNode(array_to_ll([1,2,3,4,5,6])).val)
