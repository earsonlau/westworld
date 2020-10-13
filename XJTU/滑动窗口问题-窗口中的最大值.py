# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回滑动窗口中的最大值。
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#

from _collections import deque
def getmaxwindow(arr,w):
    if arr is None or len(arr) == 0:
        return None
    # qmax是一个只存数组下标的双端队列
    qmax = deque()
    # res是结果集，只放结果
    res = []
    # 遍历原数组
    for i in range(len(arr)):
        # 只要现在遍历到的数字arr[i]比队列最右端的数字要大
        # 队列从右侧弹出元素
        while len(qmax) != 0 and arr[qmax[-1]] <= arr[i]:
            qmax.pop()
        # 现在遍历到的数字arr[i]从右侧加入队列，队列从左到右递减
        qmax.append(i)
        # 如果队列最左端数字=现在遍历到的数字的下标 - 窗口长度
        # 说明队列最左端的数字要弹出，保证窗口内数字个数==窗口长度
        if qmax[0] == i - w:
            qmax.popleft()
        # 如果遍历到的数字的下标 >= 窗口长度 - 1 (窗口已经形成，排除掉一开始窗口内数字没充满窗口的情况)
        # 把双端队列最左端的数字放进结果集
        if i >= w - 1 :
            res.append(arr[qmax[0]])
    return res
print(getmaxwindow( [1,3,-1,-3,5,3,6,7], 3))