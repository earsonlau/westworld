# 1.
# 正则表达式匹配
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持
# '.' 和 '*' 的正则表达式匹配。
#
# '.'
# 匹配任意单个字符
# '*'
# 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 说明:
#
# s 可能为空，且只包含从 a - z 的小写字母。
# p 可能为空，且只包含从 a - z 的小写字母，以及字符 . 和  * 。
# 示例
# 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a"
# 无法匹配
# "aa"
# 整个字符串。
# 示例
# 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为
# '*'
# 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是
# 'a'。因此，字符串
# "aa"
# 可被视为
# 'a'
# 重复了一次。
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*"
# 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 示例
# 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为
# '*'
# 表示零个或多个，这里
# 'c'
# 为
# 0
# 个, 'a'
# 被重复一次。因此可以匹配字符串
# "aab"。
# 示例
# 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false


class Solution {
private String pattern;
private String text;
private Boolean[][] dp;
public boolean isMatch(String s, String p) {
if (s == null) s=new String();
if (p == null) p=new String();
// 空的正则串不能匹配s
if (s.length() != 0 & & p.length() == 0)


return false;
// 空正则串可以匹配空s
if (s.length() == 0 & & p.length() == 0) return true;

// 非空正则不一定可以匹配空s或非空s
// 此处由于要处理 * 使用递归解法
this.text = s;
this.pattern = p;
this.dp = new
Boolean[s.length() + 1][p.length() + 1];
return recur(0, 0);
}
// i为text的索引, j为pattern的索引
private
boolean
recur(int
i, int
j) {
if (j < pattern.length() & & i < text.length() & & dp[i][j] != null) return dp[i][j];
// 正则串为空
if (j == pattern.length()) return dp[i][j]=(i == text.length());
// 正则串非空
匹配串为空
if (i == text.length()) {
// 只可能 * 取0重才可能为真
if (j+1 < pattern.length() & & pattern.charAt(j+1) == '*') {
dp[i][j]=recur(i, j+2); // 正则串去掉两个
} else {
dp[i][j]=false;
}
} else {// 正则串非空 匹配串非空
// 当前字符是否匹配
boolean match=pattern.charAt(j) == text.charAt(i) | | pattern.charAt(j) == '.';
if (j+2 <= pattern.length() & & pattern.charAt(j+1) == '*') {
dp[i][j]=(match & recur(i+1, j)) | | // 当前匹配了, 看text的下个字符是否还可以用 * 匹配
(recur(i, j+2)); // 当前不匹配, * 取0此重复
} else {
dp[i][j]=match & recur(i+1, j+1);
}
}
return dp[i][j];
}
}
