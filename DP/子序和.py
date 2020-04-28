#最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
#  示例:
#
#  输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
#  进阶:
#
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#  Related Topics 数组 分治算法 动态规划

#分治算法 in Python
class Solution:
    def crossSum(self,nums,left,right,p):
        if left == right: return nums[left]
        leftSubsum = -float('inf')
        currSum = 0
        for i in range (p,left-1,-1):
            currSum+=nums[i]
            leftSubsum = max(leftSubsum,currSum)

        rightSubsum = -float('inf')
        currSum = 0
        for i in range(p+1,right+1):
            currSum += nums[i]
            rightSubsum = max(rightSubsum,currSum)

        return leftSubsum + rightSubsum

    def helper(self,nums,left,right):
        print("left:",left)
        print("right:",right)
        if left == right: return nums[left]
        p = (left + right) // 2
        leftSum = self.helper(nums,left,p)
        rightSum = self.helper(nums,p+1,right)
        crossSum = self.crossSum(nums,left,right,p)
        return max(max(leftSum,rightSum),crossSum)
    def maxSubArray(self,nums):
        return self.helper(nums,0,len(nums) - 1 )

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))


#贪心
class Solution:
    def maxSubArray(self,nums):
        n = len(nums)
        currSum = nums[0]
        maxSum = nums[0]
        for i in range(1,n):
            currSum = max(nums[i],currSum + nums[i])
            maxSum = max(maxSum,currSum)
        return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))

#动态规划
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)

        return max_sum
