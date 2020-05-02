# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
#

def isMatch(text,pattern):
    if len(text) != len(pattern):
        return False
    for j in range(len(pattern)):
        if pattern[j] != text[j]:
            return False
    return True

# 然后，我稍微改造一下上面的代码，略微复杂了一点，但意思还是一样的，很容易理解吧：
def isMatch(text,pattern):
    i = 0 # text的索引
    j = 0 # pattern的索引
    while j < len(pattern):
        if i >= len(text):
            return False
        i += 1
        j += 1
        if pattern[j] != text[i]:
            return False
    # 相等则说明完成匹配
    return j == len(text)

# 如上改写，是为了将这个算法改造成递归算法（伪码）：
# def isMatch(text, pattern) -> bool:
#     if pattern is empty: return (text is empty?)
#     first_match = (text not empty) and pattern[0] == text[0]
#     return first_match and isMatch(text[1:], pattern[1:])


# 如果你能够理解这段代码，恭喜你，你的递归思想已经到位，正则表达式算法虽然有点复杂，其实是基于这段递归代码逐步改造而成的。
# 点号可以匹配任意一个字符，万金油嘛，其实是最简单的，稍加改造即可：
def isMatch(text, pattern) -> bool:
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and isMatch(text[1:], pattern[1:])
# 星号通配符可以让前一个字符重复任意次数，包括零次。那到底是重复几次呢？这似乎有点困难，不过不要着急，我们起码可以把框架的搭建再进一步：
# def isMatch(text, pattern) -> bool:
#     if not pattern: return not text
#     first_match = bool(text) and pattern[0] in {text[0], '.'}
#     if len(pattern) >= 2 and pattern[1] == '*':
#         # 发现 '*' 通配符
#     else:
#         return first_match and isMatch(text[1:], pattern[1:])
# # 星号前面的那个字符到底要重复几次呢？这需要计算机暴力穷举来算，假设重复 N 次吧。前文多次强调过，写递归的技巧是管好当下，之后的事抛给递归。具体到这里，不管 N 是多少，当前的选择只有两个：匹配 0 次、匹配 1 次。所以可以这样处理：
# # if len(pattern) >= 2 and pattern[1] == '*':
# #     return isMatch(text, pattern[2:]) or \
# #             first_match and isMatch(text[1:], pattern)
# 解释：如果发现有字符和 '*' 结合，
    # 或者匹配该字符 0 次，然后跳过该字符和 '*'
    # 或者当 pattern[0] 和 text[0] 匹配后，移动 text
# 可以看到，我们是通过保留 pattern 中的「*」，同时向后推移 text，来实现「*」将字符重复匹配多次的功能。


# 我选择使用「备忘录」递归的方法来降低复杂度。有了暴力解法，优化的过程及其简单，就是使用两个变量 i, j 记录当前匹配到的位置，从而避免使用子字符串切片，并且将 i, j 存入备忘录，避免重复计算即可。
# 我将暴力解法和优化解法放在一起，方便你对比，你可以发现优化解法无非就是把暴力解法「翻译」了一遍，加了个 memo 作为备忘录，仅此而已。
# 带备忘录的递归
def isMatch(text, pattern) -> bool:
    memo = dict()  # 备忘录

    def dp(i, j):
        if (i, j) in memo: return memo[(i, j)]
        if j == len(pattern): return i == len(text)

        first = i < len(text) and pattern[j] in {text[i], '.'}

        if j <= len(pattern) - 2 and pattern[j + 1] == '*':
            ans = dp(i, j + 2) or \
                  first and dp(i + 1, j)
        else:
            ans = first and dp(i + 1, j + 1)

        memo[(i, j)] = ans
        return ans

    return dp(0, 0)


# 暴力递归
def isMatch(text, pattern) -> bool:
    if not pattern: return not text

    first = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return isMatch(text, pattern[2:]) or \
               first and isMatch(text[1:], pattern)
    else:
        return first and isMatch(text[1:], pattern[1:])
