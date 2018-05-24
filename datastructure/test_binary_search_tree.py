class Node:
    def __init__(self, key):
        self.key  = key
        self.left  = None
        self.right = None
        self.parent = None


def delete(node, x):
    if node:
        if x == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.data = search_min(node.right)
                node.right = delete_min(node.right)
        elif x < node.data:
            node.left = delete(node.left, x)
        else:
            node.right = delete(node.right, x)
    return node


# 最小値を探す
def search_min(node):
    if node.left is None: return node.data
    return search_min(node.left)


# 最小値を削除する
def delete_min(node):
    if node.left is None: return node.right
    node.left = delete_min(node.left)
    return node

# 高階関数バージョン
def traverse_h(func, node):
    if node:
        traverse_h(func, node.left)
        func(node.data)
        traverse_h(func, node.right)

# ジェネレータバージョン
def traverse(node):
    if node:
        for x in traverse(node.left):
            yield x
        yield node.data
        for x in traverse(node.right):
            yield x

def search(node, x):
    while node:
        if node.data == x: return True
        if x < node.data:
            node = node.left
        else:
            node = node.right
    return False


class BinaryTree:
    def __init__(self):
        self.root = None

    # 探索
    def search(self, k):
        return _search(self.root, k)
        

    def _search(x, k):
        if x == None or k == x.key:
            return x
        if k < x.key:
            return self._search(x.left, k)
        else:
            return self._search(x.right. k)


    def minimum(self):
        x = self.root
        while x.left != None:
            x = x.left
        return x


    def maximum(self)
        x = self.root
        while x.right != None:
            x = x.right
        return x


    def _successor(x):
        if x.right != None:
            return self.minimum(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = yy = y.parent
        return y

    
    # 中間順木巡回
    def inoder_walk(self):
        if self.root != None:
            self._inorder_walk(self.root)

    
    def _inorder_walk(self, node):
        if(node != None):
            self._inorder_walk(node.left)
            print(str(node.data))
            self._inorder_walk(node.right)


# テスト
if __name__ == '__main__':
    import random
    tree = BinaryTree()
    data = [random.randint(0, 100) for x in range(10)]
    print(data)
    print(tree)
    for k in data: tree.insert(k)
    print(tree)
    tree.printTree()
    
    for x in data:
        print('search', x, tree.search(x))
        print('delete', x)
        tree.delete(x)
        print('search', x, tree.search(x))
        print(tree)