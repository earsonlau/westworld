#双指针解法
testcase = [1,1,1,1,2,3,4,5]
#给一个值4和testcase[1,1,1,1,2,3,4,5]，
# 1.期望返回(4, [1, 1, 1, 1])
def sum_to_k_all_positive(k,arr):
    if len(arr) == 0 :
        return 0
    left = 0
    right = 0
    sum = arr[0]
    len_ = 0
    while (right < len(arr)):
        if sum == k :
            #找到了， 保存最长子数组，窗口数组和更新，左指针往前走一格
            if right - left + 1 > len_:
                res_arr = arr[left:right+1]
            len_ = max(right-left+1,len_)
            sum -=arr[left]
            left += 1
        elif sum < k :
            #sum还太小，右指针往前走一格，窗口数组和更新
            right += 1
            if right == len(arr):
                break
            sum += arr[right]
        else:
            #sum太大，窗口内数组和更新，左指针往前走一格
            sum -= arr[left]
            left += 1
    return len_,res_arr
print(sum_to_k_all_positive(4,[1,1,1,1,2,3,4,5]))