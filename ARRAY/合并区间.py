# 给出一个区间的集合，请合并所有重叠的区间。
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

#思路：


from typing import List
#双指针就完事了
class Solution:
    def merge(self,intervals :List[List[int]]):
        if len(intervals) == 0 or len(intervals) == 1: return intervals
        # \\ initialize
        save = 0 # 用于保留和扩展的指针
        scan = 0 # 用于扫描的指针
        ans = [] # 结果集
        # 对二维数组进行排序
        intervals.sort()
        # 遍历所有的区间
        while scan < len(intervals):
            if intervals[scan][0] > intervals[save][1]: #此时两个区间不相交
                ans.append(intervals[save]) # save指向的区间压入结果集
                save = scan # save往前走一步
                scan = scan + 1 # scan往前走一步
            elif intervals[scan][1] <= intervals[save][1]: # 此时后一个区间被前一个区间所包含
                scan = scan + 1 # scan走一步，save不动
            else:
                # 两个区间相交但不包含 把第一个区间的右端点改为第二个区间的右端点
                intervals[save][1] = intervals[scan][1]
                # scan往前走，save不动（save指向的区间变成了这两个区间的合并区间）
                scan = scan + 1
        # scan已经移动到最后了，直接把save指向的区间压进去
        ans.append(intervals[save])
        return ans
a = Solution()
intervals =  [[1, 3], [2, 6], [8, 10], [15, 18]]
print(a.merge(intervals))