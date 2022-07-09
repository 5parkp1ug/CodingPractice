from tree import Tree


def bfs(root: Tree) -> None:
    queue = []
    queue.insert(0, root)

    while queue:
        node = queue.pop()
        print(node.val)
        if node.left: queue.insert(0, node.left)
        if node.right: queue.insert(0, node.right)

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
    node2.right = node6

    bfs(root)