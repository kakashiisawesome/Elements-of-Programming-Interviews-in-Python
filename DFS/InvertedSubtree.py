
class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getSubTreesWithRoot(target, root, result):
    # Search for target node in root tree

    if root.val == target.val:
        result.append(root)

    if root.left:
        getSubTreesWithRoot(target, root.left, result)
    if root.right:
        getSubTreesWithRoot(target, root.right, result)



def isEqual(source, target):

    if source is None:
        return target is None
    else:
        if target is None:
            return False

    s, t = [], []

    if source.left:
        s.append(source.lef.val)
    if source.right:
        s.append(source.right.val)

    if target.left:
        t.append(target.left.val)
    if target.right:
        t.append(target.right.val)

    s.sort()
    t.sort()

    if s == t:
        return isEqual(source.left)


    # if source is None:
    #     return target is None
    # else:
    #     if target is None:
    #         return False
    #
    #     if source.val != target.val:
    #         return False





def solve(source, target):
    if source is None:
        return target is None

    subtrees = []
    getSubTreesWithRoot(source, target, subtrees)


s = Tree(0, Tree(1, None, Tree(3)), Tree(2))
t = Tree(5, Tree(2), Tree(0, Tree(2), Tree(1, Tree(3))))

solve(s, t)

a = [None,2,3]
a.sort()
b = [2,3,None]
b.sort()
print(a == b)