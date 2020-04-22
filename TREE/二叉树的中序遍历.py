class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(self, root: TreeNode):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # leetcode submit region end(Prohibit modification and deletion)
    WHITE, GRAY = 0, 1
    res = []
    stack = [(WHITE, root)]

    while stack:
        color, node = stack.pop()

        if node is None:
            continue
        print("pop一下,我发现了", node.val,"是",color, "色的")
        if color == WHITE:
            stack.append((WHITE, node.right))
            if node.right:
                print((node.right).val, "变成白色")

            stack.append((GRAY, node))
            if node:
                print(node.val, "变成灰色")

            stack.append((WHITE, node.left))

            if node.left:
                print((node.left).val, "变成白色")
        else:
            res.append(node.val)
            print("把",node.val,"加入res")
    print("遍历次序:",res)
    return res