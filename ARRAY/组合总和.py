# 给定一个无重复元素的数组 candidates 和一个目标数 target ，
# 找出 candidates 中所有可以使数字和为 target 的组合。
#  candidates 中的数字可以无限制重复被选取。
#
#  说明：
#  所有数字（包括 target）都是正整数。
#  解集不能包含重复的组合。
#
#  示例 1:
#  输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
#
#  示例 2:
#  输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#  Related Topics 数组 回溯算法


#   解题思路
#   变量意义：use表示已经使用过的数（组成的列表），remain表示距离target还有多大。
#   具体实现：
#   1. 对candidates升序排序，以方便根据remain的大小使用return减小搜索空间；
#   2. 递归求可能的组合。具体的，每次递归时对所有candidates做一次遍历，情况有3：
#       1，满足条件，则答案加入一条；
#       2，不足，继续递归，
#       3，超出，则直接退出本路线。
#   3. 注意每层递归都对全体candidates做遍历会导致如[2,2,3],[3,2,2]这样的对称重复的答案的产生。
#   这是因为发生了“往前选择”的情况，
#   我们每次更深层的递归都往后缩小一个candidates，强制函数只能“往后选择”，这将不会出现重复答案。
#   4.代码写的比较简单，更多细节请看代码
#
from typing import List
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    if not candidates or len(candidates) == 0:
        return 0
    candidates = sorted(candidates) #对所有候选数进行排序
    ans = [] # 存放可能的组合
    find(0, [], target, ans)
    return ans

def find(start, use, remain,ans):
    # start表示每次从排序后的候选数中的第start位开始选数
    # use表示已经使用过的数（组成的列表），remain表示距离target还有多大。
    for i in range(start, len(candidates)):
        # 每回都从start位置开始向后寻找，这样就不会出现重复答案。
        c = candidates[i]  # c是一个临时变量存放候选数
        if c == remain:
            # 如果加上这个候选数后刚好碰到target，说明此时的use数组加上他刚好满足要求
            # 把它加入use后把整个use并入结果集
            ans.append(use + [c])
            return ans
        if c < remain:
            # 加上这个候选数还够不到target，说明还得再继续找数
            # 从i开始找，保证是向后寻找，use+[c]表示c要用，remain-c表示跟target距离缩短c
            find(i, use + [c], remain - c, ans)
        if c > remain:
            # 如果加上c溢出了，说明c不能加
            return ans

candidates = [2, 3, 6, 7]
target = 7
result = combinationSum(candidates, target)
print(result)


#
# #另一个解法，暂时没看懂
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         size = len(candidates)
#         if size == 0:
#             return []
#
#         # 剪枝是为了提速，在本题非必需
#         candidates.sort()
#         # 在遍历的过程中记录路径，它是一个栈
#         path = []
#         res = []
#         # 注意要传入 size ，在 range 中， size 取不到
#         self.__dfs(candidates, 0, size, path, res, target)
#         return res
#
#     def __dfs(self, candidates, begin, size, path, res, target):
#         # 先写递归终止的情况
#         if target == 0:
#             # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
#             # 或者使用 path.copy()
#             res.append(path[:])
#             return
#
#         for index in range(begin, size):
#             residue = target - candidates[index]
#             # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
#             if residue < 0:
#                 break
#             path.append(candidates[index])
#             # 因为下一层不能比上一层还小，起始索引还从 index 开始
#             self.__dfs(candidates, index, size, path, res, residue)
#             path.pop()