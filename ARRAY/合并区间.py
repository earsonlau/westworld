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
from typing import List
#双指针就完事了
class Solution:
    def merge(self,intervals :List[List[int]]):
        if len(intervals) == 0 or len(intervals) == 1: return intervals
        # \\ initialize
        save = 0
        scan = 0
        ans = []
        # \\ 思路1
        intervals.sort()
        # \\ 思路2
        while scan < len(intervals):
            if intervals[scan][0] > intervals[save][1]:
                ans.append(intervals[save])
        # \\情况一
                save = scan
            elif intervals[scan][1] <= intervals[save][1]:
                scan = scan + 1
        # \\因为已经排好序了，所以是情况二
            else:
                # \\情况三
                intervals[save][1] = intervals[scan][1]
                scan = scan + 1
        # \\ 思路3
        ans.append(intervals[save])
        return ans
a = Solution()
intervals = [
    [1,4],
    [4,5]
]
print(a.merge(intervals))