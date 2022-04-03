from queue import Queue


class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.left is None:
            self.left = TreeNode(data)
        elif self.left is not None:
            self.left.insert(data)
        elif self.right is None:
            self.right = TreeNode(data)
        else:
            self.right.insert(data)


def preOrderPrintTree_dg(head: TreeNode):   # 先序递归
    if not head:
        return
    print(head.data, end=" ")
    preOrderPrintTree_dg(head.left)
    preOrderPrintTree_dg(head.right)


def preOrderPrintTree_fdg(head: TreeNode):  # 先序非递归
    print("Pre-order : ", end=" ")
    if not head:
        return
    stack = [head]
    while len(stack) != 0:
        head = stack.pop()
        print(head.data, end=" ")
        if head.right:
            stack.append(head.right)
        if head.left:
            stack.append(head.left)


def midOrderPrintTree_dg(head: TreeNode):   # 中序递归
    if not head:
        return
    midOrderPrintTree_dg(head.left)
    print(head.data, end=" ")
    midOrderPrintTree_dg(head.right)


def midOrderPrintTree_fdg(head: TreeNode):  # 中序非递归
    print("Mid-order : ", end=" ")
    if head is None:
        return
    stack = []
    while len(stack) != 0 or head is not None:
        if head:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            print(head.data, end=" ")
            head = head.right


def postOrderPrintTree_dg(head: TreeNode):  # 后序递归
    if head is None:
        return
    postOrderPrintTree_dg(head.left)
    postOrderPrintTree_dg(head.right)
    print(head.data, end=" ")


def postOrderPrintTree_fdg(head: TreeNode):  # 后序非递归
    print("Post-order : ", end=" ")
    if head is None:
        return
    stack = [head]
    tmp = []
    while len(stack) != 0:
        head = stack.pop()
        tmp.append(head)
        if head.left is not None:
            stack.append(head.left)
        if head.right is not None:
            stack.append(head.right)
    while len(tmp) != 0:
        print(tmp.pop().data, end=" ")


def levelOrderPrintTree(head: TreeNode):    # 层次遍历
    print("Level-order : ", end=" ")
    if head is None:
        return
    que = Queue()
    que.put(head)
    while not que.empty():
        head = que.get()
        print(head.data, end=" ")
        if head.left is not None:
            que.put(head.left)
        if head.right is not None:
            que.put(head.right)


def main():
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    # preOrderPrintTree_dg(head)
    # preOrderPrintTree_fdg(head)
    # midOrderPrintTree_dg(head)
    # midOrderPrintTree_fdg(head)
    # postOrderPrintTree_dg(head)
    # postOrderPrintTree_fdg(head)
    levelOrderPrintTree(head)

if __name__ == "__main__":
    main()
