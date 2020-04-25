#给定一个nums数组，找三个数加起来=0的所有可能。

from typing import List
#排序+双指针
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        if(not nums or n<3):
            return []
        nums.sort()
        res=[]
        for i in range(n): #遍历数组
            if(nums[i]>0):
                return res #后面不可能再来两个数和nums[i]相加=0
            if(i>0 and nums[i]==nums[i-1]):
                continue #跳过，避免出现重复解
            L=i+1 #左指针指向i的后一个数
            R=n-1 #右指针指向最后一个数
            while(L<R): #两个指针没碰到
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]]) #找到一组解，放进口袋
                    while(L<R and nums[L]==nums[L+1]): #左指针和下一位置有重复
                        L=L+1 #左指针右移一格
                    while(L<R and nums[R]==nums[R-1]): #右指针和前一位置有重复
                        R=R-1 #右指针前移一格
                    L=L+1 #寻找新解
                    R=R-1 #寻找新解
                elif(nums[i]+nums[L]+nums[R]>0):
                    R=R-1 #nums[R]太大，右指针左移
                else:
                    L=L+1 #nums[L]太小，左指针右移
        return res

#执行
a = Solution()
print(a.threeSum([-1,0,1,2,-1,4]))