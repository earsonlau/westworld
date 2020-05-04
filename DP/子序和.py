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
    def crossSum(self,nums,left,right,p): # p为分治算法的分割点
        if left == right: return nums[left] # base
        leftSubsum = -float('inf') # 负无穷
        currSum = 0 # 当前累计和
        for i in range(p, left-1, -1): # 从中间位置向左遍历
            currSum+=nums[i] # 计算累计和
            leftSubsum = max(leftSubsum,currSum) # 取累计和最大和,记为 左子和

        rightSubsum = -float('inf')
        currSum = 0
        for i in range(p+1,right+1): # 从中间位置向右遍历
            currSum += nums[i] # 当前累计和
            rightSubsum = max(rightSubsum,currSum) # 取累计和最大和,记为 右子和

        return leftSubsum + rightSubsum #左子和右子和相加即为最终和

    def helper(self,nums,left,right):
        print("left:",left)
        print("right:",right)
        if left == right: return nums[left]
        p = (left + right) // 2 # p取中点
        leftSum = self.helper(nums,left,p) # 递归求左子和
        rightSum = self.helper(nums,p+1,right) # 递归求右子和
        crossSum = self.crossSum(nums,left,right,p) # 求最终和
        return max(max(leftSum,rightSum),crossSum)

    def maxSubArray(self,nums):
        # 最左边的位置作为left参数的值,最右边的位置作为right参数的值
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
            currSum = max(nums[i],currSum + nums[i]) # 不断求不带负数的和
            maxSum = max(maxSum,currSum) # 取和的最大值
        return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))

#动态规划
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0: # 如果为正数
                nums[i] += nums[i - 1] # nums[i - 1]直接加到nums[i]上
            max_sum = max(nums[i], max_sum) # 取最大和

        return max_sum
