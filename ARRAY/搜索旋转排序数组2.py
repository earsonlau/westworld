# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
#  ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#
#  编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
#  示例 1:
#
#  输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
#
#
#  示例 2:
#
#  输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false

# 思路:
# 本题是需要使用二分查找，怎么分是关键，举个例子：
#
# 第一类
# 	10111 和 1110111101 这种。此种情况下 nums[start] == nums[mid]，分不清到底是前面有序还是后面有序，此时 start++ 即可。相当于去掉一个重复的干扰项。
# 第二类
# 	2 3 4 5 6 7 1这种，也就是 nums[start] < nums[mid]。此例子中就是 2 < 5；
# 	这种情况下，前半部分有序。因此如果 nums[start] <=target<nums[mid]，则在前半部分找，否则去后半部分找。
# 第三类
# 	6 7 1 2 3 4 5这种，也就是 nums[start] > nums[mid]。此例子中就是 6 > 2；
# 	这种情况下，后半部分有序。因此如果 nums[mid] <target<=nums[end]。则在后半部分找，否则去前半部分找。


def search(nums,target):
    if (nums is None or len(nums) == 0 ):
        return -1
    start = 0
    end = len(nums) - 1
    while (start <= end):
        mid = start + (end - start)//2
        if nums[mid] == target:
            return True
        elif nums[start] == nums[mid]:
            start += 1
            continue
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
    return False

print(search( [2,5,6,0,0,1,2],5))