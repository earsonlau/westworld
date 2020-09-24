#求最小路径长度
class Solution:
    def walk(self,matrix,i,j):
        if i == len(matrix)-1 and j == len(matrix[0])-1:
            #已经在右下角
            return matrix[i][j]
        elif i == len(matrix) - 1:
            #已经在最后一行
            return matrix[i][j] + self.walk(matrix,i,j+1)
        elif j == len(matrix[0]) -1:
            #已经在最后一列
            return matrix[i][j] + self.walk(matrix,i+1,j)
        go_right = self.walk(matrix,i,j+1) #右边位置到终点的最短路径和
        go_down = self.walk(matrix,i+1,j) #下边位置到终点的最短路径和
        return matrix[i][j] + min (go_down,go_right)
sol=Solution()
m = [ [ 1, 3, 5, 9 ], [ 8, 1, 3, 4 ], [ 5, 0, 6, 1 ], [ 8, 8, 4, 0 ] ]
print(sol.walk(m,0,0))