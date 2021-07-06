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


if __name__ == '__main__':

	# Initialize the nodes
	first_node = Node(1)
	second_node = Node('This is second node')
	third_node = Node({'a':1, 'b': 2})

	# Create the list
	linked_list = LinkedList()
	linked_list.head = first_node
	linked_list.head.next = second_node
	second_node.next = third_node

	linked_list.traverse()