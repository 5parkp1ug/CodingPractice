#!/usr/bin/env python3
# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Reversing linked list by reversing the links consecutively 
# ==============================================================================

class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None  # Initial assignment to None as no node connection exists by default      

class LinkedList:

    def __init__(self) -> None:
        self.head = None
    
    def traverse(self):
        disp = ''
        current_node = self.head
        while current_node != None:
            disp += f'{current_node.data} --> '
            current_node = current_node.next
        print(disp.strip('--> '))

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