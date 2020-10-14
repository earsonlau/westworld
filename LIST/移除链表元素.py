# 删除链表中等于给定值 val 的所有节点。
# 示例:
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5

# 思路：
# 删除结点的步骤
#
# 找到该结点的前一个结点
# 进行删除操作
#
# 三种方法
#
# 删除头结点时另做考虑（由于头结点没有前一个结点）
# 添加一个虚拟头结点，删除头结点就不用另做考虑
# 递归
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 删除头结点时另做考虑（由于头结点没有前一个结点）
class Solution:
    def removeElements(self,head,val):
        # 删除值相同的头结点后,可能新的头结点也是值相等的,用循环解决
        while (head is not None and head.val == val):
            head = head.next
        if head is None:
            return head
        prev = head
        # 确保当前结点后还有结点
        while (prev.next is not None):
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head

# 方法二: 添加一个虚拟头结点
class Solution:
    def removeElements(self,head,val):
        # 创建一个虚拟头结点
        dummyNode = ListNode(val-1)
        dummyNode.next = head
        prev = dummyNode
        # 确保当前结点后还有结点
        while (prev.next != None):
            if prev.next.val == val :
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummyNode.next

# 方法三（递归）
#
class Solution:
    def removeElements(self,head,val):
        if head is None:
            return None
        head.next = self.removeElements(head.next,val)
        if head.val == val:
            return head.next
        else:
            return head
