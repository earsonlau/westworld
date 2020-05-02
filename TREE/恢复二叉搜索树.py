# 二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。
#
# 示例 1:
#
# 输入: [1,3,null,null,2]
#
#    1
#   /
#  3
#   \
#    2
#
# 输出: [3,1,null,null,2]
#
#    3
#   /
#  1
#   \
#    2
# 示例 2:
#
# 输入: [3,1,4,null,null,2]
#
#   3
#  / \
# 1   4
#    /
#   2
#
# 输出: [2,1,4,null,null,3]
#
#   2
#  / \
# 1   4
#    /
#   3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def recoverTree(self, root):
        self.mid(root)
        node1 = None
        node2 = None
        for i in range(len(self.res) - 1):
            if self.res[i].val > self.res[i + 1].val and node1 == None:
                node1 = self.res[i]
                node2 = self.res[i + 1]
            elif self.res[i].val > self.res[i + 1].val and node1 != None:
                node2 = self.res[i + 1]

        node1.val, node2.val = node2.val, node1.val

    def mid(self, root):
        if root is not None:
            self.mid(root.left)
            self.res.append(root)
            self.mid(root.right)
