"""
1. 同じ値のキーが複数あるとdeleteできないバグ
2. マージ操作の関数化
3. 存在しないキーのdelete
"""
class Node(object):
    def __init__(self, t):
        self.n  = None
        self.keys = []
        self.leaf = False
        self.c = []


    def __repr__(self):
        # return "<Node: (n, keys, leaf, c) = ({}, {}, {}, {})>".format(self.n, self.keys, self.leaf, self.c)
        if self.leaf:
        	return "<Node: (n, keys, leaf) = ({}, {}, {})>".format(self.n, self.keys, self.leaf)
        return "<Node: (n, keys, leaf) = ({}, {}, {})>\n{}".format(self.n, self.keys, self.leaf, "\n".join([x.__repr__() for x in self.c]))
        

class B_Tree(object):
	def __init__(self, t):
		self.t = t
		self.root = None
		self.create()


	def create(self):
		x = Node(self.t)
		x.leaf = True
		x.n = 0
		self.root = x


	def search(self, x, k):
		i = 0
		while i < x.n and k > x.keys[i]:
			i += 1
		if i < x.n and k == x.keys[i]:
			return (x, i)
		elif x.leaf:
			return None
		else:
			return self.search(x.c[i], k)


	def insert(self, k):
		r = self.root
		self._insert(r, k)
		

	def _insert(self, x, k):
		if x.n == 2*self.t - 1:
			s = Node(self.t)
			self.root = s
			s.leaf = False
			s.n = 0
			s.c.append(x)
			self._split_child(s, 0)
			self._insert_nonfull(s, k)
		else:
			self._insert_nonfull(x, k)


	def _split_child(self, x, i):

		z = Node(self.t)
		y = x.c[i]
		z.leaf = y.leaf
		z.n = self.t - 1

		# yのキーをzに移動
		z.keys[:self.t-1] = y.keys[self.t:2*self.t-1]
			
		# yの子どもをzに移動
		if not y.leaf:
			z.c = y.c[self.t:2*self.t]
		y.n = self.t - 1
		x.c[i+2:x.n+2] = x.c[i+1:x.n+1]

		# テキストから修正
		if len(x.c) == i+1:
			x.c.append(z)
		else:
			x.c[i+1] = z

		# xのキーを移動
		x.keys.append(y.keys[self.t-1])
		x.keys = sorted(x.keys)
		x.n = x.n + 1

		# テキストには書いてない
		y.keys = y.keys[:self.t-1]
		y.c = y.c[:self.t]


	def _insert_nonfull(self, x, k):
		i = x.n
		if x.leaf:
			# kの挿入位置を見つける
			x.keys.append(k)
			x.keys = sorted(x.keys)
			x.n += 1
		else:
			while i >= 1 and k < x.keys[i-1]:
				i -= 1
			if x.c[i].n == 2*self.t - 1:
				self._split_child(x, i)
				if k > x.keys[i]:
					i += 1
			self._insert_nonfull(x.c[i], k)


	def _max_key(self, x):
		while not x.leaf:
			x = x.c[-1]
		return x.keys[-1]


	def _min_key(self, x):
		while not x.leaf:
			x = x.c[0]
		return x.keys[0]


	def delete(self, x, k):
		if k in x.keys:
			# xが葉のとき
			if x.leaf:
				x.keys.remove(k)
				x.n -= 1

			# xが中間ノードのとき
			else:
				i = x.keys.index(k)
				y = x.c[i]
				z = x.c[i+1]

				# 2a
				if y.n >= self.t:
					# yから最大値k1を探す
					k1 = self._max_key(y)
					# 再帰的にk1を削除
					self.delete(y, k1)
					# kをk1に張替え
					x.keys[i] = k1

				# 2b
				elif z.n >= self.t:
					# zから最小値を探す
					k2 = self._min_key(z)
					# 再帰的にk2を削除
					self.delete(z, k2)
					# kをk2に張替え
					x.keys[i] = k2

				# 2c
				else:
					# マージ
					y.keys.append(x.keys.pop(i))
					y.keys += z.keys
					y.c += z.c
					y.n = 2*self.t - 1
					# キーと子の消去
					x.c.pop(i+1)
					x.n -= 1
		else:
			i = 0
			while i < x.n and k > x.keys[i]:
				i += 1
			if x.c[i].n == self.t-1:
				if 0 < i: y = x.c[i-1]
				if i < x.n: z = x.c[i+1]

				# 3a 左右どちらかの子のキーがt個なら移送
				if 0 < i and y.n >= self.t:
					k1 = self._max_key(y)
					self.delete(y, k1)
					k0 = x.keys[i-1]
					self._insert(x.c[i], k0)
					x.keys[i-1] = k1

				elif i < x.n and z.n >= self.t:
					k2 = self._min_key(z)
					self.delete(z, k2)
					k0 = x.keys[i]
					self._insert(x.c[i], k0)
					x.keys[i] = k2
				
				# 3b 左右どちらかの子のキーがt-1個ならマージ
				elif i < x.n and z.n == self.t-1:
					# zとマージ
					x.c[i].keys.append(x.keys.pop(i))
					x.c[i].keys += z.keys
					x.c[i].c += z.c
					x.c[i].n = 2*self.t - 1
					x.c.pop(i+1)
					x.n -= 1
				elif 0 < i and y.n == self.t-1:
					# yとマージ
					y.keys.append(x.keys.pop(i-1))
					y.keys += x.c[i].keys
					y.c += x.c[i].c
					y.n = 2*self.t - 1
					x.c.pop(i)
					x.n -= 1
					i -= 1
			self.delete(x.c[i], k)


	def show(self):
		if self.root != None:
			self._inorder_walk(self.root)


	def _inorder_walk(self, x):
		if x.leaf:
			for k in x.keys:
				print(k)
		elif x != None:
			for i, k in enumerate(x.keys):
				self._inorder_walk(x.c[i])
				print(k)
			self._inorder_walk(x.c[-1])



if __name__ == '__main__':

	# データ作成
    import random
    data = [random.randint(0, 100) for x in range(15)]
    print(data)

    # 2分探索木作成
    tree = B_Tree(t=2)

    # insert
    for k in data:
    	print('\ninsert {}'.format(k))
    	tree.insert(k)
    	print('\n{}'.format(tree.root))

    # search
    print('\nsearch: {}'.format(data[0]))
    res = tree.search(tree.root, data[0])
    print(res)

    # show
    tree.show()

    # delete
    for k in data:
	    print('\ndelete: {}'.format(k))
	    tree.delete(tree.root, k)
	    print('\n{}'.format(tree.root))


"""
$ python datastructure/test_b_tree.py 
[86, 54, 46, 34, 37, 70, 6, 58, 74, 62, 20, 36, 62, 74, 34]

insert 86

<Node: (n, keys, leaf) = (1, [86], True)>

insert 54

<Node: (n, keys, leaf) = (2, [54, 86], True)>

insert 46

<Node: (n, keys, leaf) = (3, [46, 54, 86], True)>

insert 34

<Node: (n, keys, leaf) = (1, [54], False)>
<Node: (n, keys, leaf) = (2, [34, 46], True)>
<Node: (n, keys, leaf) = (1, [86], True)>

insert 37

<Node: (n, keys, leaf) = (1, [54], False)>
<Node: (n, keys, leaf) = (3, [34, 37, 46], True)>
<Node: (n, keys, leaf) = (1, [86], True)>

insert 70

<Node: (n, keys, leaf) = (1, [54], False)>
<Node: (n, keys, leaf) = (3, [34, 37, 46], True)>
<Node: (n, keys, leaf) = (2, [70, 86], True)>

insert 6

<Node: (n, keys, leaf) = (2, [37, 54], False)>
<Node: (n, keys, leaf) = (2, [6, 34], True)>
<Node: (n, keys, leaf) = (1, [46], True)>
<Node: (n, keys, leaf) = (2, [70, 86], True)>

insert 58

<Node: (n, keys, leaf) = (2, [37, 54], False)>
<Node: (n, keys, leaf) = (2, [6, 34], True)>
<Node: (n, keys, leaf) = (1, [46], True)>
<Node: (n, keys, leaf) = (3, [58, 70, 86], True)>

insert 74

<Node: (n, keys, leaf) = (3, [37, 54, 70], False)>
<Node: (n, keys, leaf) = (2, [6, 34], True)>
<Node: (n, keys, leaf) = (1, [46], True)>
<Node: (n, keys, leaf) = (1, [58], True)>
<Node: (n, keys, leaf) = (2, [74, 86], True)>

insert 62

<Node: (n, keys, leaf) = (1, [54], False)>
<Node: (n, keys, leaf) = (1, [37], False)>
<Node: (n, keys, leaf) = (2, [6, 34], True)>
<Node: (n, keys, leaf) = (1, [46], True)>
<Node: (n, keys, leaf) = (1, [70], False)>
<Node: (n, keys, leaf) = (2, [58, 62], True)>
<Node: (n, keys, leaf) = (2, [74, 86], True)>

insert 20

<Node: (n, keys, leaf) = (1, [54], False)>
<Node: (n, keys, leaf) = (1, [37], False)>
<Node: (n, keys, leaf) = (3, [6, 20, 34], True)>
<Node: (n, keys, leaf) = (1, [46], True)>
<Node: (n, keys, leaf) = (1, [70], False)>
<Node: (n, keys, leaf) = (2, [58, 62], True)>
<Node: (n, keys, leaf) = (2, [74, 86], True)>

insert 36

<Node: (n, keys, leaf) = (1, [54], False)>
<Node: (n, keys, leaf) = (2, [20, 37], False)>
<Node: (n, keys, leaf) = (1, [6], True)>
<Node: (n, keys, leaf) = (2, [34, 36], True)>
<Node: (n, keys, leaf) = (1, [46], True)>
<Node: (n, keys, leaf) = (1, [70], False)>
<Node: (n, keys, leaf) = (2, [58, 62], True)>
<Node: (n, keys, leaf) = (2, [74, 86], True)>

insert 62

<Node: (n, keys, leaf) = (1, [54], False)>
<Node: (n, keys, leaf) = (2, [20, 37], False)>
<Node: (n, keys, leaf) = (1, [6], True)>
<Node: (n, keys, leaf) = (2, [34, 36], True)>
<Node: (n, keys, leaf) = (1, [46], True)>
<Node: (n, keys, leaf) = (1, [70], False)>
<Node: (n, keys, leaf) = (3, [58, 62, 62], True)>
<Node: (n, keys, leaf) = (2, [74, 86], True)>

insert 74

<Node: (n, keys, leaf) = (1, [54], False)>
<Node: (n, keys, leaf) = (2, [20, 37], False)>
<Node: (n, keys, leaf) = (1, [6], True)>
<Node: (n, keys, leaf) = (2, [34, 36], True)>
<Node: (n, keys, leaf) = (1, [46], True)>
<Node: (n, keys, leaf) = (1, [70], False)>
<Node: (n, keys, leaf) = (3, [58, 62, 62], True)>
<Node: (n, keys, leaf) = (3, [74, 74, 86], True)>

insert 34

<Node: (n, keys, leaf) = (1, [54], False)>
<Node: (n, keys, leaf) = (2, [20, 37], False)>
<Node: (n, keys, leaf) = (1, [6], True)>
<Node: (n, keys, leaf) = (3, [34, 34, 36], True)>
<Node: (n, keys, leaf) = (1, [46], True)>
<Node: (n, keys, leaf) = (1, [70], False)>
<Node: (n, keys, leaf) = (3, [58, 62, 62], True)>
<Node: (n, keys, leaf) = (3, [74, 74, 86], True)>

search: 86
(<Node: (n, keys, leaf) = (3, [74, 74, 86], True)>, 2)
6
20
34
34
36
37
46
54
58
62
62
70
74
74
86

delete: 86

<Node: (n, keys, leaf) = (1, [46], False)>
<Node: (n, keys, leaf) = (2, [20, 36], False)>
<Node: (n, keys, leaf) = (1, [6], True)>
<Node: (n, keys, leaf) = (2, [34, 34], True)>
<Node: (n, keys, leaf) = (1, [37], True)>
<Node: (n, keys, leaf) = (2, [62, 70], False)>
<Node: (n, keys, leaf) = (2, [54, 58], True)>
<Node: (n, keys, leaf) = (1, [62], True)>
<Node: (n, keys, leaf) = (2, [74, 74], True)>

delete: 54

<Node: (n, keys, leaf) = (1, [46], False)>
<Node: (n, keys, leaf) = (2, [20, 36], False)>
<Node: (n, keys, leaf) = (1, [6], True)>
<Node: (n, keys, leaf) = (2, [34, 34], True)>
<Node: (n, keys, leaf) = (1, [37], True)>
<Node: (n, keys, leaf) = (2, [62, 70], False)>
<Node: (n, keys, leaf) = (1, [58], True)>
<Node: (n, keys, leaf) = (1, [62], True)>
<Node: (n, keys, leaf) = (2, [74, 74], True)>

delete: 46

<Node: (n, keys, leaf) = (1, [37], False)>
<Node: (n, keys, leaf) = (2, [20, 34], False)>
<Node: (n, keys, leaf) = (1, [6], True)>
<Node: (n, keys, leaf) = (1, [34], True)>
<Node: (n, keys, leaf) = (1, [36], True)>
<Node: (n, keys, leaf) = (2, [62, 70], False)>
<Node: (n, keys, leaf) = (1, [58], True)>
<Node: (n, keys, leaf) = (1, [62], True)>
<Node: (n, keys, leaf) = (2, [74, 74], True)>

delete: 34

<Node: (n, keys, leaf) = (1, [37], False)>
<Node: (n, keys, leaf) = (1, [20], False)>
<Node: (n, keys, leaf) = (1, [6], True)>
<Node: (n, keys, leaf) = (3, [34, 34, 36], True)>
<Node: (n, keys, leaf) = (2, [62, 70], False)>
<Node: (n, keys, leaf) = (1, [58], True)>
<Node: (n, keys, leaf) = (1, [62], True)>
<Node: (n, keys, leaf) = (2, [74, 74], True)>

delete: 37

<Node: (n, keys, leaf) = (1, [58], False)>
<Node: (n, keys, leaf) = (1, [20], False)>
<Node: (n, keys, leaf) = (1, [6], True)>
<Node: (n, keys, leaf) = (3, [34, 34, 36], True)>
<Node: (n, keys, leaf) = (1, [70], False)>
<Node: (n, keys, leaf) = (2, [62, 62], True)>
<Node: (n, keys, leaf) = (2, [74, 74], True)>

delete: 70

<Node: (n, keys, leaf) = (0, [], False)>
<Node: (n, keys, leaf) = (3, [20, 58, 62], False)>
<Node: (n, keys, leaf) = (1, [6], True)>
<Node: (n, keys, leaf) = (3, [34, 34, 36], True)>
<Node: (n, keys, leaf) = (1, [62], True)>
<Node: (n, keys, leaf) = (2, [74, 74], True)>

delete: 6

<Node: (n, keys, leaf) = (0, [], False)>
<Node: (n, keys, leaf) = (3, [34, 58, 62], False)>
<Node: (n, keys, leaf) = (1, [20], True)>
<Node: (n, keys, leaf) = (2, [34, 36], True)>
<Node: (n, keys, leaf) = (1, [62], True)>
<Node: (n, keys, leaf) = (2, [74, 74], True)>

delete: 58

<Node: (n, keys, leaf) = (0, [], False)>
<Node: (n, keys, leaf) = (3, [34, 36, 62], False)>
<Node: (n, keys, leaf) = (1, [20], True)>
<Node: (n, keys, leaf) = (1, [34], True)>
<Node: (n, keys, leaf) = (1, [62], True)>
<Node: (n, keys, leaf) = (2, [74, 74], True)>

delete: 74

<Node: (n, keys, leaf) = (0, [], False)>
<Node: (n, keys, leaf) = (3, [34, 36, 62], False)>
<Node: (n, keys, leaf) = (1, [20], True)>
<Node: (n, keys, leaf) = (1, [34], True)>
<Node: (n, keys, leaf) = (1, [62], True)>
<Node: (n, keys, leaf) = (1, [74], True)>

delete: 62

<Node: (n, keys, leaf) = (0, [], False)>
<Node: (n, keys, leaf) = (2, [34, 36], False)>
<Node: (n, keys, leaf) = (1, [20], True)>
<Node: (n, keys, leaf) = (1, [34], True)>
<Node: (n, keys, leaf) = (3, [62, 62, 74], True)>

delete: 20

<Node: (n, keys, leaf) = (0, [], False)>
<Node: (n, keys, leaf) = (1, [36], False)>
<Node: (n, keys, leaf) = (2, [34, 34], True)>
<Node: (n, keys, leaf) = (3, [62, 62, 74], True)>

delete: 36

<Node: (n, keys, leaf) = (0, [], False)>
<Node: (n, keys, leaf) = (1, [34], False)>
<Node: (n, keys, leaf) = (1, [34], True)>
<Node: (n, keys, leaf) = (3, [62, 62, 74], True)>

delete: 62

<Node: (n, keys, leaf) = (0, [], False)>
<Node: (n, keys, leaf) = (1, [34], False)>
<Node: (n, keys, leaf) = (1, [34], True)>
<Node: (n, keys, leaf) = (2, [62, 74], True)>

delete: 74

<Node: (n, keys, leaf) = (0, [], False)>
<Node: (n, keys, leaf) = (1, [34], False)>
<Node: (n, keys, leaf) = (1, [34], True)>
<Node: (n, keys, leaf) = (1, [62], True)>

delete: 34

<Node: (n, keys, leaf) = (0, [], False)>
<Node: (n, keys, leaf) = (0, [], False)>
<Node: (n, keys, leaf) = (3, [34, 34, 62], True)>
"""