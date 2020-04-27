
# 给定两个二叉树，编写一个函数来检验它们是否相同。
#
#  如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
#  示例 1:
#
#  输入:       1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# 输出: true
#
#  示例 2:
#
#  输入:      1          1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# 输出: false
#
#
#  示例 3:
#
#  输入:       1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# 输出: false
#
#  Related Topics 树 深度优先搜索




def isSameTree(root1, root2):
    # // 都为空的话，显然相同
    if (root1 is None and root2 is None): return True
    # // 一个为空，一个非空，显然不同
    if (root1 is None or root2 is None): return False
    # // 两个都非空，但 val 不一样也不行
    if (root1.val != root2.val): return False
    # // root1 和 root2 该比的都比完了
    return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
