class Solution:
    def maxcount(self,nums):
        max = float("inf")
        imax = 1
        imin = 1
        for i in range(len(nums)):
            if nums[i] < 0 :
                #如果nums的第i个元素为负，则imax和imin的值互换.
                # 因为和负数相乘，最大的会变成最小，而最小的会变成最大.
                tmp = imax
                imax = imin
                imin = tmp
            #维护当前最大值
            imax = max(imax * nums[i] , nums[i])
            #维护当前最小值
            imin = min(imin * nums[i] , nums[i])
            #不断更新最大值
            max = max(max,imax)
        return max

