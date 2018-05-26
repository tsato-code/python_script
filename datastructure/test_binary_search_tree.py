class Node:
    def __init__(self, key):
        self.key  = key
        self.left  = None
        self.right = None
        self.parent = None


    def __repr__(self):
        return "<Node {}>".format(self.key)


class BinaryTree:
    # コンストラクタ
    def __init__(self):
        self.root = None


    def __repr__(self):
        return "<Binary Search Tree {}>".format(self.root)


    # 中間順木巡回
    def inorder_walk(self):
        if self.root != None:
            self._inorder_walk(self.root)

    
    def _inorder_walk(self, x):
        if x != None:
            self._inorder_walk(x.left)
            print(x.key)
            self._inorder_walk(x.right)


    # 探索
    def search(self, x, k):
        if x is None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)


    # 最小値
    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    # 最大値
    def maximum(self, x):
        while x.right is not None:
            x = x.right
        return x


    # 挿入
    def insert(self, z):
        z = Node(z)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z


    # 移植
    def _transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent


    # 削除
    def delete(self, key):
        z = self.search(self.root, key)
        if z.left == None:
            self._transplant(z, z.right)
        elif z.right == None:
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y


if __name__ == '__main__':

    # データ作成
    import random
    data = [random.randint(0, 100) for x in range(10)]
    print(data)

    # 2分探索木作成
    tree = BinaryTree()

    # insert
    for k in data: tree.insert(k)

    # 出力
    tree.inorder_walk()

    # 消去
    for k in data:
        print('* '*10)
        tree.delete(k)
        tree.inorder_walk()


"""
$ python test_binary_search_tree.py 
[46, 94, 85, 85, 1, 27, 75, 25, 81, 15]
1
15
25
27
46
75
81
85
85
94
* * * * * * * * * * 
1
15
25
27
75
81
85
85
94
* * * * * * * * * * 
1
15
25
27
75
81
85
85
* * * * * * * * * * 
1
15
25
27
75
81
85
* * * * * * * * * * 
1
15
25
27
75
81
* * * * * * * * * * 
15
25
27
75
81
* * * * * * * * * * 
15
25
75
81
* * * * * * * * * * 
15
25
81
* * * * * * * * * * 
15
81
* * * * * * * * * * 
15
* * * * * * * * * * 
"""