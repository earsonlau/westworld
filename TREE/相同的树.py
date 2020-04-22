def isSameTree(root1, root2):
    # // 都为空的话，显然相同
    if (root1 is None and root2 is None): return True
    # // 一个为空，一个非空，显然不同
    if (root1 is None or root2 is None): return False
    # // 两个都非空，但 val 不一样也不行
    if (root1.val != root2.val): return False
    # // root1 和 root2 该比的都比完了
    return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
