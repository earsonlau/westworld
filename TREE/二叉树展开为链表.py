# 给定一个二叉树，原地将它展开为链表。
#
# 例如，给定二叉树
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
# 解法一
# 可以发现展开的顺序其实就是二叉树的先序遍历。算法和 94 题中序遍历的 Morris 算法有些神似，我们需要两步完成这道题。
#
# 将左子树插入到右子树的地方
# 将原来的右子树接到左子树的最右边节点
# 考虑新的右子树的根节点，一直重复上边的过程，直到新的右子树为 null

def flatten(root):
    while root is not None:
    #左子树为 null, 直接考虑下一个节点
        if root.left is None:
            root = root.right
    else:
        #找左子树最右边的节点
        pre = root.left
        while(pre.right is not None):
            pre = pre.right
        #将原来的右子树接到左子树的最右边节点
        pre.right =root.right
        #将左子树插入到右子树地方
        root.right = root.left
        root.left = None
        #考虑下一个节点
        root = root.right