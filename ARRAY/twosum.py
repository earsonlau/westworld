#两数之和

def twosum(nums,target):
    res = {}
    for i in range(len(nums)):
        if nums[i] in res:
            return [nums[i],res[nums[i]]]
        else:
            res[target-nums[i]] = nums[i]
    return res

print(twosum([2,7,11,15],9))