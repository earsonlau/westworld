
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
#  示例 1：
#
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
#  示例 2：
#
#  输入: "cbbd"
# 输出: "bb"
#
#  Related Topics 字符串 动态规划
#
# key：双指针
#
# 寻找回文串的问题核心思想是：从中间开始向两边扩散来判断回文串。
#

# string palindrome(string s):
#     string res;
#     for(i=0; i<s.size();i++){
#         //以 s[i] 为中心的回文串
#         string s1 = palindrome(s,i,i);
#         //以 s[i] 和 s[i+1] 为中心的回文串
#         string s2 = palindrome(s,i,i+1);
#         // res = longest(res,s1,s2)
#         res = res.size() > s1.size() ? res : s1;
#         res = res.size() > s2.size() ? res : s2;
#     }
#     return res;
# }

