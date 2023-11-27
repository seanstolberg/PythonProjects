class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def clone_linked_list(head):
    if not head:
        return None
    
    #create a dictionary to map original nodes to their cloned couterparts
    node_map = {}

    #iterate through the original linked list to create the clone and the mapping
    original_node = head
    while original_node:
        node_map[original_node] = Node(original_node.data)
        original_node = original_node.next
    
    # Iterate through the original list again to set the 'next' pointers in cloned list
    original_node = head
    while original_node:
        if original_node.next:
            node_map[original_node].next = node_map[original_node.next]
        original_node = original_node.next

    # Return the head of the cloned list
    return node_map[head]


# Create ogirinal linked list
original_head = Node(1)
original_head.next = Node(2)
original_head.next.next = Node(3)

# clone the linked list
cloned_head = clone_linked_list(original_head)

# test the cloned list
original_node = original_head
while original_node:
    print(original_node.data, end=" -> ")
    original_node = original_node.next

print("None")

print("Cloned linked list:")
cloned_node = cloned_head
while cloned_node:
    print(cloned_node.data, end=" -> ")
    cloned_node = cloned_node.next