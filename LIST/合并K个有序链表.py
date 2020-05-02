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
#
# 思路1：优先级队列
# 时间复杂度O(n * log(k)), n是所有链表中元素的总和，k是链表个数。
#
# JAVA
#

# /**
#  * Definition for singly-linked list.
#  * public class ListNode {
#  *     int val;
#  *     ListNode next;
#  *     ListNode(int x) { val = x; }
#  * }
#  */
# class Solution {
#     public ListNode mergeKLists(ListNode[] lists) {
#         if (lists == null || lists.length == 0) return null;
#         PriorityQueue<ListNode> queue = new PriorityQueue<>(lists.length, new Comparator<ListNode>() {
#             @Override
#             public int compare(ListNode o1, ListNode o2) {
#                 if (o1.val < o2.val) return -1;
#                 else if (o1.val == o2.val) return 0;
#                 else return 1;
#             }
#         });
#         ListNode dummy = new ListNode(0);
#         ListNode p = dummy;
#         for (ListNode node : lists) {
#             if (node != null) queue.add(node);
#         }
#         while (!queue.isEmpty()) {
#             p.next = queue.poll();
#             p = p.next;
#             if (p.next != null) queue.add(p.next);
#         }
#         return dummy.next;
#     }
# }
#
# 思路2：分治算法
# 链表两两合并
# /**
#  * Definition for singly-linked list.
#  * public class ListNode {
#  *     int val;
#  *     ListNode next;
#  *     ListNode(int x) { val = x; }
#  * }
#  */
# class Solution {
#     public ListNode mergeKLists(ListNode[] lists) {
#         if (lists == null || lists.length == 0) return null;
#         return merge(lists, 0, lists.length - 1);
#     }
#
#     private ListNode merge(ListNode[] lists, int left, int right) {
#         if (left == right) return lists[left];
#         int mid = left + (right - left) / 2;
#         ListNode l1 = merge(lists, left, mid);
#         ListNode l2 = merge(lists, mid + 1, right);
#         return mergeTwoLists(l1, l2);
#     }
#     private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
#         if (l1 == null) return l2;
#         if (l2 == null) return l1;
#         if (l1.val < l2.val) {
#             l1.next = mergeTwoLists(l1.next, l2);
#             return l1;
#         } else {
#             l2.next = mergeTwoLists(l1,l2.next);
#             return l2;
#         }
#     }
## 思路:

# 思路1:
#
# 优先级队列
#
# 时间复杂度:$O(n * log(k))$, n是所有链表中元素的总和, k是链表个数.
#
# 一年后再看此题, 也可以打猴子补丁来自定义类排序
#
# 思路2:
#
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

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


# 猴子补丁
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def __lt__(self, other):
            return self.val < other.val

        ListNode.__lt__ = __lt__

        import heapq
        heap = []
        dummy = ListNode(-1)
        p = dummy

        for l in lists:
            if l:
                heapq.heappush(heap, l)
        while heap:
            node = heapq.heappop(heap)
            p.next = ListNode(node.val)
            p = p.next
            if node.next:
                heapq.heappush(heap, node.next)
        return dummy.next

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