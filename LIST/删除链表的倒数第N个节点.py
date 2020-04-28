# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？

#JAVA解

# class Solution {
# public:
#     ListNode* removeNthFromEnd(ListNode* head, int n) {
#         ListNode* dummyHead = new ListNode(0);
#         dummyHead->next = head;
#         ListNode* p = dummyHead;
#         ListNode* q = dummyHead;
#         for( int i = 0 ; i < n + 1 ; i ++ ){
#             q = q->next;
#         }
#         while(q){
#             p = p->next;
#             q = q->next;
#         }
#         ListNode* delNode = p->next;
#         p->next = delNode->next;
#         delete delNode;
#         ListNode* retNode = dummyHead->next;
#         delete dummyHead;
#         return retNode;
#     }
# };
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def removeNthFromEnd(self,head,n):
        dummyHead = ListNode(0)
        dummyHead.next = head
        p = dummyHead
        q = dummyHead
        for i in range(n+1):
            q = q.next
        while(q):
            p = p.next
            q = q.next
        delNode = p.next
        p.next = delNode.next
        retNode = dummyHead.next
        return retNode
