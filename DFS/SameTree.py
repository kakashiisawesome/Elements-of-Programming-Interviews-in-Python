

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    if p is None:
        if q is not None:
            return False
        return True
    else:
        if q is None:
            return False

        if p.val != q.val:
            return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)



one = TreeNode(1, TreeNode(2))

two = TreeNode(1, None, TreeNode(3))

print(isSameTree(one, two))