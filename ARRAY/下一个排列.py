# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#

# 思路：

#交换nums的i，j位置的元素
def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp
    return nums

#从nums的第start个元素开始反转
def reverse(nums, start):
    i = start
    j = len(nums) - 1
    #先把nums存下来，不一定会进入while
    res = nums
    while (i < j):
        print("执行反转")
        res = swap(nums, i, j)
        print("res=",res)
        i += 1
        j -= 1
    return res

def nextPermutation(nums):
    i = len(nums) -2
    while( i >= 0 & nums[i] >= nums[i+1]):#从右侧扫描数字,找到升序排列的两个数
        i-=1
    print("i:",i)
    # 此时，i是左边那个较小数的index，i+1是右边那个较大数的index
    if( i >= 0):
        j =len(nums) - 1
        while(j >= 0 & nums[j] <= nums[i]):#从右侧扫描数字，找出第一个比nums[i]大的数
            j-=1
        # 此时，j是右起第一个比nums[i]大的数的index
        #交换nums[i]和nums[j]
        res = swap(nums,i,j)
    #把i+1位置起的元素全部反转
    return reverse(res,i+1)

print(nextPermutation([1,2,3]))
