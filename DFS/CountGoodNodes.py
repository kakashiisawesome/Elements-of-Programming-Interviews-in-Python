class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countGoodNodes(root, path):
    if root is None:
        return 0

    c = 1
    newPath = []

    for i in path:
        newPath.append(i)

    for i in newPath:
        if i > root.val:
            c = 0
            break

    newPath.append(root.val)

    return c + countGoodNodes(root.left, newPath) + countGoodNodes(root.right, newPath)


def goodNodes(root):
    return countGoodNodes(root, [])


r = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
print(countGoodNodes(r, []))