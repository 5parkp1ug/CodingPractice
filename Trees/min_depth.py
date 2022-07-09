from tree import Tree


level = 0

def min_depth(root: Tree, level: int) -> int:
	if root.left == None and root.right==None:
		return level
	
	level += 1

	if root.left == None and root.right:
		return min_depth(root.right, level)
	elif root.right == None and root.left:
		return min_depth(root.left, level)
	
	return min(min_depth(root.left, level), min_depth(root.right, level))

if __name__ == '__main__':
	root = Tree(1)

	node1 = Tree(2)
	node2 = Tree(3)
	node3 = Tree(4)
	node4 = Tree(5)
	node5 = Tree(6)
	node6 = Tree(7)

	root.left = node1
	root.left.left = node2
	root.left.left.left = node3
	root.left.left.left.left = node4
	root.left.left.left.left.left = node5
	root.left.left.left.left.left.left = node6

	print(min_depth(root, 0))