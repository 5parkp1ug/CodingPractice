from linked_list import LinkedList, Node
from messages import info, success, error


def find_kth_item(list: LinkedList, k: int) -> Node:
    kth_node = list.head
    last_node = list.head
    kth_node_start = None

    # move last node to k elements forward
    count = 1
    while count <= k:
        if not last_node:
            print(error('k greater than list'))
            exit()
        last_node = last_node.next
        if count == 1: kth_node_start = list.head
        else: kth_node_start = kth_node_start.next
        count += 1
    
    # move kth_node and last_node till last_node reaches the end
    while last_node:
        kth_node = kth_node.next
        last_node = last_node.next

    return kth_node_start, kth_node

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
    
    list.traverse()

    k = int(input('Enter the value of k : '))
    
    start, end = find_kth_item(list, k)
    print(success(f'The kth node from start & end is - {start.data} &  {end.data}'))