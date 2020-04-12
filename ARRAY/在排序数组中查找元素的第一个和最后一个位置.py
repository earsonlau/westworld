class Solution(object):
    def searchRange(self, nums, target):
        return [self.left_bound(nums,target), self.right_bound(nums,target)]

    def left_bound(self,nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right :
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