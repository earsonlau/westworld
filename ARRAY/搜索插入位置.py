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