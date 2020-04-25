# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
#  搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
#  你可以假设数组中不存在重复的元素。
#
#  你的算法时间复杂度必须是 O(log n) 级别。
#
#  示例 1:
#
#  输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
#
#  示例 2:
#
#  输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#  Related Topics 数组 二分查找

# 解题思路：
# 题目要求0（logN）的时间复杂度，基本可以断定本题是需要使用二分查找，怎么分是关踺。
# 由于题目说数字了无重复，举个例子．
# 1234567可以大致分为两类，
# 第一类2345671这种，也就是nums[start]<=nums[mid]。此例子中就是2<=5
# 这种情况下，前半部分有序。因此如果nums[start] <= target<nums[mid]，则在前半部分找，否则
# 去后半部分找。
# 第二类6712345这种，也就是nums[start] > nums[mid]。此例子中就是6>2
# 这种情况下，后半部分有序。因此如果nums[mid]< target <=nums[end]，则在后半部分找，否则去
# 前半部分找。

# public int search(int[] nums, int target) {
#         if (nums == null || nums.length == 0) {
#             return -1;
#         }
#         int start = 0;
#         int end = nums.length - 1;
#         int mid;
#         while (start <= end) {
#             mid = start + (end - start) / 2;
#             if (nums[mid] == target) {
#                 return mid;
#             }
#             //前半部分有序,注意此处用小于等于
#             if (nums[start] <= nums[mid]) {
#                 //target在前半部分
#                 if (target >= nums[start] && target < nums[mid]) {
#                     end = mid - 1;
#                 } else {
#                     start = mid + 1;
#                 }
#             } else {
#                 //target在后半部分
#                 if (target <= nums[end] && target > nums[mid]) {
#                     start = mid + 1;
#                 } else {
#                     end = mid - 1;
#                 }
#             }
#         }
#         return -1;
#     }

def search(nums,target):
    if (nums is None or len(nums) == 0 ):
        return -1
    start = 0
    end = len(nums) - 1
    while (start <= end):
        mid = start + (end - start)//2
        if nums[mid] == target:
            return mid
        #前半部分有序，注意此处用“小于等于”
        if nums[start] <= nums[mid]:
            #target在前半部分
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            #target在后半部分
            else:
                start = mid + 1
        #后半部分有序
        else:
            if target >= nums[mid] and target < nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

print(search([4,5,6,7,0,1,2],5))