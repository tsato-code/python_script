class Node(object):
    def __init__(self, t):
        self.n  = None
        self.keys = []
        self.leaf = False
        self.c = []


    def __repr__(self):
        return "<Node: (n, keys, leaf, c) = ({}, {}, {}, {})>".format(self.n, self.keys, self.leaf, self.c)


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


	def delete(self):
		pass



if __name__ == '__main__':

	# データ作成
    import random
    data = [random.randint(0, 100)-50 for x in range(10)]
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