# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
#  注意:
# 你可以假设树中没有重复的元素。
#
#  例如，给出
#
#  中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
#
#  返回如下的二叉树：
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  Related Topics 树 深度优先搜索 数组

"""
思路:
后序遍历是左-右-根，因此postorder[-1]一定是整个树的根。
由于题目说明了没有重复元素，因此我们可以通过val去inorder找到根在inorder中的索引i。
所以左子树的中序遍历序列是inorder[:i],右子树的中序遍历序列是inorder[i+1:](inorder[i]是根节点)
左子树的后序遍历序列是postorder[:i],右子树的后序遍历序列是postorder[i:-1](postorder[-1]=是根节点)
"""

from typing import List

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int])  :
        # 实际上inorder 和 postorder一定是同时为空的，因此你无论判断哪个都行
        if not inorder:
            return None
        # 后序遍历是左右根，因此postorder最后一个元素一定整个树的根。
        # 由于题目说明了没有重复元素，因此我们可以通过val去inorder找到根在inorder中的索引i。
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        print("the index of root:",i)
        root.left = self.buildTree(inorder[:i], postorder[:i])#inorder[:i]= inorder[0到i-1](左闭右开)
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root