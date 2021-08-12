from utils import *

class Solution:
    def deleteNode(self, node):
        next = node.next
        node.val = next.val
        node.next = next.next

ll = array_to_ll([4,5,1,9])
Solution().deleteNode(find_node(5, ll))
print_ll(ll)

ll = array_to_ll([0,1])
Solution().deleteNode(find_node(0, ll))
print_ll(ll)