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

# 思路：
# 有序数组的带边界限制的二分查找问题
# 要写两个函数，函数left_bound搜索左边界 right_bound搜索右边界
# 注意：
# 1.left_bound的mid位置数字跟所找数字匹配时，不要返回mid，而要把right更新为mid-1进入下一轮循环
# 1.1 循环结束后要判断left是否越界/left所指向位置是否为所找数字
# 2.right_bound的mid位置数字跟所找数字匹配时，不要返回mid，而要把left更新为mid+1进入下一轮循环
# 2.2 循环结束后要判断right是否越界/right所指向位置是否为所找数字

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