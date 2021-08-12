from utils import *

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        origin_list1 = list1

        start_node = list1
        b = b - a
        while a > 1:
            a -= 1
            start_node = list1 = list1.next
        
        end_node = start_node
        while b > 0:
            b -= 1
            end_node = list1 = list1.next

        endlist2 = list2
        while endlist2.next != None: endlist2 = endlist2.next

        start_node.next = list2
        endlist2.next = end_node

        return origin_list1


print_ll(Solution().mergeInBetween(array_to_ll([0,1,2,3,4,5]), 3, 4, array_to_ll([1000000,1000001,1000002])))
print_ll(Solution().mergeInBetween(array_to_ll([0,1,2,3,4,5,6]), 2, 5, array_to_ll([1000000,1000001,1000002,1000003,1000004])))
print_ll(Solution().mergeInBetween(array_to_ll([9,9,9]), 1, 2, array_to_ll([1,2,3,4,5])))