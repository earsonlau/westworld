# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 说明:
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。
# 这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

# 解题思路：
# 相似的查找算法有 KMP，BM，Horspool，挑了一个在实际情况中效果较好且理解简单的算法，即 Sunday 算法。
#
# 一、Sunday 匹配机制
# 匹配机制非常容易理解：
#
# 目标字符串String
#
# 模式串 Pattern
#
# 当前查询索引 idx （初始为 00）
#
# 待匹配字符串 str_cut : String [ idx : idx + len(Pattern) ]
#
# 每次匹配都会从 目标字符串中 提取 待匹配字符串与 模式串 进行匹配：
#
# 若匹配，则返回当前 idx
#
# 不匹配，则查看 待匹配字符串 的后一位字符 c：
#
# 若c存在于Pattern中，则 idx = idx + 偏移表[c]
#
# 否则，idx = idx + len(pattern)
#
# Repeat Loop 直到 idx + len(pattern) > len(String)
#
# 二、偏移表
# 偏移表的作用是存储每一个在 模式串 中出现的字符，在 模式串 中出现的最右位置到尾部的距离 +1+1，例如 aab：
#
# a 的偏移位就是 len(pattern)-1 = 2
# b 的偏移位就是 len(pattern)-2 = 1
# 其他的均为 len(pattern)+1 = 4

# 作者：Tes
# 链接：https://leetcode-cn.com/problems/implement-strstr/solution/python3-sundayjie-fa-9996-by-tes/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Func: 计算偏移表
        def calShiftMat(st):
            dic = {}
            for i in range(len(st) - 1, -1, -1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st) - i
            dic["ot"] = len(st) + 1
            return dic

        # 其他情况判断
        if len(needle) > len(haystack): return -1
        if needle == "": return 0

        # 偏移表预处理
        dic = calShiftMat(needle)
        idx = 0

        while idx + len(needle) <= len(haystack):

            # 待匹配字符串
            str_cut = haystack[idx:idx + len(needle)]

            # 判断是否匹配
            if str_cut == needle:
                return idx
            else:
                # 边界处理
                if idx + len(needle) >= len(haystack):
                    return -1
                    # 不匹配情况下，根据下一个字符的偏移，移动idx
                    cur_c = haystack[idx + len(needle)]
                    if dic.get(cur_c):
                        idx += dic[cur_c]
                    else:
                        idx += dic["ot"]

        return -1 if idx + len(needle) >= len(haystack) else idx


# 作者：Tes
# 链接：https: // leetcode - cn.com / problems / implement - strstr / solution / python3 - sundayjie - fa - 9996 - by - tes /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。