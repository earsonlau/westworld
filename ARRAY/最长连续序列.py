# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 先排序，题意要求连续序列，即可以比较 nums[i]与 nums[i - 1]
# 如果不相等，表示是递增的趋势，相等则反之，递增后需要判断是否连续，即相邻的元素差值是否为1
#
# 下面的代码处理边界 case 如[-1,0],不会比较max与cur的值，需要在最后一道防线拦截一次
def longestConsecutive(nums):
        if nums == None or len(nums) == 0:
            return 0
        nums.sort()
        n = len(nums)
        max = 1
        cur = 1
        for i in range(n):
            if (nums[i] != nums[i - 1]):
                if (nums[i - 1] + 1 == nums[i]):
                    # 统计以i结束有多长的连续递增序列
                    cur+=1
                else:
                    # max刷新为目前位置最长连续递增序列的长度
                    max = max(max, cur)
                    # cur复位
                    cur = 1
        return max(max, cur)

# 拓展:
# 最长上升子序列 （不要求连续）
# 思路:
# 	• dp[i]表示以i索引结尾的最长上升子序列的长度，
# 	即在[0-i]范围内，以nums[i]结尾的可以获得的最长上升子序列的长度
# 	• 如果遍历到i位置，在[0...j...i]区间内（）
# 	当nums[i]<=nums[j]时，表示以j结束的子序列和i结束的子序列不能形成上升子序列，
# 	举 例：[1,4,5,7,6,8]，当i=4，也就是nums[i] =6
# 	j为3时，nums[j] =7 ,nums[j]和nums[i]不能形成一个上升子序列；
#  那么情况当nums[i]>nums[j]时，
#  可以考虑在max[dp[j]]的最大值加上当前nums[i]的长度
#  dp[i]=max(dp[i],dp[j]+1)此为状态转移方程

# f[i]表示以i结尾的最长上升子序列长度
import numpy
def findNumberOfLIS(nums):
    if (nums == None or len(nums) == 0): return 0
    n = len(nums)
    f = numpy.ones(n)
    for i in range(1,n):
        for j in range(i):
            if (nums[i] > nums[j]): # 每一个以j结尾的可行的子序列的求解是该问题的一个子问题
                f[i] = max(f[j] + 1, f[i])  #在所有子问题里面找到一个最大的解
    return f.max()
print(findNumberOfLIS([100, 4, 200, 1, 3, 2]))

# dp[i]表示以i结尾的最长上升子序列长度
import numpy
def findNumberOfLIS(nums):
    if (nums == None or len(nums) == 0): return 0
    n = len(nums)
    dp = numpy.zeros(n)
    #长度为n，元素全为1的数组作为计数器
    counter = numpy.ones(n)
    dp[0] = 1
    maxLen = 0
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if (nums[i] > nums[j]):
                if (dp[j] + 1 > dp[i]):
                    dp[i] = max(dp[j] + 1, dp[i])
                    counter[i] = counter[j]
                elif (dp[j] + 1 == dp[i]):
                    counter[i] += counter[j]
        maxLen = max(maxLen, dp[i])
    result = 0
    for i in range(n):
        if (dp[i] == maxLen): result += counter[i]
    return result
print(findNumberOfLIS([100, 4, 200, 1, 3, 2]))


# 比较容易看的递归写法
def findNumOfLIS(nums):
    n = len(nums)
    ans = 0
    f = [0 for k in range(len(nums))]
    # declare a function.
    def LIS(nums, r):
        if r == 0:
            return 1
        if f[r] > 0:
            return f[r]
        ans = 1
        for i in range(r):
            if nums[r] > nums[i]:
                ans = max(ans, LIS(nums, r) + 1)
        f[r] = ans
        return f[r]
    # declare finish.

    for i in range(n-1):
        ans = max(ans,LIS(nums,i))



