
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def validateBST(root, arr):

    if root is None:
        return

    validateBST(root.left, arr)

    arr.append(root.val)

    validateBST(root.right, arr)


def f(root):
    arr = []
    validateBST(root, arr)
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            return False

    return True
