from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Pair:
    def __init__(self, parent, depth):
        self.parent = parent
        self.depth = depth


def traverse(root, target, parent, depth):
    l, r = None, None
    if root.val == target:
        return Pair(parent, depth)
    if root.left:
        l = traverse(root.left, target, root.val, depth+1)
    if l is None:
        if root.right:
            return traverse(root.right, target, root.val, depth+1)

    return l


def isCousins(root, x, y):
    pair1 = traverse(root, x, -1, 0)
    pair2 = traverse(root, y, -1, 0)

    return pair1.depth == pair2.depth and pair1.parent != pair2.parent


r = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
print(isCousins(r, 4, 5))