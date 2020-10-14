# # 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# #
# # 示例:
# #
# # 输入:
# # [
# #   1->4->5,
# #   1->3->4,
# #   2->6
# # ]
# # 输出: 1->1->2->3->4->4->5->6

## 思路:
# 分而治之
#
# 链表两两合并

## 代码:
# 思路一
# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 分治
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        n = len(lists)

        def merge(left, right):
            if left > right:
                return
            if left == right:
                return lists[left]
            mid = (left + right) // 2
            l1 = merge(left, mid)
            l2 = merge(mid + 1, right)
            return mergeTwoLists(l1, l2)

        def mergeTwoLists(l1, l2):
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = mergeTwoLists(l1, l2.next)
                return l2

        return merge(0, n - 1)