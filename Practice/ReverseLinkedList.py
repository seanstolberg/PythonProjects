
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of the result list
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        # Initialize two pointers to track the nodes before and after the sublist to be reversed
        prev = dummy_head
        for _ in range(left - 1):
            prev = prev.next
        current = prev.next

        # Reverse the sublist by changing next pointers
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        # Return the head of the reversed list
        return dummy_head.next

# Helper function to create a linked list from a list
def createLinkedList(values):
    dummy_head = ListNode()
    current = dummy_head
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next


# Helper function to create a linked list from a list
def createLinkedList(values):
    dummy_head = ListNode()
    current = dummy_head
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

# Helper function to convert a linked list to a list
def linkedListToList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example 1
list1 = createLinkedList([1, 2, 3, 4, 5])
reversed_list1_iterative = Solution.reverseBetween(list1, left = 2, right = 4)
print(linkedListToList(reversed_list1_iterative))  # Output: [5, 4, 3, 2, 1]

# Example 3
list3 = createLinkedList([5])
reversed_list3_recursive = Solution.reverseBetween(list3, left = 1, right = 1)
print(linkedListToList(reversed_list3_recursive))  # Output: [5]