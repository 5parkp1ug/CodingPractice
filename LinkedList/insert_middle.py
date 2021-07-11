from linked_list import LinkedList, Node
from messages import info, success, error


def insert_middle(list: LinkedList, node: Node) -> None:
    middle = list.head
    last = list.head.next

    while last != None and last.next != None:
        print(f'Middle-({middle.data}) Last-({last.data}) Last->Next: {last.next}')
        middle = middle.next
        last = last.next.next
    
    # link middle to new node
    node.next = middle.next
    # link new node to next
    middle.next = node

if __name__ == '__main__':
    # Initialize nodes and create linked list
    list = LinkedList()

    head_node = Node(10)
    second_node = Node(20)
    third_node = Node(30)
    fourth_node = Node(40)
    fifth_node = Node(50)

    list.head = head_node
    head_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = fifth_node
    
    print(info('List before insertion - '))
    list.traverse()

    input_data = int(input('Enter the data to be inserted : '))
    node_to_add = Node(input_data)
    
    insert_middle(list, node_to_add)
    print(success('List after insertion - '))
    list.traverse()