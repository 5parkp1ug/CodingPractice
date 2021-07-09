# Linked list class used everywhere else
from messages import warning, info, success

class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None  # Initial assignment to None as no node connection exists by default      

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def delete(self, item):
        current_node = self.head
        previous_node = None
        while current_node.data != item:
            if current_node.next == None:  # Check & return if it is the last item
                print(error("Item not found in the list"))
                return
            previous_node = current_node
            current_node = current_node.next
        
        if current_node == self.head:
            self.head = self.head.next
        else: 
            previous_node.next = current_node.next
        print(warning(f'Deleted the Node with data {item}!'))
        
    def insert(self, node, pos) -> None:

        # check if the linked list is empty. If so, insert at head
        if not self.head:
            self.head = node
            return

        count = 1
        current_node = self.head
        while(count != pos-1):
            current_node = current_node.next
            if not current_node:
                print(error('Position greater than the length of the list'))
                return
            count += 1
        
        next_node = current_node.next

        current_node.next = node
        node.next = next_node
        print(success(f'Node inserted at position {pos}'))

    def insert_head(self, node) -> None:
        first_node = self.head
        self.head = node
        node.next = first_node
        print(success('Item inserted at HEAD'))
        return

    def insert_tail(self, node) -> None:
        # check if list is empty insert at the head
        if not self.head:
            self.insert_head(node)
            return
        # iterate till last node i.e., node's next = None
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = node
        print(success('Item inserted at TAIL'))

    def search(self, item):
        count = 1
        found = False
        current_node = self.head
        while current_node:
            if current_node.data == item:
                print(success(f'Item found at the position {count}'))
                found = True
                break
            current_node = current_node.next
            count += 1
        if not found:
            print(warning('Item not found in the list'))  

    def size(self) -> int:

        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        print(success(f'The size of the list is {count}'))

    def traverse(self):
        disp = ''
        current_node = self.head
        while current_node != None:
            disp += f'{current_node.data} --> '
            current_node = current_node.next
        print(disp.strip('--> '))
