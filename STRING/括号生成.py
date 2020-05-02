# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# 回溯算法（深度优先遍历）

# import java.util.List;
#
# public class Solution {
#
#     // 做减法
#
#     public List<String> generateParenthesis(int n) {
#         List<String> res = new ArrayList<>();
#         // 特判
#         if (n == 0) {
#             return res;
#         }
#
#         // 执行深度优先遍历，搜索可能的结果
#         dfs("", n, n, res);
#         return res;
#     }
#
#     /**
#      * @param curStr 当前递归得到的结果
#      * @param left   左括号还有几个可以使用
#      * @param right  右括号还有几个可以使用
#      * @param res    结果集
#      */
#     private void dfs(String curStr, int left, int right, List<String> res) {
#         // 因为每一次尝试，都使用新的字符串变量，所以无需回溯
#         // 在递归终止的时候，直接把它添加到结果集即可，注意与「力扣」第 46 题、第 39 题区分
#         if (left == 0 && right == 0) {
#             res.add(curStr);
#             return;
#         }
#
#         // 剪枝（如图，左括号可以使用的个数严格大于右括号可以使用的个数，才剪枝，注意这个细节）
#         if (left > right) {
#             return;
#         }
#
#         if (left > 0) {
#             dfs(curStr + "(", left - 1, right, res);
#         }
#
#         if (right > 0) {
#             dfs(curStr + ")", left, right - 1, res);
#         }
#     }
# }
#
# #广度优先遍历
# import java.util.ArrayDeque;
# import java.util.ArrayList;
# import java.util.Deque;
# import java.util.LinkedList;
# import java.util.List;
# import java.util.Queue;
#
# public class Solution {
#
#     class Node {
#         /**
#          * 当前得到的字符串
#          */
#         private String res;
#         /**
#          * 剩余左括号数量
#          */
#         private int left;
#         /**
#          * 剩余右括号数量
#          */
#         private int right;
#
#         public Node(String str, int left, int right) {
#             this.res = str;
#             this.left = left;
#             this.right = right;
#         }
#     }
#
#     public List<String> generateParenthesis(int n) {
#         List<String> res = new ArrayList<>();
#         if (n == 0) {
#             return res;
#         }
#         Queue<Node> queue = new LinkedList<>();
#         queue.offer(new Node("", n, n));
#
#         while (!queue.isEmpty()) {
#
#             Node curNode = queue.poll();
#             if (curNode.left == 0 && curNode.right == 0) {
#                 res.add(curNode.res);
#             }
#             if (curNode.left > 0) {
#                 queue.offer(new Node(curNode.res + "(", curNode.left - 1, curNode.right));
#             }
#             if (curNode.right > 0 && curNode.left < curNode.right) {
#                 queue.offer(new Node(curNode.res + ")", curNode.left, curNode.right - 1));
#             }
#         }
#         return res;
#     }
# }
#
# #动态规划
# import java.util.ArrayList;
# import java.util.List;
#
# public class Solution {
#
#     // 把结果集保存在动态规划的数组里
#
#     public List<String> generateParenthesis(int n) {
#         if (n == 0) {
#             return new ArrayList<>();
#         }
#         // 这里 dp 数组我们把它变成列表的样子，方便调用而已
#         List<List<String>> dp = new ArrayList<>(n);
#
#         List<String> dp0 = new ArrayList<>();
#         dp0.add("");
#         dp.add(dp0);
#
#         for (int i = 1; i <= n; i++) {
#             List<String> cur = new ArrayList<>();
#             for (int j = 0; j < i; j++) {
#                 List<String> str1 = dp.get(j);
#                 List<String> str2 = dp.get(i - 1 - j);
#                 for (String s1 : str1) {
#                     for (String s2 : str2) {
#                         // 枚举右括号的位置
#                         cur.add("(" + s1 + ")" + s2);
#                     }
#                 }
#             }
#             dp.add(cur);
#         }
#         return dp.get(n);
#     }
# }

class Solution:
    # 把结果集保存在动态规划的数组里
    def generateParenthesis(self,n):
        if n == 0:
            return
        # 这里 dp 用list
        dp = []
        dp0 = []
        dp0.append("")
        dp.append(dp0)
        for i in range (1,n+1):
            cur = []
            for j in range(i):
                str1 = dp[j]
                str2 = dp[i - 1 - j]
                for s1 in str1 :
                    for s2 in str2:
                        # 枚举右括号的位置
                        cur.append("("+ s1 + ")" + s2)
            dp.append(cur)
        return dp[n]