# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
#  说明：不允许修改给定的链表。
#
#  示例 1：
#
#  输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#  示例 2：
#
#  输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#  示例 3：
#
#  输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
#
#
#  进阶：
# 你是否可以不用额外空间解决此题？
#  Related Topics 链表 双指针

# BFS 参考了官方题解的邻接表构建
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS
        from collections import deque, defaultdict
        # 先验判断
        if endWord not in wordList:
            return 0
        # 提前构建邻接表 -> 用generic state做key
        intermidiateWords = defaultdict(list)
        wordLen = len(beginWord)
        for word in wordList:
            for i in range(wordLen):
                intermidiateWords[word[:i] + '*' + word[i+1:]].append(word)
        # 建队列 加初始状态
        queue = deque()
        memo = set()
        queue.append(beginWord)
        memo.add(beginWord)
        step = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                curWord = queue.popleft()
                for i in range(wordLen):
                    intermidiateCurWord = curWord[:i] + '*' + curWord[i+1:]
                    # 下一个状态的所有word
                    for word in intermidiateWords[intermidiateCurWord]:
                        if word == endWord:
                            return step + 1
                        if word not in memo:
                            queue.append(word)
                            memo.add(word)
            step += 1
        else:
            return 0
#
# 作者：cui-jin-hao-_official
# 链接：https://leetcode-cn.com/problems/word-ladder/solution/python-bfs-shuang-xiang-bfs-by-cui-jin-hao-_offici/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。