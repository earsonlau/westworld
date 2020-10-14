# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

import itertools
from typing import List



# 思路:
# 思路一: 库函数

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         for i in range(len(nums) + 1):
#             for tmp in itertools.combinations(nums, i):#返回nums长度为i的子集
#                 res.append(tmp)
#         return res
#
# # 思路二: 迭代
#
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = [[]]
#         for i in nums:
#             res = res + [[i] + num for num in res]
#         return res

# 思路三: 递归(回溯算法)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def helper(i, tmp):
            print("调用helper,开始寻找子集")
            res.append(tmp)#在结果中增加路径
            print("res:",res)
            #遍历选择列表
            for j in range(i, n):
                #做选择(这里不需要)
                helper(j + 1, tmp + [nums[j]])# 递归调用helper(路径,选择列表)
                #撤销选择(这里不需要)
            print("本次对helper的调用结束.")#本次对helper的调用结束
        helper(0, [])
        return res

print(Solution().subsets([2,3,4,5]))