# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: ListNode, k: int) -> ListNode:
    
    if not head or head.next==None or k == 0:
        return head
    
    left = head
    right = head
    
    length = 1
    count = k
    # move right k places from left
    while k!=0 and right.next!=None:
        right = right.next
        k -= 1
        length += 1
    if not k==0:
        right = head
        k = count % length
        if k == 0:
            return head
        while k!=0:
            right = right.next
            k -= 1
    
    # move left and right till end of list
    while right.next != None:
        left = left.next
        right = right.next
    
    new_head = left.next
    
    left.next= None
    
    right.next = head
    
    head = new_head
    
    return head

if __name__ == '__main__':

    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    new_head = rotateRight(node1, 0)

    while new_head:
        print(new_head.val, ' --> ')
        new_head = new_head.next
