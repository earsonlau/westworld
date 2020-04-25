# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。
#
#  例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#  Related Topics 数组 双指针

def threeSum(nums, target):
    n = len(nums)
    if (not nums or n < 3):
        return []
    nums.sort()  # 排序
    print(nums)
    ans = nums[0] + nums[1] + nums[2]
    for i in range(n):  # 遍历数组
        print("i:", i)
        if (nums[i] > target):
            return ans  # 后面不可能再来两个数和nums[i]相加接近target
        if (nums[i] == nums[i - 1]):
            continue  # 跳过，避免出现重复解
        L = i + 1  # 左指针指向i的后一个数
        R = n - 1  # 右指针指向最后一个数
        print("L: ", L)
        print("R: ", R)

        while (L < R):  # 两个指针没碰到
            sum = nums[i] + nums[L] + nums[R]
            if (abs(target - sum) < abs(target - ans)):
                ans = sum  # 找到一组解，放进口袋
                print("找到一组解: ", ans)
                while (L < R and nums[L] == nums[L + 1]):  # 左指针和下一位置有重复
                    L = L + 1  # 左指针右移一格
                    print("L: ", L)
                while (L < R and nums[R] == nums[R - 1]):  # 右指针和前一位置有重复
                    R = R - 1  # 右指针前移一格
                    print("R: ", R)
            if (sum > target):
                R = R - 1  # nums[R]太大，右指针左移
                print("nums[R]太大，右指针左移,R: ", R)
            elif (sum < target):
                L = L + 1  # nums[L]太小，左指针右移
                print("nums[L]太小，左指针右移,L: ", L)
    return ans
