from typing import List
from typing import TypeVar
T = TypeVar('T')

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def array_to_ll(arr: List[T]) -> ListNode:
    head = None
    cur = None
    for element in arr:
        if head == None:
            head = ListNode(element)
            cur = head
        else:
            cur.next = ListNode(element)
            cur = cur.next

    return head

def print_ll(node: ListNode):
    element = []
    cur = node
    while cur != None:
        element.append(cur.val)
        cur = cur.next
    print(element)

def find_node(val_to_find, head: ListNode) -> ListNode:
    cur = head
    while cur != None:
        if cur.val == val_to_find:
            return cur
        cur = cur.next

    return None