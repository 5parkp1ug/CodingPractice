from tree import Tree


def dfs(root: Tree) -> None:
    if root:
        dfs(root.left)
        print(root.val)
        dfs(root.right)

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

    dfs(root)