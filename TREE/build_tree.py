class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def show(self):
        return

    def construct(self,list_to_build = None):
        if not list_to_build:
            return None
        tl = []
        for i in list_to_build:
            if i is None:
                tl.append(None)
            else:
                tl.append(TreeNode(i))
        print(tl)
        for idx in range(int(len(list_to_build) / 2 )):
            if tl[idx]:
                if idx * 2 + 1 < len(tl) and tl[idx * 2 + 1]:
                    tl[idx].left = tl[idx * 2 + 1]

                if idx * 2 + 2 < len(tl) and tl[idx * 2 + 2]:
                    tl[idx].right = tl[idx * 2 + 2]
            else:
                continue

        self.root = tl[0]

    def pre_order(self, root):
        if not root:
            return []
        res = []
        res.append(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)
        print(res)

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.val)
        self.in_order(root.right)

    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val)


l = [2, 3, 4, 5, None, 7]
t = Tree()
t.construct(l)
