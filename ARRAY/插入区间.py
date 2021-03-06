# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 示例 1:
#
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
# 示例 2:
#
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#
# 思路:
# 先考虑三种极端情况
#
# intervals为空
# newInterval[1] < intervals[0][0],直接插入第一个位置
# newInterval[0] > intervals[-1][1],直接插入最后一个位置
# 下面就要考虑重叠情况了
#
# 我们目标就是找到和newInterval相关那几个区间.
#
# 首先,左边,当newInterval[0] > intervals[i][1]说明没有和该区间没有重叠部分,继续遍历下一个区间,比如intervals = [[1,3],[6,9]], newInterval = [4,7]
#
# 然后,再看右边,这里有个情况,就是 当intervals[i][0] > newInterval[1]说明newInterval没有和任何区间重合,比如intervals = [[1,3],[6,9]], newInterval = [4,5],直接插入即可.
#
# 接下来我们要找右边重合区域,当while i < n and newInterval[1] >= intervals[i][0]说明有重叠部分,记录左边最大值!
#
# 最后把数组拼接一下即可!

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        res = []
        # 找左边重合区域
        while i < n and newInterval[0] > intervals[i][1]:#新插入的区间的左端点大于区间i的右端点
            res.append(intervals[i])#直接接在区间i的后面
            i += 1
        tmp = [newInterval[0], newInterval[1]]#否则把新区间放在临时变量tmp里面
        # 找右边重合区域
        while i < n and newInterval[1] >= intervals[i][0]:#新插入区间的右端点大于区间i的左端点且新插入的区间的左端点小于区间i的右端点
            tmp[0] = min(tmp[0], intervals[i][0])#合并后的区间的左端点是两个区间左端点的较小值
            tmp[1] = max(tmp[1], intervals[i][1])#合并后的区间的右端点是两个区间右端点的较大值
            i += 1
        res.append(tmp)#此时的tmp是合并后区间
        while i < n:#新插入的区间是某个区间的子区间
            res.append(intervals[i])
            i += 1
        return res

a = Solution()
print(a.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))