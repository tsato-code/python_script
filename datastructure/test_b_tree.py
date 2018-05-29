class Node(object):
    def __init__(self, t):
        self.n  = None
        self.keys = []
        self.leaf = False
        self.c = []


    def __repr__(self):
        return "<Node: (n, keys, leaf, c) = ({}, {}, {}, {})>".format(self.n, self.keys, self.leaf, self.c)
        # return "Node: (n, keys, leaf, c) =\n{}, {}, {}, {}".format(self.n, self.keys, self.leaf, '\n'.join([child.__repr__() for child in self.c]))

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


	def insert(self, x, k):
		r = x
		if r.n == 2*self.t - 1:
			s = Node(self.t)
			self.root = s
			s.leaf = False
			s.n = 0
			s.c.append(r)
			self._split_child(s, 0)
			self._insert_nonfull(s, k)
		else:
			self._insert_nonfull(r, k)


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


	def max_key(self, x):
		while not x.leaf:
			x = x.c[-1]
		return x.keys[-1]


	def min_key(self, x):
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
					k1 = self.max_key(y)
					# 再帰的にk1を削除
					self.delete(y, k1)
					# kをk1に張替え
					x.keys[i] = k1
				# 2b
				elif z.n >= self.t:
					# zから最小値を探す
					k2 = self.min_key(z)
					# 再帰的にk2を削除
					self.delete(z, k2)
					# kをk2に張替え
					x.keys[i] = k2
				# 2c
				else:
					# マージ
					y.keys += z.keys
					y.c += z.c
					y.n *= 2
					# キーと子の消去
					x.keys[i:] = x.keys[i+1:]
					x.c[i+1:] = x.c[i+2:]
					x.n -= 1
		else:
			i = 0
			while i < x.n and k > x.keys[i]:
				i += 1
			# 3a
			if x.c[i].n == self.t-1:
				y = x.c[i-1]
				if i < x.n: z = x.c[i+1]
				if y.n >= self.t:
					k1 = self.max_key(y)
					self.delete(y, k1)
					k0 = x.keys[i-1]
					self.insert(x.c[i], k0)
					x.keys[i-1] = k1

				elif i < x.n and z.n >= self.t:
					k2 = self.min_key(z)
					self.delete(z, k2)
					k0 = x.keys[i]
					self.insert(x.c[i], k0)
					x.key[i] = k2
				
			# 3b 必ず左右の子を持たなければならないか確認が必要
			elif 0 < i < x.n and y.n == self.t-1 and z.n == self.t-1:
				x.c[i].keys += z.keys
				x.c[i].c += z.c
				x.c[i].n *= 2
				x.keys[i:] = x.keys[i+1:]   # あとでpopで書き換え 
				x.c[i+1:] = x.c[i+2:]   # あとでpopで書き換え
				x.n -= 1
				"""
				elif i < x.n:
					# zとマージ
					x.c[i].keys += z.keys
					x.c[i].c += z.c
					x.c[i].n *= 2
					x.keys[i:] = x.keys[i+1:]   # あとでpopで書き換え 
					x.c[i+1:] = x.c[i+2:]   # あとでpopで書き換え
					x.n -= 1
				else:
					# yとマージ
					y.keys += x.c[i].keys
					y.c += x.c[i].c
					y.n *= 2
					x.keys[i-1:] = x.keys[i+1:]   # あとでpopで書き換え
					x.c[i-1:] = x.c[i+1:]   # あとでpopで書き換え
					x.n -= 1
					i -= 1
				"""
			self.delete(x.c[i], k)



if __name__ == '__main__':

	# データ作成
    import random
    data = [random.randint(0, 100) for x in range(10)]
    # data = [5, 15, 39, 11, 32, 55, 50, 33, 28, 4]
    print(data)

    # 2分探索木作成
    tree = B_Tree(t=2)

    # insert
    for k in data:
    	print('\ninsert {}'.format(k))
    	tree.insert(tree.root, k)
    	print('\n{}'.format(tree.root))

    # search
    print('\nsearch: {}'.format(data[0]))
    res = tree.search(tree.root, data[0])
    print(res)

    # delete
    print('\ndelete: {}'.format(data[0]))
    tree.delete(tree.root, data[0])
    print('\n{}'.format(tree.root))
