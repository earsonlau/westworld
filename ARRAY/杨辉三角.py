
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
#  在杨辉三角中，每个数是它左上方和右上方的数的和。
#
#  示例:
#
#  输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#  Related Topics 数组
def yanghui(numRows):

    # 创建一个二维列表
    triangle = [[]]

    # 如果输入的数小于零那么就返回空二维列表
    if (numRows <= 0):
        return triangle;

    # 获得集合中的第一个元素（里面放的全是集合）也就是获得到的其实还是一个集合
    triangle[0].append(1)
    print("添加第一个元素：", triangle)

    # 然后从集合的一个元素（也是集合）开始遍历
    for i in range(1, numRows):
        # 每一个元素后创建一个新的集合
        tmp = []
        # 这是获得一个当前元素的上一个元素，也就是获得一个集合
        prevrow = triangle[i - 1]
        # 这是添加每行的第一个1
        tmp.append(1)
        print("添加每行的第一个1：", tmp)
        # 这个循环是控制每行添加一个1后应该还添加几个元素（对每行而言）
        for j in range(1, i):
            # 添加什么元素（添加的就是上一行当前位置和他前一个位置的和）
            tmp.append(prevrow[j] + prevrow[j - 1])
        print("添加最后一个1前面的数字：", tmp[1:])
        # 然后在添加每行最后一个元素1
        tmp.append(1)
        print("添加最后一个1：", tmp)
        # 然后把这个集合给添加到集合中去
        triangle.append(tmp)
        print("把这个集合塞进triangle：", triangle)
    return triangle