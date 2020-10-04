testcase = [1,1,1,-1,1,2,3,4,5]
#给一个值5和testcase[1,1,1,-1,1,2,3,4,5]，
# 1.期望返回(6, [1, 1, 1, -1, 1, 2])
def sum_to_k(k,arr):
    if len(arr) == 0 :
        return 0
    #先求出arr所有元素之和
    sum_ = 0
    len_ = 0
    res = {}
    res[0] = -1 #因为从0开始到索引指示位置的长度等于索引-(-1) 故res的key为0时value为-1
    #如果不写这一个，那么位置0开始的长度永远会被忽略
    for i in range(len(arr)):
        #对位置0到位置i的元素求和得到sum_
        sum_ += arr[i]
        # 如果和为k的子数组找到了
        if sum_ - k in res:
            # 这次找到的子数组比上一次找到的子数组更长
            #更新res_arr为更长的子数组
            if i - res[sum_-k] > len_:
                res_arr=arr[res[sum_-k]+1:(i+1)]
            #len始终为最长子数组的长度，故每次要和上次求的len_比较，取较大者
            len_ = max( i - res[sum_ - k],len_)
        #和不在哈希表里面，插入一个和
        if sum_ not in res:
            res[sum_] = i
    return len_,res_arr
print(sum_to_k(5,testcase))