#!/usr/bin/env python3
# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Linked list implementation with Insert, Delete, Search and
#                Traverse operations
# ==============================================================================

def success(message):
    return f'\033[92m{message}\033[0m'

def info(message):
    return f'\033[94m{message}\033[0m'

def error(message):
    return f'\033[91m{message}\033[0m'

def warning(message):
    return f'\033[93m{message}\033[0m'

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
        if self.head == None: 
            print(warning('Empty list'))
            return
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next


if __name__ == '__main__':

    linked_list = LinkedList()
    
    while(True):
        
        print('Select an Option (1-5)')
        print('1. Insert')
        print('2. Delete')
        print('3. Search')
        print('4. Print')
        print('5. Size')
        print('6. Exit')
        option = int(input('Enter the option: '))
        
        if option == 1:
            print('='*15, 'INSERT OPERATION', '='*15)
            print('\033[92m TIP: For position enter 1 for Head and leave blank for tail \033[0m ')
            data = input('Enter the data: ')
            pos = int(input('Enter the position: ') or -1)
            
            node = Node(data=data)
            if pos == 1:
                linked_list.insert_head(node)
            elif pos == -1:
                linked_list.insert_tail(node)
            else:
                linked_list.insert(node, pos)
            print('='*48)

        elif option == 2:
            print('='*15, 'DELETE OPERATION', '='*15)
            item = input('Enter the item to delete: ')
            linked_list.delete(item)
            print('='*48)

        elif option == 3:
            print('='*15, 'SEARCH OPERATION', '='*15)
            item = input('Enter the item to search: ')
            linked_list.search(item)
            print('='*48)

        elif option == 4:
            print('='*15, 'TRAVERSE OPERATION', '='*15)
            linked_list.traverse()
            print('='*50)

        elif option == 5:
            print('='*15, 'SIZE OPERATION', '='*15)
            linked_list.size()
            print('='*46)

        elif option == 6:
            print('BYE!!!')
            quit()
        