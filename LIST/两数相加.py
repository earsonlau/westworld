# 思路：

#一遍哈希表
def twosum(nums, target):
    res = {}
    for i in range(len(nums)):
        if nums[i] in res:
            return [nums[i], res[nums[i]]]
        else:
            res[target - nums[i]] = nums[i]
