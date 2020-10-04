def maxsum(arr):
    if len(arr) == 0:
        return 0
    max_ = float('-inf')#负责记录cur更新后最大的值。初值为无穷小
    cur = 0#cur记录累加和
    for i in range(len(arr)):
        cur += arr[i]
        max_ = max(max_,cur)
        #如果cur是负的，清零 大于零的话不变
        cur = 0 if cur < 0 else cur
    return max_
print(maxsum([1,2,3,4,5,-2,-30,10,12]))