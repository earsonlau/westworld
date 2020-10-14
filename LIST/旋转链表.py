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


# 思路：


class LNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.random = None

class LinkList(object):
    def __init__(self):
        self.head = None

    #链表初始化函数, 方法类似于尾插
    def initList(self, data):
        if data is None or len(data) == 0:
            print("array can not be empty")
            return False
        #创建头结点
        self.head = LNode(data[0])
        p = self.head
        #逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = LNode(i)
            p.next = node
            p = p.next
#


def toString(cur):
    s = ""
    while cur is not None:
        s += str(cur.val)
        s += " -> "
        cur = cur.next

    s+= "NULL"
    return s

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
# 关键在于边界条件的讨论和代码调试
class Solution:
    def rotateRight(self,head,k):
        # 特判
        if head is None or head.next is None or k ==0:
            return head
        #第一步:知道链表有多少个结点
        n = 1
        fastnode = head
        while (fastnode.next is not None):
            fastnode = fastnode.next
            n += 1
        # fastnode到末尾结点
        k = k % n
        if k == 0:
            return head

        # 第二步:找到倒数第k个节点,走 n - k - 1 步
        slownode = head
        for i in range(n-k-1):
            slownode = slownode.next

        # 第三步:穿针引线
        newhead = slownode.next
        #先把尾部接到开头
        fastnode.next = head
        #再切断原来的连接
        slownode.next = None
        return newhead