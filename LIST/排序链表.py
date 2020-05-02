# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2:
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5

# 解答一：归并排序（递归法）
# 题目要求时间空间复杂度分别为O(nlogn)O(nlogn)和O(1)O(1)，根据时间复杂度我们自然想到二分法，从而联想到归并排序；
#
# 对数组做归并排序的空间复杂度为 O(n)O(n)，分别由新开辟数组O(n)O(n)和递归函数调用O(logn)O(logn)组成，而根据链表特性：
#
# 数组额外空间：链表可以通过修改引用来更改节点顺序，无需像数组一样开辟额外空间；
# 递归额外空间：递归调用函数将带来O(logn)O(logn)的空间复杂度，因此若希望达到O(1)O(1)空间复杂度，则不能使用递归。
# 通过递归实现链表归并排序，有以下两个环节：
#
# 分割 cut 环节： 找到当前链表中点，并从中点将链表断开（以便在下次递归 cut 时，链表片段拥有正确边界）；
# 我们使用 fast,slow 快慢双指针法，奇数个节点找到中点，偶数个节点找到中心左边的节点。
# 找到中点 slow 后，执行 slow.next = None 将链表切断。
# 递归分割时，输入当前链表左端点 head 和中心节点 slow 的下一个节点 tmp(因为链表是从 slow 切断的)。
# cut 递归终止条件： 当head.next == None时，说明只有一个节点了，直接返回此节点。
# 合并 merge 环节： 将两个排序链表合并，转化为一个排序链表。
# 双指针法合并，建立辅助ListNode h 作为头部。
# 设置两指针 left, right 分别指向两链表头部，比较两指针处节点值大小，由小到大加入合并链表头部，指针交替前进，直至添加完两个链表。
# 返回辅助ListNode h 作为头部的下个节点 h.next。
# 时间复杂度 O(l + r)，l, r 分别代表两个链表长度。
# 当题目输入的 head == None 时，直接返回None。
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 解答二：归并排序（从底至顶直接合并）
# 对于非递归的归并排序，需要使用迭代的方式替换cut环节：
# 我们知道，cut环节本质上是通过二分法得到链表最小节点单元，再通过多轮合并得到排序结果。
# 每一轮合并merge操作针对的单元都有固定长度intv，例如：
# 第一轮合并时intv = 1，即将整个链表切分为多个长度为1的单元，并按顺序两两排序合并，合并完成的已排序单元长度为2。
# 第二轮合并时intv = 2，即将整个链表切分为多个长度为2的单元，并按顺序两两排序合并，合并完成已排序单元长度为4。
# 以此类推，直到单元长度intv >= 链表长度，代表已经排序完成。
# 根据以上推论，我们可以仅根据intv计算每个单元边界，并完成链表的每轮排序合并，例如:
# 当intv = 1时，将链表第1和第2节点排序合并，第3和第4节点排序合并，……。
# 当intv = 2时，将链表第1-2和第3-4节点排序合并，第5-6和第7-8节点排序合并，……。
# 当intv = 4时，将链表第1-4和第5-8节点排序合并，第9-12和第13-16节点排序合并，……。
# 此方法时间复杂度O(nlogn)O(nlogn)，空间复杂度O(1)O(1)。
#
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        if not head or head.next == None:
            return head

        current, length = head, 0
        while current:  # 求得链表长度
            current, length = current.next, length + 1

        root = ListNode(0)
        root.next = head
        intv = 1  # 每次合并的规模

        # 根据不同的链表切片规模，每一次都从头进行归并
        while intv < length:
            merge_point, current = root, root.next

            while current:  # 根据当前的合并规模，将链表内的链表切片两两归并

                # 获取当前需要归并的子链表 h1
                h1, intv_residue_1 = current, intv
                while intv_residue_1 and current:
                    current, intv_residue_1 = current.next, intv_residue_1 - 1
                if intv_residue_1:  # h2 在这种情况下不存在，所以本轮不需要合并
                    break

                    # 获取当前需要归并的子链表 h2
                h2, intv_residue_2 = current, intv
                while intv_residue_2 and current:
                    current, intv_residue_2 = current.next, intv_residue_2 - 1

                len1, len2 = intv, intv - intv_residue_2  # len2 的长度可能比 intv 小

                while len1 and len2:  # 归并排序
                    if h1.val < h2.val:
                        merge_point.next, h1, len1 = h1, h1.next, len1 - 1
                    else:
                        merge_point.next, h2, len2 = h2, h2.next, len2 - 1
                    merge_point = merge_point.next

                if len1:  # 归并排序处理一下没有被归并的剩余值
                    merge_point.next = h1
                else:
                    merge_point.next = h2
                while len1 > 0 or len2 > 0:
                    merge_point, len1, len2 = merge_point.next, len1 - 1, len2 - 1

                merge_point.next = current  # h1 和 h2 的归并只是影响了链表的一部分，这里应该把归并后的链表切片跟原链表h2之后的部分拼起来

            intv *= 2

        return root.next