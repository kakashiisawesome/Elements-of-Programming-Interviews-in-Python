class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchHead(root, head):
    # Search for the head of LL in the tree
    l, r = False, False
    if root.val == head.val:
        if head.next is None:
            return True
        if root.left is not None:
            l = searchHead(root.left, head.next)
        if root.right is not None:
            r = searchHead(root.right, head.next)

    if not l and not r:
        if root.left is not None:
            l = searchHead(root.left, head)
        if root.right is not None:
            r = searchHead(root.right, head)


    return l or r


def isSubPath(root, head):
    if head is None or root is None:
        return False
    return searchHead(root, head)

if __name__ == '__main__':
    one = TreeNode(1)
    f1 = TreeNode(4)
    f2 = TreeNode(4)
    t1 = TreeNode(2)
    t2 = TreeNode(2)
    o2 = TreeNode(1)
    o3 = TreeNode(1)
    six = TreeNode(6)
    eight = TreeNode(8)
    three = TreeNode(3)
    nine = TreeNode(9)
    ten = TreeNode(10)

    one.right = o2
    o2.left = ten
    o2.right = o3
    ten.left = nine

    # f1.right = t1
    # t1.left = o2
    #
    # f2.left = t2
    # t2.left = six
    # t2.right = eight
    # eight.left = o3
    # eight.right = three

    head = ListNode(1, ListNode(10))
    print(isSubPath(one, head))