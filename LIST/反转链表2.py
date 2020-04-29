# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 反转以 head 为起点的 n 个节点，返回新的头节点
    def reverseN(self,head,n):
        successor = ListNode(None)
        if n == 1 :
            # 记录第n个节点
            successor = head.next
            return head
        # 以 head.next 为起点，需要反转前 n - 1 个节点
        last = self.reverseN(head.next, n - 1)
        # 让 head.next 的next指针指回head(反转指针
        head.next.next = head
        # 让反转后的 head 节点和后面的节点连起来
        head.next = successor#successor是不变的第n+1个节点
        return last

    def reverseBetween(self,head,m,n):
        # base case
        if m == 1 :
            return  self.reverseN(head,n)
        # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, m - 1, n -1 )
        return head

