"""
木が高いときにキーが空になるときがある
2c マージ操作がよくない？
=> 中間ノードが空になったときの処理がない
=> そんなことはなく、中間ノードは空にならないように設計されているはず
=> マージがおかしい
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
					"""
					if x.n == 0:
						print('2c')
						print('x.keys: {}, x.c: {}'.format(x.keys, x.c))
						print('y.keys: {}, y.c: {}'.format(y.keys, y.c))
						x = y    # 2018-05-30
					"""

		elif not x.leaf:
			i = 0
			while i < x.n and k > x.keys[i]:
				i += 1
			if x.c[i].n == self.t-1:
				if 0 < i: y = x.c[i-1]
				if i < x.n: z = x.c[i+1]

				# 3a 左右どちらかの子のキーがt個以上なら移送
				if 0 < i and y.n >= self.t:
					k1 = self._max_key(y)
					self._delete(y, k1)
					k0 = x.keys[i-1]
					self._insert(x.c[i], k0)
					x.keys[i-1] = k1

				elif i < x.n and z.n >= self.t:
					k2 = self._min_key(z)
					self._delete(z, k2)
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
					"""
					if x.n == 0:
						print('3b right marge')
						print('root', self.root.__repr__())
						print('x', x)
						x = x.c[i] 	# 2018-05-30
						print('root', self.root.__repr__())
						print('x', x)
						target = x
					"""

				elif 0 < i and y.n == self.t-1:
					# yとマージ
					y.keys.append(x.keys.pop(i-1))
					y.keys += x.c[i].keys
					y.c += x.c[i].c
					y.n = 2*self.t - 1
					x.c.pop(i)
					x.n -= 1
					i -= 1
					"""
					if x.n == 0:
						print('3b left marge')
						x = y 	# 2018-05-30
						target = x
					"""
			self._delete(x.c[i], k)
		"""
		if x.c != []:
			for y in x.c:
				if y.n == 0 and y.c != []:
					y = y.c[0]
		"""
		


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
    data = [random.randint(0, 3) for x in range(5)]
    data = [2, 2, 1, 3, 1, 1, 0, 2, 0, 2, 0, 3, 3, 0, 1, 1, 0, 2, 2, 1, 1, 1, 1, 1, 3, 0, 2, 0, 2, 0]
    # data = [1, 2, 1, 2, 2]
    print(data)

    # create B-Tree
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
	    tree.delete(k)
	    print('\n{}'.format(tree.root))