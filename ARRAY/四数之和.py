#这个代码输出的结果不对

def FourSum(nums,target):
    n=len(nums)
    res=[]
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