from linked_list import LinkedList, Node
from messages import info, success, error

def delete_node(node: Node) -> None:
    # STEP 1: Copy the next node's data into current node
    node.data = node.next.data
    # STEP 2: delete the next node
    node.next = node.next.next

if __name__ == '__main__':
    # Initialize nodes and create linked list
    list = LinkedList()

    head_node = Node(10)
    second_node = Node(20)
    third_node = Node(30)
    fourth_node = Node(40)

    list.head = head_node
    head_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    
    print(info('List before deletion - '))
    list.traverse()

    input_data = int(input('Enter the data to be deleted (1/2/3)? : '))
    if input_data == 1: node_to_delete = head_node
    elif input_data == 2: node_to_delete = second_node
    elif input_data == 3: node_to_delete = third_node
    elif input_data == 4: print(error('Cannot delete last node')); exit()
    else: print(error('Wrong Input')); exit()
    

    delete_node(node_to_delete)
    print(success('List after deletion - '))
    list.traverse()