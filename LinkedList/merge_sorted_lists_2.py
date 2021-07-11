from linked_list import LinkedList, Node
from messages import info, success, error


def merge_sorted_lists(list_a: LinkedList, list_b: LinkedList) -> LinkedList:
    
    new_list = LinkedList()

    curr_a = list_a.head
    curr_b = list_b.head

    # compare the heads and insert the first element
    if curr_a.data > curr_b.data:
        new_list.head = curr_b
        curr_b = curr_b.next
    else:
        new_list.head = curr_a
        curr_a = curr_a.next

    curr_new_list = new_list.head

    while curr_a != None and curr_b != None:
        if curr_a.data <= curr_b.data:
            curr_new_list.next = curr_a
            curr_a = curr_a.next
        else:
            curr_new_list.next = curr_b
            curr_b = curr_b.next
        curr_new_list = curr_new_list.next
    
    if curr_a != None:
        curr_new_list.next = curr_a
        curr_a = curr_a.next
        curr_new_list = curr_new_list.next
    
    elif curr_b != None:
        curr_new_list.next = curr_b
        curr_b = curr_b.next
        curr_new_list = curr_new_list.next
    
    return new_list


if __name__ == '__main__':
    # Initialize nodes and create two separate linked lists
    list_a = LinkedList()
    head_node_a = Node(5)
    second_node_a = Node(10)
    third_node_a = Node(15)
    fourth_node_a = Node(40)
    # fifth_node_a = Node(32)

    list_a.head = head_node_a
    head_node_a.next = second_node_a
    second_node_a.next = third_node_a
    third_node_a.next = fourth_node_a
    # fourth_node_a.next = fifth_node_a
    
    list_b = LinkedList()
    head_node_b = Node(2)
    second_node_b = Node(3)
    third_node_b = Node(20)
    # fourth_node_b = Node(25)
    # fifth_node_b = Node(28)

    list_b.head = head_node_b
    head_node_b.next = second_node_b
    second_node_b.next = third_node_b
    # third_node_b.next = fourth_node_b
    # fourth_node_b.next = fifth_node_b

    list_a.traverse()
    list_b.traverse()

    new_list = merge_sorted_lists(list_a, list_b)
    new_list.traverse()
