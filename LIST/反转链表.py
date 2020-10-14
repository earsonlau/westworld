# 反转一个单链表
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

# #双指针迭代
# 我们可以申请两个指针，第一个指针叫 pre，最初是指向 null 的。
# 第二个指针 cur 指向 head，然后不断遍历 cur。
# 每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
# 都迭代完了(cur 变成 null 了)，pre 就是最后一个节点了。


class Solution:
    def reverseList(self,head):
        # 申请节点，pre 和 cur,pre 指向 None
        pre = None
        cur = head
        tmp = None
        while cur != None :
            # 记录当前节点的下一个节点, 放在tmp里面
            tmp = cur.next
            # 然后将当前节点指向 pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre

#递归解法
# 这题有个很骚气的递归解法，递归解法很不好理解，这里最好配合代码和动画一起理解。
# 递归的两个条件：
#
# 终止条件是当前节点或者下一个节点==null
# 在函数内部，改变节点的指向，也就是 head 的下一个节点指向 head 递归函数那句
# head.next.next = head
# 很不好理解，其实就是 head 的下一个节点指向head。
# 递归函数中每次返回的 cur 其实只最后一个节点，在递归函数内部，改变的是当前节点的指向。
# class Solution {
#         public ListNode reverseList(ListNode head) {
#                 //递归终止条件是当前为空，或者下一个节点为空
#                 if(head==null || head.next==null) {
#                         return head;
#                 }
#                 //这里的cur就是最后一个节点
#                 ListNode cur = reverseList(head.next);
#                 //这里请配合动画演示理解
#                 //如果链表是 1->2->3->4->5，那么此时的cur就是5
#                 //而head是4，head的下一个是5，下下一个是空
#                 //所以head.next.next 就是5->4
#                 head.next.next = head;
#                 //防止链表循环，需要将head.next设置为空
#                 head.next = null;
#                 //每层递归函数都返回cur，也就是最后一个节点
#                 return cur;
#         }
# }

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#同样是递归，换种形式表达。
from typing import List
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(head):
            if head == None or head.next == None:
                return head, head
            pre, last = helper(head.next)
            last.next = head
            head.next = None
            return pre, head

        rt, _ = helper(head)
        return rt