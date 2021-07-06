class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None  # Initial assignment to None as no node connection exists by default
        

class LinkedList:

    def __init__(self) -> None:
        self.head = None
    
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
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
                raise ValueError('Position greater than the length of the list')
            count += 1
        
        next_node = current_node.next

        current_node.next = node
        node.next = next_node

    def insert_head(self, node) -> None:
        first_node = self.head
        self.head = node
        node.next = first_node
        return

    def search(self, item):
        count = 1
        found = False
        current_node = self.head
        while current_node:
            if current_node.data == item:
                print(f'Item found at the position {count}')
                found = True
                break
            current_node = current_node.next
            count += 1
        if not found:
            print('Item not found in the list')
        

    def size(self) -> int:

        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

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
            data = input('Enter the data: ')
            pos = int(input('Enter the position: '))
            
            node = Node(data=data)
            if pos == 1:
                linked_list.insert_head(node)
            else:
                linked_list.insert(node, pos)
            print('='*48)

        elif option == 2:
            pass

        elif option == 3:
            item = input('Enter the item to search: ')
            linked_list.search(item)

        elif option == 4:
            print('='*15, 'TRAVERSE OPERATION', '='*15)
            linked_list.traverse()
            print('='*50)

        elif option == 5:
            print('='*15, 'SIZE OPERATION', '='*15)
            print(f'The size of the list is {linked_list.size()}')
            print('='*46)

        elif option == 6:
            print('BYE!!!')
            quit()
        