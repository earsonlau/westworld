# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#思路：
# 对preorder数组而言，树T的结点落在preorder[p_start,p_end]
# 对inorder数组而言， 树T的结点落在inorder[i_start,i_end]
# preorder[p_start]根节点root
# 寻找中序数组里root的位置，记为i_root_index
# i_root_index-i_start记为leftnum (表示根节点跟最左节点的距离)
# 在前序数组里，树T的左子树T_leftchild结点落在preorder[p_start+1...p_start + left_num + 1]
# 在前序数组里，树T的右子树T_rightchild结点落在preorder[p_start + left_num + 1...p_end]
# 在中序数组里，树T的左子树T_leftchild结点落在inorder[i_start...i_root_index ]
# 在中序数组里，树T的右子树T_rightchild结点落在preorder[i_root_index 1...i_end]

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    return buildTreeHelper(preorder, 0, len(preorder), inorder, 0, len(inorder))

def buildTreeHelper(preorder,  p_start,  p_end, inorder,  i_start,  i_end):
    # // preorder 为空，直接返回 null
    if p_start == p_end:
        return None
    root_val = preorder[p_start]#根节点是前序遍历的第一个节点
    root = TreeNode(root_val)
    # //在中序遍历中找到根节点的位置
    i_root_index = inorder.index(root_val)#根节点索引
    leftNum = i_root_index - i_start
    # //递归的构造左子树
    root.left = buildTreeHelper(preorder, p_start + 1, p_start + leftNum + 1, inorder, i_start, i_root_index);
    # //递归的构造右子树
    root.right = buildTreeHelper(preorder, p_start + leftNum + 1, p_end, inorder, i_root_index + 1, i_end)
    return root

#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
print(buildTree([3,9,20,15,7],[9,3,15,20,7]))
# 上边的代码很好理解，但存在一个问题，在中序遍历中找到根节点的位置每次都得遍历中序遍历的数组去寻找，
# 参考这里 ，我们可以用一个HashMap把中序遍历数组的每个元素的值和下标存起来，这样寻找根节点的位置就可以直接得到了。
#
# def buildTree(preorder, inorder):
#     inorder_map={}
#     for i in range(len(inorder)):
#         inorder_map[inorder[i]] = i
#     return buildTreeHelper(preorder, 0, len(preorder), inorder, 0, len(inorder), map)
#
# def buildTreeHelper(preorder, p_start, p_end, inorder, i_start, i_end, map):
#     if p_start == p_end:
#         return None
#     root_val = preorder[p_start]
#     root = TreeNode(root_val)
#     i_root_index = map[root_val]#用哈希表查找根的索引
#     leftNum = i_root_index - i_start
#     root.left = buildTreeHelper(preorder, p_start + 1, p_start + leftNum + 1, inorder, i_start, i_root_index, map)
#     root.right = buildTreeHelper(preorder, p_start + leftNum + 1, p_end, inorder, i_root_index + 1, i_end, map)
#     return root
