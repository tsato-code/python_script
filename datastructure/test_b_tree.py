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


	def delete(self, k):
		self._delete(self.root, k)
		if self.root.n == 0 and self.root.c != []: 	# 2018-05-30 根が空かつ子が非空
			self.root = self.root.c[0]


	def _delete(self, x, k):
		if k in x.keys:
			# xが葉のとき
			if x.leaf:
				x.keys.remove(k)
				x.n -= 1

			# xが葉でないとき
			else:
				i = x.keys.index(k)
				y = x.c[i]
				z = x.c[i+1]

				# 2a
				if y.n >= self.t:
					# yから最大値k1を探す
					k1 = self._max_key(y)
					# 再帰的にk1を削除
					self._delete(y, k1)
					# kをk1に張替え
					x.keys[i] = k1

				# 2b
				elif z.n >= self.t:
					# zから最小値を探す
					k2 = self._min_key(z)
					# 再帰的にk2を削除
					self._delete(z, k2)
					# kをk2に張替え
					x.keys[i] = k2

				# 2c
				else:
					# マージ
					y.keys.append(x.keys.pop(i))
					y.keys += z.keys
					y.c += z.c
					y.n = 2*self.t - 1
					x.c.pop(i+1)
					x.n -= 1
					self._delete(x.c[i], k)

		elif not x.leaf:
			i = 0
			while i < x.n and k > x.keys[i]:
				i += 1
			if x.c[i].n == self.t-1:
				if 0 < i: y = x.c[i-1]
				if i < x.n: z = x.c[i+1]

				# 3a 左右どちらかの子のキーがt個以上なら移送
				if 0 < i and y.n >= self.t:
					# 2018-05-31
					x.c[i].keys.insert(0, x.keys.pop(i-1))
					x.keys.insert(i-1, y.keys.pop(-1))
					if not y.leaf: x.c[i].c.insert(0, y.c.pop(-1))
					y.n -= 1
					x.c[i].n += 1

				elif i < x.n and z.n >= self.t:
					# 2018-05-31
					x.c[i].keys.append(x.keys.pop(i))
					x.keys.insert(i, z.keys.pop(0))
					if not z.leaf: x.c[i].c.append(z.c.pop(0))
					z.n -= 1
					x.c[i].n += 1
				
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
			self._delete(x.c[i], k)


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
    data = [random.randint(0, 100) for x in range(10**2)]
    print(data)

    # create B-Tree
    tree = B_Tree(t=5)

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
	    tree.delete(k)
	    print('\n{}'.format(tree.root))


"""
$ python test_b_tree2.py 
[84, 86, 68, 68, 60, 29, 48, 8, 5, 45]

insert 84

<Node: (n, keys, leaf) = (1, [84], True)>

insert 86

<Node: (n, keys, leaf) = (2, [84, 86], True)>

insert 68

<Node: (n, keys, leaf) = (3, [68, 84, 86], True)>

insert 68

<Node: (n, keys, leaf) = (1, [84], False)>
<Node: (n, keys, leaf) = (2, [68, 68], True)>
<Node: (n, keys, leaf) = (1, [86], True)>

insert 60

<Node: (n, keys, leaf) = (1, [84], False)>
<Node: (n, keys, leaf) = (3, [60, 68, 68], True)>
<Node: (n, keys, leaf) = (1, [86], True)>

insert 29

<Node: (n, keys, leaf) = (2, [68, 84], False)>
<Node: (n, keys, leaf) = (2, [29, 60], True)>
<Node: (n, keys, leaf) = (1, [68], True)>
<Node: (n, keys, leaf) = (1, [86], True)>

insert 48

<Node: (n, keys, leaf) = (2, [68, 84], False)>
<Node: (n, keys, leaf) = (3, [29, 48, 60], True)>
<Node: (n, keys, leaf) = (1, [68], True)>
<Node: (n, keys, leaf) = (1, [86], True)>

insert 8

<Node: (n, keys, leaf) = (3, [48, 68, 84], False)>
<Node: (n, keys, leaf) = (2, [8, 29], True)>
<Node: (n, keys, leaf) = (1, [60], True)>
<Node: (n, keys, leaf) = (1, [68], True)>
<Node: (n, keys, leaf) = (1, [86], True)>

insert 5

<Node: (n, keys, leaf) = (1, [68], False)>
<Node: (n, keys, leaf) = (1, [48], False)>
<Node: (n, keys, leaf) = (3, [5, 8, 29], True)>
<Node: (n, keys, leaf) = (1, [60], True)>
<Node: (n, keys, leaf) = (1, [84], False)>
<Node: (n, keys, leaf) = (1, [68], True)>
<Node: (n, keys, leaf) = (1, [86], True)>

insert 45

<Node: (n, keys, leaf) = (1, [68], False)>
<Node: (n, keys, leaf) = (2, [8, 48], False)>
<Node: (n, keys, leaf) = (1, [5], True)>
<Node: (n, keys, leaf) = (2, [29, 45], True)>
<Node: (n, keys, leaf) = (1, [60], True)>
<Node: (n, keys, leaf) = (1, [84], False)>
<Node: (n, keys, leaf) = (1, [68], True)>
<Node: (n, keys, leaf) = (1, [86], True)>

search: 84
(<Node: (n, keys, leaf) = (1, [84], False)>
<Node: (n, keys, leaf) = (1, [68], True)>
<Node: (n, keys, leaf) = (1, [86], True)>, 0)
5
8
29
45
48
60
68
68
84
86

delete: 84

<Node: (n, keys, leaf) = (1, [48], False)>
<Node: (n, keys, leaf) = (1, [8], False)>
<Node: (n, keys, leaf) = (1, [5], True)>
<Node: (n, keys, leaf) = (2, [29, 45], True)>
<Node: (n, keys, leaf) = (1, [68], False)>
<Node: (n, keys, leaf) = (1, [60], True)>
<Node: (n, keys, leaf) = (2, [68, 86], True)>

delete: 86

<Node: (n, keys, leaf) = (3, [8, 48, 68], False)>
<Node: (n, keys, leaf) = (1, [5], True)>
<Node: (n, keys, leaf) = (2, [29, 45], True)>
<Node: (n, keys, leaf) = (1, [60], True)>
<Node: (n, keys, leaf) = (1, [68], True)>

delete: 68

<Node: (n, keys, leaf) = (2, [8, 48], False)>
<Node: (n, keys, leaf) = (1, [5], True)>
<Node: (n, keys, leaf) = (2, [29, 45], True)>
<Node: (n, keys, leaf) = (2, [60, 68], True)>

delete: 68

<Node: (n, keys, leaf) = (2, [8, 48], False)>
<Node: (n, keys, leaf) = (1, [5], True)>
<Node: (n, keys, leaf) = (2, [29, 45], True)>
<Node: (n, keys, leaf) = (1, [60], True)>

delete: 60

<Node: (n, keys, leaf) = (2, [8, 45], False)>
<Node: (n, keys, leaf) = (1, [5], True)>
<Node: (n, keys, leaf) = (1, [29], True)>
<Node: (n, keys, leaf) = (1, [48], True)>

delete: 29

<Node: (n, keys, leaf) = (1, [8], False)>
<Node: (n, keys, leaf) = (1, [5], True)>
<Node: (n, keys, leaf) = (2, [45, 48], True)>

delete: 48

<Node: (n, keys, leaf) = (1, [8], False)>
<Node: (n, keys, leaf) = (1, [5], True)>
<Node: (n, keys, leaf) = (1, [45], True)>

delete: 8

<Node: (n, keys, leaf) = (2, [5, 45], True)>

delete: 5

<Node: (n, keys, leaf) = (1, [45], True)>

delete: 45

<Node: (n, keys, leaf) = (0, [], True)>
"""