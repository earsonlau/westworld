# 给定一个二叉树
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#
#
#
# 进阶：
#
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
#
#
# 递归法平凡版，无复杂指针
#
# 核心是getNextNoNullChild，根据root，找到下一级右手第一个
# 然后分情况讨论，对每个节点：
# 左子右子都有，则左子next指向右子，右子next指向getNextNoNullChild
# 只有左子，左子指向getNextNoNullChild，
# 只有右子，右子指向getNextNoNullChild，
#
# 注意：递归时要先递归右子树，否则上级节点next关系没建好，下级无法成功getNextNoNullChild
#
#
#
#
#
#
# // package com.leetcode.explore.learnCard.dataStructureBinaryTree.conclusion4;
#
# /**
#  * 补充节点的右侧指针，不是完美二叉树
#  */
# public class Solution {
#     public Node connect(Node root) {
#         if (root == null || (root.right == null && root.left == null)) {
#             return root;
#         }
#         if (root.left != null && root.right != null) {
#             root.left.next = root.right;
#             root.right.next = getNextNoNullChild(root);
#         }
#         if (root.left == null) {
#             root.right.next = getNextNoNullChild(root);
#         }
#         if (root.right == null) {
#             root.left.next = getNextNoNullChild(root);
#         }
#
#         //这里要注意：先递归右子树，否则右子树根节点next关系没建立好，左子树到右子树子节点无法正确挂载
#         root.right = connect(root.right);
#         root.left = connect(root.left);
#
#         return root;
#     }
#
#     /**
#      * 一路向右找到有子节点的根节点
#      */
#     private static Node getNextNoNullChild(Node root) {
#         while (root.next != null) {
#             if (root.next.left != null) {
#                 return root.next.left;
#             }
#             if (root.next.right != null) {
#                 return root.next.right;
#             }
#             root = root.next;
#         }
#         return null;
#     }
# }
#

# 解法2：
# 纵向是二叉树，横向是链表，两层嵌套循环，主循环处理各层，子循环处理每层节点的各子节点。
# 定义3个变量，分别标记：下一层头节点head，下一层已遍历到的前置节点pre，以及当前层处理的游标cur：
#
# 总初始化：下一层要处理的头节点head=root
# 各层初始化：当前层处理游标节点cur用head更新赋值，而后pre=head=None，表示下一层尚未找到前置和头节点
# 对当前层游标节点cur进行处理，对左右子节点分别判断：
# 如果下一层尚未找到前置节点，则意味着该左/右子节点就是下一层的头节点，于是更新pre=head=该子节点
# 如果pre已赋值，则直接更新pre的next到当前的左/右子节点，然后pre更新到其next值
# cur游标更新到下一个值
# 根据更新后的head，处理下一层
#
# 作者：luanz
# 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/solution/gai-xie-de-guan-fang-die-dai-fa-geng-jia-qing-xi-y/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:#当前层的头节点
            cur = head #当前层处理节点
            pre = head = None#初始化下一层头节点和前置节点
            while cur:
                if cur.left:
                    if not pre:#若尚未找到下一层前置节点，则同步更新下一层头节点和前置节点
                        pre = head =cur.left
                    else:#已找到下一层前置节点，则将前置节点指向当前子节点，并前移pre
                        pre.next = cur.left
                        pre = pre.next
                if cur.right:
                    if not pre:
                        pre = head = cur.right
                    else:
                        pre.next = cur.right
                        pre = pre.next
                cur = cur.next
        return root
#
# 作者：luanz
# 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/solution/gai-xie-de-guan-fang-die-dai-fa-geng-jia-qing-xi-y/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。