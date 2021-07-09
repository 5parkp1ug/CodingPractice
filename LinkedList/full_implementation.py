# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Linked list implementation with Insert, Delete, Search and
#                Traverse operations
# ==============================================================================

from linked_list import LinkedList, Node

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
        