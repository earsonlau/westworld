# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c +
#  d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#  注意：
#  答案中不可以包含重复的四元组。
#  示例：
#  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#
#  Related Topics 数组 哈希表 双指针

# 思路：
# 1.排序
# 2.滑动窗口扫描数组

def FourSum(nums,target):
    n=len(nums)
    if(not nums or n<3):
        return []
    nums.sort()
    res=[]
    for a in range(n):
        for b in range(a+1,n):#遍历数组
            if(nums[b]>target):
                return res #后面不可能再来两个数和nums[i]相加=0
            if(b>0 and nums[b]==nums[b-1]):
                continue #跳过，避免出现重复解
            L=b+1 #左指针指向i的后一个数
            R=n-1 #右指针指向最后一个数
            while(L<R): #两个指针没碰到
                if(nums[a]+nums[b]+nums[L]+nums[R]==target):
                    res.append([nums[a],nums[b],nums[L],nums[R]]) #找到一组解，放进口袋
                    while(L<R and nums[L]==nums[L+1]): #左指针和下一位置有重复
                        L=L+1 #左指针右移一格
                    while(L<R and nums[R]==nums[R-1]): #右指针和前一位置有重复
                        R=R-1 #右指针前移一格
                    L=L+1 #寻找新解
                    R=R-1 #寻找新解
                elif(nums[a]+nums[b]+nums[L]+nums[R]>target):
                    R=R-1 #nums[R]太大，右指针左移
                else:
                    L=L+1 #nums[L]太小，左指针右移
    return res

print(FourSum([1,0,-1,0,-2,2],0))