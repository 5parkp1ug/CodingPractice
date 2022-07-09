from tree import Tree

def traverse(node):
	if not node: return []
	result = []
	q = []
	q.append(node)
	q.append(None)
	temp = []
	while q:
		node = q.pop(0)
		# print(node)
		if node:
			temp.append(node.val)
			if node.left: q.append(node.left)
			if node.right: q.append(node.right)
		elif node == None and temp:
			q.append(None)
			result.append(temp)
			temp = []
	return result

if __name__ == '__main__':
    root = Tree(1)

    node1 = Tree(2)
    node2 = Tree(3)
    node3 = Tree(4)
    node4 = Tree(5)
    node5 = Tree(6)
    node6 = Tree(7)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.left.left = node6

    print(traverse(root))