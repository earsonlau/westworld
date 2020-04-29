# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
#
# 要求返回这个链表的 深拷贝。 
#
# 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
#
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。

#思路一：哈希
#借助哈希保存节点信息
#代码
# 时间复杂度 O(n)
# 空间复杂度 O(n)

# class Solution {
# public:
#     Node* copyRandomList(Node* head) {
#         if (head == nullptr) {
#             return head;
#         }
#         Node *cur = head;
#         unordered_map<Node*, Node*> ump;
#         //1. 遍历链表，将原节点作为key，拷贝节点作为value保存在map中
#         while (cur != nullptr) {
#             Node *copy = new Node(cur->val);
#             ump[cur] = copy;
#             cur = cur->next;
#         }
#         //2. 复制链表next和random指针
#         cur = head;
#         while (cur != nullptr) {
#             ump[cur]->next = ump[cur->next];
#             ump[cur]->random = ump[cur->random];
#             cur = cur->next;
#         }
#         return ump[head];
#     }
# };

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self,head):
        if head is None:
            return head
        cur = head
        ump = {}
        # 遍历链表，将原节点作为key，拷贝节点作为value保存在map中
        while cur is not None:
            copy = ListNode(cur.val)
            ump[cur] = copy
            cur = cur.next

        # 复制链表next和random指针
        cur = head
        while cur is not None:
            ump[cur].next  = ump[cur.next]
            ump[cur].random = ump[cur.random]
            cur = cur.next
        return ump[head]

# 思路二：原地复制
# 复制节点，同时将复制节点链接到原节点后面，如A->B->C 变为 A->A'->B->B'->C->C'。
# 设置节点random值。
# 将复制链表从原链表分离。
#
# 代码
# 时间复杂度：O(n)
# 空间复杂度：O(1)


