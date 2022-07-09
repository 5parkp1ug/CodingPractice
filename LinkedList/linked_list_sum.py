"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the 
two numbers do not contain any leading zero, except the number 0 itself.

Example - 
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


from linked_list import LinkedList, Node

def linked_list_sum(linked_list1: LinkedList, linked_list2: LinkedList) -> LinkedList:
    curr_1 = linked_list1.head
    curr_2 = linked_list2.head

    list_sum = LinkedList()

    # calculate sum of heads and assign the head of list_sum linked list
    sum = curr_1.data + curr_2.data
    curr_data = sum % 10
    carry = int(sum/10)
    
    list_sum.head = Node(curr_data)

    curr_1 = curr_1.next
    curr_2 = curr_2.next
    curr_list_sum = list_sum.head

    while curr_1 and curr_2:
        # print(f"{curr_1.data} + {curr_2.data} + {carry}")
        curr_sum = curr_1.data + curr_2.data + carry

        curr_data = curr_sum % 10
        carry = int(curr_sum/10)
        # print(f"Curr Sum = {curr_sum} Current data - {curr_data} New Carry - {carry}")
        curr_list_sum.next = Node(curr_data)
        
        curr_1 = curr_1.next
        curr_2 = curr_2.next
        curr_list_sum = curr_list_sum.next

    # add remaining list
    if (curr_1 or curr_2):
        remaining_list = curr_1 if curr_1 else curr_2

        while remaining_list:
            curr_sum = remaining_list.data + carry
            curr_data = curr_sum % 10
            carry = int(curr_sum/10)
            curr_list_sum.next = Node(curr_data)

            remaining_list = remaining_list.next
            curr_list_sum = curr_list_sum.next
    
    # check if carry exists
    if carry:
        curr_list_sum.next = Node(carry)
    
    return list_sum
        


if __name__ == '__main__':
    # Initialize nodes and create two separate linked lists
    list_a = LinkedList()
    head_node_a = Node(9)
    second_node_a = Node(9)
    third_node_a = Node(9)
    fourth_node_a = Node(9)
    fifth_node_a = Node(9)
    sixth_node_a = Node(9)
    seventh_node_a = Node(9)

    list_a.head = head_node_a
    head_node_a.next = second_node_a
    second_node_a.next = third_node_a
    third_node_a.next = fourth_node_a
    fourth_node_a.next = fifth_node_a
    fifth_node_a.next = sixth_node_a
    sixth_node_a.next = seventh_node_a
    
    list_b = LinkedList()
    head_node_b = Node(9)
    second_node_b = Node(9)
    third_node_b = Node(9)
    fourth_node_b = Node(9)

    list_b.head = head_node_b
    head_node_b.next = second_node_b
    second_node_b.next = third_node_b
    third_node_b.next = fourth_node_b

    sum = linked_list_sum(list_a, list_b)

    sum.traverse()