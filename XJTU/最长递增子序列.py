testcase = [3,1,4,2,5,7]
def findlongestincreasesubsequence(l):
    #给定一个list，求最长递增子序列，返回长度
    #暴力解
    res = []#初始化一个res，用来存放以每一个位置结尾的递增子序列长度
    for i in range(len(l)):
        for j in range(i,-1,-1):
            if l[j] < l[i]:
                res.append(res[j]+1)
                #对每一个i位置的数从右往左找第一个比他小的数l[j]，如果找到了，
                #更新res[i]的值为res[j]+1
                break
        #没有找到比他小的数，更新res[i]的值为1
        if len(res) == i:
            res.append(1)
    print(res)
    max_ = res[0] #max_为最长递增自序列的长度
    for i in range(len(res)):
        max_ = max(max_,res[i])
    # return max_
    #下面打印最长递增子序列
    p = []
    end = res.index(max_)
    p.append(l[end])
    for i in range(end-1,-1,-1):
        if l[i] < l[end] and res[i] + 1 == res[end]:
            p.append(l[i])
            end = i
            continue
    return p[::-1]

print(findlongestincreasesubsequence(testcase))

