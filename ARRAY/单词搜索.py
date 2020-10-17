# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#  
#
# 提示：
#
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3

#思路:
# 对矩阵的每一个位置都朝着上下左右四个方向进行搜索
# 每次搜索都是递归进行深度优先遍历，不匹配的时候就回溯到上一层换一下方向，没得换了再回上一层

# 递归函数：
# 不变变量：board表示字母矩阵，word表示给定单词
# 变化变量：index表示现在遍历到word的第几个字母
# start_x表示起始位置的横坐标
# start_y表示起始位置的纵坐标
# marked标记矩阵中在这次递归中被访问过的字母（"不匹配->回溯"时标记会被擦除）
# 从(start_x,start_y)位置开始递归搜索
# 终止条件：index == len(word)-1 （即index指向word的最后一个字母）
#           若匹配返回True，不匹配返回False
# 不满足终止条件则遍历上下左右方向，匹配则进入深层递归
#回溯算法

from typing import List
class Solution:
    #         (x-1,y)
    # (x,y-1) (x,y) (x,y+1)
    #         (x+1,y)

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]#左,上,下,右
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        marked = [[False for _ in range(n)] for _ in range(m)]#一个m*n的二维数组
        for i in range(m):
            for j in range(n):
                # 对每一个格子都从word的第一个字母开始搜索
                if self.__search_word(board, word, 0, i, j, marked, m, n):
                    return True
        return False

    def __search_word(self, board, word, index,
                      start_x, start_y, marked, m, n):
        #深度优先遍历
        # 不变变量：board表示字母矩阵，word表示给定单词
        # 变化变量：index表示现在遍历到word的第几个字母
        # start_x表示起始位置的横坐标
        # start_y表示起始位置的纵坐标
        # marked标记矩阵中在这次递归中被访问过的字母（"不匹配->回溯"时标记会被擦除）

        # 先写递归终止条件
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]

        # 中间匹配了，再继续搜索
        if board[start_x][start_y] == word[index]:
            # 先占住这个位置，搜索不成功的话，要释放掉
            marked[start_x][start_y] = True
            for direction in self.directions:# 分别从左,上,下,右四个方向进行搜索
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                # 注意：如果这一次 search word 成功的话，就返回
                if 0 <= new_x < m and 0 <= new_y < n and \
                        not marked[new_x][new_y] and \
                        self.__search_word(board, word,
                                           index + 1,
                                           new_x, new_y,
                                           marked, m, n):
                    return True
            #不匹配时标记会被擦除
            marked[start_x][start_y] = False
        return False