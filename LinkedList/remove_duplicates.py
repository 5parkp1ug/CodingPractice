from linked_list import LinkedList, Node
from messages import info, success, error


def remove_duplicate(list: LinkedList) -> None:
    
    current_node = list.head

    while current_node != None:
        while (current_node.next != None) and (current_node.next.data == current_node.data):
            current_node.next = current_node.next.next
        current_node = current_node.next

if __name__ == '__main__':
    # Initialize nodes and create linked list
    list = LinkedList()

    head_node = Node(10)
    second_node = Node(30)
    third_node = Node(40)
    fourth_node = Node(50)
    fifth_node = Node(50)

    list.head = head_node
    head_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = fifth_node
    
    print(info('List before deletion - '))
    list.traverse()
    
    remove_duplicate(list)
    print(success('List after deletion - '))
    list.traverse()