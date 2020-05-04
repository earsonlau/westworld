# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
#
#
#
#  示例 1:
#
#  输入: [1,2,0]
# 输出: 3
#
#
#  示例 2:
#
#  输入: [3,4,-1,1]
# 输出: 2
#
#
#  示例 3:
#
#  输入: [7,8,9,11,12]
# 输出: 1
#
#
#
#
#  提示：
#
#  你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
#  Related Topics 数组
#
# 方法一：哈希表（空间复杂度不符合要求）
# 按照刚才我们读例子的思路，其实我们只需从最小的正整数 1 开始，依次判断2、3 、4 直到数组的长度 N 是否在数组中。
#
# 如果当前考虑的数不在这个数组中，我们就找到了这个缺失的最小正整数。
#
# 由于我们需要依次判断某一个正整数是否在这个数组里，我们可以先把这个数组中所有的元素放进哈希表。接下来再遍历的时候，就可以以 O(1)的时间复杂度判断某个正整数是否在这个数组。
#
# 由于题目要求我们只能使用常数级别的空间，而哈希表的大小与数组的长度是线性相关的，因此空间复杂度不符合题目要求。

class Solution:
    def firstMissingPositive(self,nums):
        lens = len(nums) # 取一下nums长度
        #定义一个叫hashSet的集合
        hashSet  = set()
        # 遍历nums
        for num in nums:
            # 往集合里添加元素
            hashSet.add(num)
        #遍历整数
        for i in range(1,lens+1):
            if (not (i in hashSet)):
                return i # 谁不在 返回谁
        return lens + 1 # 否则返回lens + 1

a = Solution()
print(a.firstMissingPositive([2,3]))

# 方法二：二分查找（时间复杂度不符合要求）
# 根据刚才的分析，这个问题其实就是要我们查找一个元素，而查找一个元素，如果是在有序数组中查找，会快一些；
#
# 因此我们可以将数组先排序，再使用二分查找法从最小的正整数 11 开始查找，找不到就返回这个正整数；
#
# 这个思路需要先对数组排序，而排序使用的时间复杂度是 O(N \log N)O(NlogN)，是不符合这个问题的时间复杂度要求。

class Solution:
    # 二分查找
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return - 1

    def firstMissingPositive(self, nums):
        lens = len(nums)
        #定义一个叫hashSet的集合
        nums.sort()
        for i in range(1,lens+1):
            res = self.binarySearch(nums, i)
            if res == -1:
                return i
        return lens + 1

a = Solution()
print(a.firstMissingPositive([2,3]))

# 方法三：将数组视为哈希表
# 由于题目要求我们“只能使用常数级别的空间”，而要找的数一定在 [1, N + 1] 左闭右闭（这里 N 是数组的长度）这个区间里。因此，我们可以就把原始的数组当做哈希表来使用。事实上，哈希表其实本身也是一个数组；
# 我们要找的数就在 [1, N + 1] 里，最后 N + 1 这个元素我们不用找。因为在前面的 N 个元素都找不到的情况下，我们才返回 N + 1；
# 那么，我们可以采取这样的思路：就把 1 这个数放到下标为 0 的位置， 2 这个数放到下标为 1 的位置，按照这种思路整理一遍数组。然后我们再遍历一次数组，第 1 个遇到的它的值不等于下标的那个数，就是我们要找的缺失的第一个正数。
# 这个思想就相当于我们自己编写哈希函数，这个哈希函数的规则特别简单，那就是数值为 i 的数映射到下标为 i - 1 的位置。
# 我们来看一下这个算法是如何应用在示例 2 上的。

from typing import List
class Solution:

    # 3 应该放在索引为 2 的地方
    # 4 应该放在索引为 3 的地方
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                self.__swap(nums, i, nums[i] - 1) # 如果是索引但是没有放在正确的地方 那么放到正确的地方
        #谁没有建立正确的映射关系,谁就是缺失的
        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1

        return size + 1

    def __swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]
