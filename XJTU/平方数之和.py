# 给一个正整数n，寻找最少的完全平方数(1,4,9,16...)，使他们的和为n。
# 例如
# 16 = 4 + 4 + 4 +4
# 16 = 16
# 返回1 因为1个完全平方数16就能组成16
import queue
def numSquares(n):
    if n < 0:
        return 0
    #使用队列从起点n到终点0进行广度优先搜索
    q = queue.Queue()
    q.put((n,0))
    #减少重复计算
    visited = [False] * (n+1)
    visited[n] = True

    while not q.empty():
        tuple_num_step = q.get()
        num = tuple_num_step[0]
        step = tuple_num_step[1]
        # num == 0 表示已经找到0
        if num == 0:
            return step
        i = 1
        while num - i * i >= 0:
            if not visited[num - i*i]:
                # 表示从结点num到结点num-i*i有边，
                # 把结点和起点到该节点的路径长度组成的tuple入队
                q.put((num - i*i,step + 1))
                visited[num - i*i] = True
                i+=1
            else:
                i+=1
    print("no solution")
print(numSquares(16))