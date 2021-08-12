# Definition for singly-linked list.
from utils import array_to_ll
from utils import ListNode

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ret = 0
        temp = head
        while temp != None:
            ret = (ret << 1) + temp.val
            temp = temp.next
        
        return ret

print(Solution().getDecimalValue(array_to_ll([1,0,1])))
a = 0
print(a << 1)
print(a + 1 << 1)