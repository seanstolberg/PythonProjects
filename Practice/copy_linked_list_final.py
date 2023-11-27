class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def clone_linked_list(head):
    if not head:
        return None
    
    # create a dict to map original nodes to their clone couterparts
    node_map = {}
    
    # iterate through the orginal linked list to created the clone and the mapping
    original_node = head
    while original_node:
        node_map[original_node] = Node(original_node.data)
        original_node = original_node.next
        
    # Iterate through the original list again to set the next pointers in the cloned list
    original_node = head
    while original_node:
        if original_node.next:
            node_map[original_node].next = node_map[original_node.next]
        original_node = original_node.next
        
    return node_map[head]
    
    

#######################
# Create original linked list
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