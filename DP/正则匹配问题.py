
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
#  '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#
#
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
#  说明:
#
#
#  s 可能为空，且只包含从 a-z 的小写字母。
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
#
#
#  示例 1:
#
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
#
#  示例 2:
#
#  输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#
#  示例 3:
#
#  输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#
#  示例 4:
#
#  输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#
#
#  示例 5:
#
#  输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
#  Related Topics 字符串 动态规划 回溯算法

#回溯
# 首先，我们考虑只有 '.' 的情况。这种情况会很简单：我们只需要从左到右依次判断 s[i] 和 p[i] 是否匹配。
#
# def isMatch(self,s:str, p:str) -> bool:
#     if not p: return not s # 边界条件
#
#     first_match = s and p[0] in {s[0],'.'} # 比较第一个字符是否匹配
#
#     return first_match and self.isMatch(s[1:], p[1:])
# 如果有星号，它会出现在 p[1] 的位置，这时有两种情况：
#
# 星号代表匹配 0 个前面的元素。如 '##' 和 a*##，这时我们直接忽略 p 的 a*，比较 ## 和 ##；
# 星号代表匹配一个或多个前面的元素。如 aaab 和 a*b，这时我们将忽略 s 的第一个元素，比较 aab 和 a*b。
# 以上任一情况忽略掉元素进行比较时，剩下的如果匹配，我们认为 s 和 p 是匹配的。
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        # 第一个字母是否匹配
        first_match = bool(s and p[0] in {s[0],'.'})
        # 如果 p 第二个字母是 *
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or \
            first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])




#DP
# 状态转移方程见
# https://leetcode-cn.com/problems/regular-expression-matching/solution/hui-su-he-dong-tai-gui-hua-by-ml-zimingmeng/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 边界条件，考虑 s 或 p 分别为空的情况
        if not p: return not s
        if not s and len(p) == 1: return False

        m, n = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        # 初始状态
        dp[0][0] = True
        dp[0][1] = False

        for c in range(2, n):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]

        for r in range(1, m):
            i = r - 1
            for c in range(1, n):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':  # ‘*’前面的字符匹配s[i] 或者为'.'
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:  # ‘*’匹配了0次前面的字符
                        dp[r][c] = dp[r][c - 2]
                else:
                    dp[r][c] = False
        return dp[m - 1][n - 1]




# class Solution {
# private String pattern;
# private String text;
# private Boolean[][] dp;
# public boolean isMatch(String s, String p) {
# if (s == null) s=new String();
# if (p == null) p=new String();
# // 空的正则串不能匹配s
# if (s.length() != 0 & & p.length() == 0)
#
#
# return false;
# // 空正则串可以匹配空s
# if (s.length() == 0 & & p.length() == 0) return true;
#
# // 非空正则不一定可以匹配空s或非空s
# // 此处由于要处理 * 使用递归解法
# this.text = s;
# this.pattern = p;
# this.dp = new
# Boolean[s.length() + 1][p.length() + 1];
# return recur(0, 0);
# }
# // i为text的索引, j为pattern的索引
# private
# boolean
# recur(int
# i, int
# j) {
# if (j < pattern.length() & & i < text.length() & & dp[i][j] != null) return dp[i][j];
# // 正则串为空
# if (j == pattern.length()) return dp[i][j]=(i == text.length());
# // 正则串非空
# 匹配串为空
# if (i == text.length()) {
# // 只可能 * 取0重才可能为真
# if (j+1 < pattern.length() & & pattern.charAt(j+1) == '*') {
# dp[i][j]=recur(i, j+2); // 正则串去掉两个
# } else {
# dp[i][j]=false;
# }
# } else {// 正则串非空 匹配串非空
# // 当前字符是否匹配
# boolean match=pattern.charAt(j) == text.charAt(i) | | pattern.charAt(j) == '.';
# if (j+2 <= pattern.length() & & pattern.charAt(j+1) == '*') {
# dp[i][j]=(match & recur(i+1, j)) | | // 当前匹配了, 看text的下个字符是否还可以用 * 匹配
# (recur(i, j+2)); // 当前不匹配, * 取0此重复
# } else {
# dp[i][j]=match & recur(i+1, j+1);
# }
# }
# return dp[i][j];
# }
# }










