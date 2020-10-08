#两数之和

"""
思路：
遍历一遍数组。用一张哈希表存放遍历过的元素。如果元素在哈希表里面，直接返回该元素和他在哈希表里对应的value
否则，在哈希表里面存一条记录(target-nums[i],nums[i])
"""
def twosum(nums,target):
    res = {}
    for i in range(len(nums)):
        if nums[i] in res:
            return [nums[i],res[nums[i]]]
        else:
            res[target-nums[i]] = nums[i]
    return res

#执行
print(twosum([2,7,11,15],9))