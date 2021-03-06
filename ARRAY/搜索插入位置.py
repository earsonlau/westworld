# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
#  你可以假设数组中无重复元素。
#
#  示例 1:
#
#  输入: [1,3,5,6], 5
# 输出: 2
#
#
#  示例 2:
#
#  输入: [1,3,5,6], 2
# 输出: 1
#
#
#  示例 3:
#
#  输入: [1,3,5,6], 7
# 输出: 4
#
#
#  示例 4:
#
#  输入: [1,3,5,6], 0
# 输出: 0
#
#  Related Topics 数组 二分查找

# 思路:

#二分就完事了~
class Solution:
    def searchInsert(self,nums, target) :
        left = 0
        right = len(nums) - 1 # 注意
        while(left <= right): # 注意
            mid = left + (right - left) // 2  # 注意
            if(nums[mid] == target): # 注意
                return mid
            elif(nums[mid] < target) :
                left = mid + 1 # 注意
            else:
                right = mid - 1 # 注意
        # 相关返回值
        return 0

a = Solution()
print(a.searchInsert([1,3,5,6],5))