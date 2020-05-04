# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：

# 使用快排partition的思路

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # all in [0, zero) = 0
        # all in [zero, i) = 1
        # all in [two, len - 1] = 2

        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        size = len(nums)
        # 先看看有多少个球，若只有1一个球或者0个球，无需排序直接返回
        if size < 2:
            return
        #第一位肯定是0
        zero = 0
        #最后一位肯定是2
        two = size
        i = 0
        #起始指针
        #遍历
        while i < two:
            # 如果nums的第i个位置是0:
            if nums[i] == 0:
                #把zero和i位置的元素互换(把i位置的0换到zero位置
                swap(nums, i, zero)
                #i自增
                i += 1
                #zero自增
                zero += 1
            # 如果nums的第i个位置元素是1
            elif nums[i] == 1:
                #不需要换
                i += 1
            # nums的第i个位置元素是2
            else:
                #two后退一位
                two -= 1
                #把i位置的2换到two位置
                swap(nums, i, two)
