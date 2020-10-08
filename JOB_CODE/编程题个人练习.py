# 1. 反转链表
# 双指针操作即可，一个cur和一个pre，加上一个tmp保存一下下一个要遍历的
def reverselist(head):
    pre = None
    cur = head
    while cur != None:
        tmp = cur.next
        cur.next =pre
        pre = cur
        cur = tmp
    return pre
# 2. 二分查找

# 3. 二叉树的先序中序后序
# 4. 判断链表中是否有环
# 5. 合并有序链表
# 6. 寻找第K大
# 7. 删除链表的倒数第k个节点
# 8. 二叉树层次遍历
# 8. 两个栈实现队列
# 9. 最长公共子串
# 10. 子数组最大累加和
# 11. 最长递增子序列