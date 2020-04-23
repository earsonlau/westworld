# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
#

#
# class ListNode {
#     int val;
#     ListNode next;
#
#     ListNode(int x) {
#         val = x;
#     }
#
#     public ListNode(int[] nums) {
#         if (nums == null || nums.length == 0) {
#             throw new IllegalArgumentException("arr can not be empty");
#         }
#         this.val = nums[0];
#         ListNode curr = this;
#         for (int i = 1; i < nums.length; i++) {
#             curr.next = new ListNode(nums[i]);
#             curr = curr.next;
#         }
#     }
#
#     @Override
#     public String toString() {
#         StringBuilder s = new StringBuilder();
#         ListNode cur = this;
#         while (cur != null) {
#             s.append(cur.val ).append(" -> ");
#             cur = cur.next;
#         }
#         s.append("NULL");
#         return s.toString();
#     }
# }
#
#
# // 关键在于边界条件的讨论，和代码调试
#
# public class Solution {
#
#     public ListNode rotateRight(ListNode head, int k) {
#         // 特判
#         if (head == null || head.next == null || k == 0) {
#             return head;
#         }
#
#         // 第 1 步：先要知道链表有多少个结点
#         int n = 1;
#         ListNode fastNode = head;
#         while (fastNode.next != null) {
#             fastNode = fastNode.next;
#             n++;
#         }
#         // 此时 fastNode 到末尾结点
#
#         k = k % n;
#         if (k == 0) {
#             return head;
#         }
#         // 第 2 步：找到倒数第 k 个结点，走 n - k - 1 步
#         ListNode slowNode = head;
#         for (int i = 0; i < n - k - 1; i++) {
#             slowNode = slowNode.next;
#         }
#
#         // 第 3 步：穿针引线
#         ListNode newHead = slowNode.next;
#         // 先把尾部接到开头
#         fastNode.next = head;
#         // 再切断原来的连接
#         slowNode.next = null;
#         return newHead;
#     }
# }
