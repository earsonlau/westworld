# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
#
# 递归

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self,root: TreeNode,sum):
        if root is None:
            return False
        return self.hasPathSumHelper(self,root,sum)
    def hasPachSumHelper(self,root: TreeNode,sum):
        #到达叶子节点
        if root.left is None and root.right is None:
            return root.val == sum
        #左孩子为 null
        if root.left is None:
            return self.hasPachSumHelper(root.right, sum - root.val)
        #右孩子为 null
        if root.right is None:
            return self.hasPachSumHelper(root.left, sum - root.val) or self.hasPachSumHelper(root.left, sum - root.val)