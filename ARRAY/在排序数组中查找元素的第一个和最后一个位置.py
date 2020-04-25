# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。
# 找出给定目标值在数组中的开始位置和结束位置。
#
#  你的算法时间复杂度必须是 O(log n) 级别。
#
#  如果数组中不存在目标值，返回 [-1, -1]。
#
#  示例 1:
#
#  输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
#  示例 2:
#
#  输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#  Related Topics 数组 二分查找


class Solution(object):
    def searchRange(self, nums, target):
        return [self.left_bound(nums,target), self.right_bound(nums,target)]
    #找左边界,二分查找
    def left_bound(self,nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right :#小于等于
            mid = left + (right - left) // 2;
            if (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            elif (nums[mid] == target):
                # 别返回，收紧右侧边界以锁定左侧边界
                right = mid - 1
         # 最后要检查 left 越界的情况
        if (left >= len(nums) or nums[left] != target):
            return -1
        return left
    #找右边界,二分查找
    def right_bound(self,nums, target) :
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            if (nums[mid] < target) :
                left = mid + 1
            elif (nums[mid] > target) :
                right = mid - 1
            elif (nums[mid] == target) :
                 # 别返回，收紧左侧边界以锁定右侧边界
                left = mid + 1
         # 最后要检查 right 越界的情况
        if (right < 0 or nums[right] != target):
            return -1
        return right

a= Solution()
print(a.searchRange(nums = [5,7,7,8,8,10],target= 8))