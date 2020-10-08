# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字）。
#
#  示例 1:
#
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
#  示例 2:
#
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是连续的。
#  Related Topics 数组 动态规划
"""
思路：
遍历一次数组，每到一个位置都刷新一遍'当前最大值'和'当前最小值'，所有'当前最大值'的最大值就是全局最大值。
注意遍历到一个负数时，当前最大值要和当前最小值进行交换。
"""
class Solution:
    def maxcount(self,nums):
        max = float("inf")
        imax = 1
        imin = 1
        for i in range(len(nums)):
            if nums[i] < 0 :
                #如果nums的第i个元素为负，则imax和imin的值互换.
                # 因为和负数相乘，最大的会变成最小，而最小的会变成最大.
                tmp = imax
                imax = imin
                imin = tmp
            #维护当前最大值
            imax = max(imax * nums[i], nums[i])
            #维护当前最小值
            imin = min(imin * nums[i], nums[i])
            #不断更新最大值
            max = max(max,imax)
        return max

