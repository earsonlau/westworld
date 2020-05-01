# # 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# #
# # 示例 1:
# #
# # 输入: 123
# # 输出: 321
# #
# # 示例 2:
# #
# # 输入: -123
# # 输出: -321
# #
# # 示例 3:
# #
# # 输入: 120
# # 输出: 21
# #
# # 注意:
# #
# # 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
# # 请根据这个假设，如果反转后整数溢出那么就返回 0。
#
#     1 	class Solution {
#     2 	    public int reverse(int x) {
#     3 	        int ans = 0;
#     4 	        while (x != 0) {
#     5 	            int pop = x % 10;
#     6 	            // 溢出判断
#     7 	            if (ans > Integer.MAX_VALUE / 10 || (ans == Integer.MAX_VALUE / 10 && pop > 7))
#     8 	                return 0;
#     9 	            if (ans < Integer.MIN_VALUE / 10 || (ans == Integer.MIN_VALUE / 10 && pop < -8))
#    10 	                return 0;
#    11 	            ans = ans * 10 + pop;
#    12 	            x /= 10;
#    13 	        }
#    14 	        return ans;
#    15 	    }
# 	}
class Solution:
    def reverse(self,x):
        ans = 0
        while x != 0:
            pop = x % 10
            # 溢出判断
            if ans > float('inf') / 10 or ( ans == float('inf') / 10 and pop > 7):
                return 0
            if ans < -float('inf') / 10 or (ans == -float('inf') / 10 and pop < -8):
                return 0
            ans = ans * 10 + pop
            x /= 10
        return ans
