# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。

# 递归、栈循环实现深度优先遍历；用队列循环实现层遍历。
# //深度优先：递归版

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self,root:TreeNode ):
        if (root is None):
            return 0
        l = self.maxDepth(root.left)+1
        r = self.maxDepth(root.right)+1
        if l>r:
            return l
        else:
            return r

#深度优先：栈的循环版

#广度优先：使用队列