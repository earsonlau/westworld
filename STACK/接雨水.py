# 思路:
# 黑色的看成墙，蓝色的看成水，宽度一样，给定一个数组，每个数代表从左到右墙的高度，求出能装多少单位的水。也就是图中蓝色正方形的个数。
#
# 解法一：按行求
# 这是我最开始想到的一个解法，提交后直接 AC 了，自己都震惊了。就是先求高度为 11 的水，再求高度为 22 的水，再求高度为 33 的水。
#
# 整个思路就是，求第 i 层的水，遍历每个位置，如果当前的高度小于 i，并且两边有高度大于等于 i 的，说明这个地方一定有水，水就可以加 11。
#
# 如果求高度为 i 的水，首先用一个变量 temp 保存当前累积的水，初始化为 00。从左到右遍历墙的高度，遇到高度大于等于 i 的时候，开始更新 temp。更新原则是遇到高度小于 i 的就把 temp 加 11，遇到高度大于等于 i 的，就把 temp 加到最终的答案 ans 里，并且 temp 置零，然后继续循环。
#
# public int trap(int[] height) {
#     int sum = 0;
#     int max = getMax(height);//找到最大的高度，以便遍历。
#     for (int i = 1; i <= max; i++) {
#         boolean isStart = false; //标记是否开始更新 temp
#         int temp_sum = 0;
#         for (int j = 0; j < height.length; j++) {
#             if (isStart && height[j] < i) {
#                 temp_sum++;
#             }
#             if (height[j] >= i) {
#                 sum = sum + temp_sum;
#                 temp_sum = 0;
#                 isStart = true;
#             }
#         }
#     }
#     return sum;
# }
# private int getMax(int[] height) {
# 		int max = 0;
# 		for (int i = 0; i < height.length; i++) {
# 			if (height[i] > max) {
# 				max = height[i];
# 			}
# 		}
# 		return max;
# }
#
#
#
# 解法二：按列求
#
#
#
# public int trap(int[] height) {
#     int sum = 0;
#     //最两端的列不用考虑，因为一定不会有水。所以下标从 1 到 length - 2
#     for (int i = 1; i < height.length - 1; i++) {
#         int max_left = 0;
#         //找出左边最高
#         for (int j = i - 1; j >= 0; j--) {
#             if (height[j] > max_left) {
#                 max_left = height[j];
#             }
#         }
#         int max_right = 0;
#         //找出右边最高
#         for (int j = i + 1; j < height.length; j++) {
#             if (height[j] > max_right) {
#                 max_right = height[j];
#             }
#         }
#         //找出两端较小的
#         int min = Math.min(max_left, max_right);
#         //只有较小的一段大于当前列的高度才会有水，其他情况不会有水
#         if (min > height[i]) {
#             sum = sum + (min - height[i]);
#         }
#     }
#     return sum;
# }
#
#
#
# 解法三：动态规划
#
# 我们注意到，解法二中。对于每一列，我们求它左边最高的墙和右边最高的墙，都是重新遍历一遍所有高度，这里我们可以优化一下。
#
# 首先用两个数组，max_left [i] 代表第 i 列左边最高的墙的高度，max_right[i] 代表第 i 列右边最高的墙的高度。（一定要注意下，第 i 列左（右）边最高的墙，是不包括自身的，和 leetcode 上边的讲的有些不同）
#
# 对于 max_left我们其实可以这样求。
#
# max_left [i] = Max(max_left [i-1],height[i-1])。它前边的墙的左边的最高高度和它前边的墙的高度选一个较大的，就是当前列左边最高的墙了。
#
# 对于 max_right我们可以这样求。
#
# max_right[i] = Max(max_right[i+1],height[i+1]) 。它后边的墙的右边的最高高度和它后边的墙的高度选一个较大的，就是当前列右边最高的墙了。
#
# 这样，我们再利用解法二的算法，就不用在 for 循环里每次重新遍历一次求 max_left 和 max_right 了。
#
#
# 解法四：双指针
from typing import List
def trap(self, height: List[int]) -> int:
    if not height or len(height) <= 2:
        return 0
    left = 1
    right = len(height) - 2
    left_max = height[0]
    right_max = height[len(height) - 1]
    res = 0
    while left <= right:
        if left_max < right_max:
            if left_max > height[left]:
                res += left_max - height[left]
            left_max = max(left_max, height[left])
            left += 1
        else:
            if right_max > height[right]:
                res += right_max - height[right]
            right_max = max(right_max, height[right])
            right -= 1
    return res
