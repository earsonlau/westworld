# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
# 示例 1:
#
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:
#
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
# 这里的方法不需要记录已经走过的路径，所以执行用时和内存消耗都相对较小
#
# 首先设定上下左右边界
# 其次向右移动到最右，此时第一行因为已经使用过了，可以将其从图中删去，体现在代码中就是重新定义上边界
# 判断若重新定义后，上下边界交错，表明螺旋矩阵遍历结束，跳出循环，返回答案
# 若上下边界不交错，则遍历还未结束，接着向下向左向上移动，操作过程与第一，二步同理
# 不断循环以上步骤，直到某两条边界交错，跳出循环，返回答案

class Solution:
    def spiralOrder(self,matrix):
        ans = []
        if (matrix is None or len(matrix) == 0):
            return ans
        u = 0
        d = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1
        while(1):
            for i in range(l,r+1):
                # i = i + 1
                ans.append(matrix[u][i])
            u = u + 1
            if u > d :
                break
            for i in range(u,d+1):
                # i = i + 1
                ans.append(matrix[i][r])
            r = r - 1
            if r < l :
                break
            for i in range(r,l-1,-1):
                # i = i - 1
                ans.append(matrix[d][i])
            d = d - 1
            if d < u :
                break
            for i in range(d,u-1,-1):
                # i = i - 1
                ans.append(matrix[i][l])
            l = l + 1
            if l > r :
                break
        return ans
a = Solution()
matrix = \
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(a.spiralOrder(matrix))