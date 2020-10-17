# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
# 输入: "cbbd"
# 输出: "bb"


#
'''
思路1：暴力枚举，把所有长度>1子串都过一遍，找出最长的
思路2：中心扩散，每一个位置都做一次扩散，得到最长的（注意子串长度为奇数偶数分开处理）
'''

#BF 枚举
class Solution:
    # 暴力匹配（超时）
    def longestPalindrome(self, s: str) -> str:
        # 特判
        size = len(s)
        # 长度为1，则本身就是回文串
        if size < 2:
            return s
        max_len = 1
        res = s[0]
        # 枚举所有长度大于等于 2 的子串
        for i in range(size - 1):
            # 以每一个元素都作为起点扫一遍
            for j in range(i + 1, size):
                # 如果以i为起点j为终点的子串是回文串而且长度比上一轮算到的最长更长：
                if j - i + 1 > max_len and self.__valid(s, i, j):
                    # 更新一下最新的最长回文串的长度
                    max_len = j - i + 1
                    # 更新一下最新的最长回文串
                    res = s[i:j + 1]
        # 暴力枚举完所有字串 返回结果
        return res

    def __valid(self, s, left, right):
        # 验证子串 s[left, right] 是否为回文串
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


# 中心扩散法
# 遍历每一个索引，以这个索引为中心，利用“回文串”中心对称的特点，往两边扩散，看最多能扩散多远

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        # 至少是 1
        max_len = 1
        res = s[0]
        # 每一个i都是扩散的中心
        for i in range(size):
            # 长度为奇数的扩散结果1
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            # 长度为偶数的扩散结果2
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            # 结果1和结果2取较长
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            # 刷新
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res

    def __center_spread(self, s, size, left, right):
        """
        left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
        """
        i = left
        j = right
        # i开始向左扩散 j开始向右扩散 如果 s[i] != s[j] 跳出循环
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j], j - i - 1