# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#
#递归
# public TreeNode sortedArrayToBST(int[] nums) {
#     return sortedArrayToBST(nums, 0, nums.length);
# }
#
# private TreeNode sortedArrayToBST(int[] nums, int start, int end) {
#     if (start == end) {
#         return null;
#     }
#     int mid = (start + end) >>> 1;
#     TreeNode root = new TreeNode(nums[mid]);
#     root.left = sortedArrayToBST(nums, start, mid);
#     root.right = sortedArrayToBST(nums, mid + 1, end);
#
#     return root;
# }

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self,nums):
        return self.sortedArrayToBST(nums, 0, len(nums))

    def __sortedArrayToBST__(self,nums,start,end):
        if start == end:
            return None
        mid = (start) + end >> 1
        root = TreeNode(nums[mid])
        root.left= self.sortedArrayToBST(nums, start, mid)
        root.right = self.sortedArrayToBST(nums, mid + 1, end)
        return root
