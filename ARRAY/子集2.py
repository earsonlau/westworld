# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# # ]


#递归
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def helper(idx, tmp):
            res.append(tmp)
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                helper(i+1, tmp + [nums[i]])
        helper(0, [])
        return res

#迭代
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        res = [[]]
        cur = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                cur = [tmp + [nums[i]] for tmp in cur]
            else:
                cur = [tmp + [nums[i]] for tmp in res]
            res += cur
        return res