class Node:
    def __init__(self, x):
        self.data  = x
        self.left  = None
        self.right = None
        
            
def search(node, x):
    while node:
        if node.data == x: return True
        if x < node.data:
            node = node.left
        else:
            node = node.right
    return False


def insert(node, x):
    if node is None:return Node(x)
    elif x == node.data: return node
    elif x < node.data:
        node.left = insert(node.left, x)
    else:
        node.right = insert(node.right, x)
    return node


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
    
    
class BinaryTree:
    def __init__(self):
        self.root = None

    # 探索
    def search(self, x):
        return search(self.root, x)

    # 挿入
    def insert(self, x):
        self.root = insert(self.root, x)

    # 削除
    def delete(self, x):
        self.root = delete(self.root, x)

    # 巡回
    def traverse(self):
        for x in traverse(self.root):
            yield x
    
    # 出力
    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)
    
    
    def _printTree(self, node):
        if(node != None):
            self._printTree(node.left)
            print(str(node.data) + ' ')
            self._printTree(node.right)


# テスト
if __name__ == '__main__':
    import random
    tree = BinaryTree()
    data = [random.randint(0, 100) for x in range(10)]
    print(data)
    print(tree)
    for x in data: tree.insert(x)
    print(tree)
    tree.printTree()
    
    for x in data:
        print('search', x, tree.search(x))
        print('delete', x)
        tree.delete(x)
        print('search', x, tree.search(x))
        print(tree)