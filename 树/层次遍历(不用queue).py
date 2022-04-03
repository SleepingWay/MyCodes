class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode):
    if root is None:
        return []
    que = [root]
    res = []
    while que:
        res.append([x.val for x in que])
        ll = []
        for x in que:
            if x.left is not None:
                ll.append(x.left)
            if x.right is not None:
                ll.append(x.right)
        que = ll
    return res


def main():
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    print(levelOrder(head))

if __name__ == '__main__':
    main()