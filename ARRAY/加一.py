# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:
#
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。

# 根据题意加一，没错就是加一这很重要，因为它是只加一的所以有可能的情况就只有两种：
#
# 除 99 之外的数字加一；
# 数字 99。
# 加一得十进一位个位数为 00 加法运算如不出现进位就运算结束了且进位只会是一。
#
# 所以只需要判断有没有进位并模拟出它的进位方式，如十位数加 11 个位数置为 00，如此循环直到判断没有再进位就退出循环返回结果。
#
# 然后还有一些特殊情况就是当出现 9999、999999 之类的数字时，循环到最后也需要进位，出现这种情况时需要手动将它进一位。
import numpy as np
class Solution:
    def plusOne(self,digits):
        for i in range(len(digits)- 1,-1,-1):#从后往前遍历
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] != 0: return digits #只要有一位不为0(没有出现进位)，就直接返回
        digits = np.zeros(len(digits) + 1)
        digits[0] = 1
        return digits

a = Solution()
print(a.plusOne([9,9,9]))
