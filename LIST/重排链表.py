# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

# 解法一 存储
# 链表的缺点就是不能随机存储，当我们想取末尾元素的时候，只能从头遍历一遍，很耗费时间。
# 第二次取末尾元素的时候，又得遍历一遍。
# 所以先来个简单粗暴的想法，把链表存储到线性表中，然后用双指针依次从头尾取元素即可。

# 思路1：
'''
如果头节点为空 返回空
创建一个数组 如果头节点非空 把整个链表都塞进数组里面 数组里面每个位置都放一个节点
指针left指向数组头 list_[0] 指针right指向数组尾 list_[len(list_)-1]
当left<right时：
    1.让left位置的节点的next指针指向right节点
    2.left自增1（若left自增1后与right指向同一个节点，跳出循环），
    3.right节点的next指向left节点
    4.right自减1
最后left节点的next指向空
'''


def reorderList(head):
    if head is None:
        return
    # 存到list_
    list_ =[]
    while(head is not None):
       list_.append(head)
       head = head.next

    #头尾指针依次取元素
    left = 0
    right = len(list_) -1
    while left < right:
        list_[left].next = list_[right]
        left += 1
        # 偶数个节点的情况,会提前相遇
        if left == right :
            break
        list_[righr].next = list_[left]
        right -= 1
    list_[left].next = None

# 解法二 递归
# 解法一中也说到了，我们的问题就是取尾元素的时候，需要遍历一遍链表。
# 如果我们的递归函数能够返回当前头元素对应的尾元素，
# 并且将头元素和尾元素之间的链表按要求完成，那就变得简单了。
#思路没看懂

def reorderListHelper(head,len):
    # 只有单节点，直接返回head.next
    if len == 1 :
        outTail = head.next
        head.next = None
        return outTail
    # 双节点，返回head.next.next
    if len == 2 :
        outTail = head.next.next
        head.next.next = None
        return outTail
    # 得到对应的尾节点,并且将头结点和尾节点之间的链表通过递归处理
    tail = reorderListHelper(head.next,len - 2)
    subHead = head.next
    head.next = tail
    outTail = tail.next
    tail.next = subHead
    return outTail

def reorderList(head):
    if head is None or head.next is None or head.next.next is None:
        return
    len = 0
    h = head
    # 求出节点数
    while h is not None:
        len += 1
        h = h.next
    reorderListHelper(head,len)

# 解法三
# 思路：
# 这里，主要是利用到一头一尾取元素的特性。
# 主要是三步，举个例子。
# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# 第一步，将链表平均分成两半
# 1 -> 2 -> 3
# 4 -> 5 -> 6
#
# 第二步，将第二个链表逆序
# 1 -> 2 -> 3
# 6 -> 5 -> 4
#
# 第三步，依次连接两个链表
# 1 -> 6 -> 2 -> 5 -> 3 -> 4
#
# 第一步找中点的话，用快慢指针。快指针一次走两步，慢指针一次走一步，
# 当快指针走到终点的话，慢指针会刚好到中点。如果节点个数是偶数的话，慢指针走到的是左端点，
# 利用这一点，我们可以把奇数和偶数的情况合并，不需要分开考虑。
# 第二步链表逆序的话，有迭代和递归的两种方式，迭代的话主要利用两个指针，依次逆转。
# 第三步的话就很简单了，两个指针分别向后移动就可以。

def reorderList(head):
    if head is None or head.next is None or head.next.next is None:
        return
    # 找中点,链表分成两个
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    newHead = slow.next
    slow.next = None

    # 第二个链表倒置
    newHead = reverseList(newHead)

    #链表节点依次连接
    while newHead is not None:
        temp = newHead.next
        newHead.next = head.next
        head.next = newHead
        head = newHead.next
        newHead = temp

def reverseList(head):
    if head is None:
        return None
    tail = head
    head = head.next
    tail.next = None
    while head is not None:
        temp = head.next
        head.next = tail
        tail = head
        head = temp
    return tail
