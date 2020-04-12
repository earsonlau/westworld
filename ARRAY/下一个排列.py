# public class Solution {
#     public void nextPermutation(int[] nums) {
#         int i = nums.length - 2;
#         while (i >= 0 && nums[i + 1] <= nums[i]) {
#             i--;
#         }
#         if (i >= 0) {
#             int j = nums.length - 1;
#             while (j >= 0 && nums[j] <= nums[i]) {
#                 j--;
#             }
#             swap(nums, i, j);
#         }
#         reverse(nums, i + 1);
#     }
#
#     private void reverse(int[] nums, int start) {
#         int i = start, j = nums.length - 1;
#         while (i < j) {
#             swap(nums, i, j);
#             i++;
#             j--;
#         }
#     }
#
#     private void swap(int[] nums, int i, int j) {
#         int temp = nums[i];
#         nums[i] = nums[j];
#         nums[j] = temp;
#     }
# }

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
    print("i=",i,",j=",j)
    while (i < j):
        res = swap(nums, i, j)
        print("res=",res)
        i += 1
        j -= 1
    return res

def nextPermutation(nums):
    i = len(nums) -2
    while( i >= 0 & nums[i] >= nums[i+1]):#从右侧扫描数字,找到升序排列的两个数
        i-=1
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

