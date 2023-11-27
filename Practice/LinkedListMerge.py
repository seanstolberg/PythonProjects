# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]):
    # create a dummy head node to serve as the head of the merged LL
    dummy_head = ListNode()

    # initialize a pointer to the current node in the merged list
    current = dummy_head

    #traverse both lists simulataneously
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    #after merging, if any list still has remaining nodes, append them to the merged list
    if list1:
        current.next = list1
    if list2:
        current.next = list2

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
list1 = createLinkedList([1, 2, 4])
list2 = createLinkedList([1, 3, 4])
merged_list1 = mergeTwoLists(list1, list2)
print(linkedListToList(merged_list1))  # Output: [1, 1, 2, 3, 4, 4]

# Example 2
list3 = createLinkedList([])
list4 = createLinkedList([])
merged_list2 = mergeTwoLists(list3, list4)
print(linkedListToList(merged_list2))  # Output: []

# Example 3
list5 = createLinkedList([])
list6 = createLinkedList([0])
merged_list3 = mergeTwoLists(list5, list6)
print(linkedListToList(merged_list3))  # Output: [0]