# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。
#
# 说明:
#
# 初始化 nums1 和 nums3 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]

# 思路
# 标签：从后向前数组遍历
# 因为 nums1 的空间都集中在后面，所以从后向前处理排序的数据会更好，节省空间，一边遍历一边将值填充进去
# 设置指针 last_one_index1 和 last_one_index2 分别指向 nums1 和 nums2 的有数字尾部，
# 从尾部值开始比较遍历，
# 同时设置指针 total_index 指向 nums1 的最末尾，每次遍历比较值大小之后，则进行填充
# 当 last_one_index1<0 时遍历结束，此时 nums2 中还有数据未拷贝完全，
# 将其直接拷贝到 nums1 的前面，最后得到结果数组

class Solution:
    def merge(self,nums1,nums1_count,nums2,nums2_count):
        last_one_index1 = nums1_count - 1
        last_one_index2 = nums2_count - 1
        total_index = nums1_count + nums2_count - 1
        while last_one_index1 >= 0 and last_one_index2 >=0:
            if nums2[last_one_index2] > nums1[last_one_index1]:
                #nums1的最末端放上末端位置较大的那个数组的最后一个数
                nums1[total_index] = nums2[last_one_index2]
                total_index -= 1
                last_one_index2 -= 1
                print(nums1)
            else:
                # nums1的最末端放上末端位置较大的那个数组的最后一个数
                nums1[total_index] = nums1[last_one_index1]
                total_index -= 1
                last_one_index1 -= 1
                print(nums1)
        if last_one_index2 + 1 > 0:
            # 当 last_one_index1<0 时遍历结束，
            # 此时 nums2 中还有数据未拷贝完全，
            # 将其直接拷贝到 nums1 的前面，最后得到结果数组
            nums1.insert(0,nums2[0:(last_one_index2+1)])

        return nums1
print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))
