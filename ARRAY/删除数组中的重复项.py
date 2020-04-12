#双指针法
def removeDuplicates(nums):
    if (len(nums) == 0):
        return 0
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:#不重复
            #两个指针一起动
            i = i + 1
            nums[i] = nums[j]
        #如果重复，只有j动，i保持不动
    return i+1

print(removeDuplicates([0,0,0,1,1,1,2,2,3,3,4]))
