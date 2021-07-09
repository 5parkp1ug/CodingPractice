# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Reversing linked list by reversing the links consecutively 
# ==============================================================================

from linked_list import LinkedList, Node

def insert_nodes(count: int) -> LinkedList:
    list = LinkedList()

    node_list = []
    # create nodes and add them to list
    for num in range(count):
        node = Node(num)
        node_list.append(node)
    
    # add head node to the list
    head_node = node_list.pop(0)
    list.head = head_node
    previous_node = head_node

    for i in node_list:
        previous_node.next = i
        previous_node = i
    
    print(f'\033[92m [+] Inserted {count} nodes \033[0m')
    return list

def reverse(list) -> LinkedList:
    previous_node = None
    next_node = None
    head = list.head
    current_node = list.head

    while current_node:
        # store the next node
        next = current_node.next
        # reverse the link
        current_node.next = previous_node
        # move previous node to next position for next iteration
        previous_node = current_node
        # move current node to next position for next iteration
        current_node = next
    
    # change the head to the previous node which has traversed to last node
    list.head = previous_node

    return list
    
    
if __name__ == '__main__':
    list = insert_nodes(50)
    print('\033[92m [+] Before Reversing \033[0m')
    list.traverse()
    print('\033[92m [+] After Reversing \033[0m')
    reverse(list)
    list.traverse()