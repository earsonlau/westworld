# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
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






#最长连续子序列的代码
# import numpy
# def longestIncreasingContinuousSubsequence(nums):
#     if (nums == None or len(nums) == 0): return 0
#     n = len(nums)
#     # start表示从前往后，end表示从后往
#     start = numpy.ones(2)
#     maxStart = 1
#     for i in range(1,n):
#         start[i % 2] = 1
#         if (nums[i] > nums[i - 1]):
#             start[i % 2] += start[(i - 1) % 2]
#         maxStart = max(maxStart, start[i % 2])
#     return  maxStart
#     end = numpy.ones(2)
#     maxEnd = 1
#     for i in range(n - 2,-1,-1):
#         end[i % 2] = 1
#         if (nums[i] > nums[i + 1]):
#             end[i % 2] += end[(i + 1) % 2]
#         maxEnd = max(maxEnd, end[i % 2])
#     # return max(maxStart, maxEnd)
# nums = [100, 4, 200, 1, 3, 2]
# print(longestIncreasingContinuousSubsequence(nums))
