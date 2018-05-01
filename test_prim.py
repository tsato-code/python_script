import heapq


class Prim:
	""" Prim法のクラス
	"""
	def __init__(self, edges):
		""" コンストラクタ

		Args:
			params (list(int)): 重み付き無向グラフ
		"""
		self.edges = edges


	def __repr__(self):
		""" printしたときの挙動
		
		Returns:
			出力される文字列
		"""
		return "status edges: {}".format(self.edges)

 
	def replace_element(self):
		""" heapqの実装が第一要素の第一成分によって管理されるので要素の成分を並べ替え
		"""
		self.edges = [(e[2], e[0], e[1]) for e in self.edges]


	def exec(self, r=0):
		""" Prim法の実行
		
		Args:
			r (int): アルゴリズムを実行するときの始点
		"""
		nodes = set([n for e in self.edges for n in e])
		visited = [False for n in nodes]
		self.total_weight = 0
		self.tree, p_queue = [], []
		r = 0
		visited[r] = True
		heapq.heappush(p_queue, (0, r, -1))

		while p_queue != []:
			e = heapq.heappop(p_queue)
			if visited[e[1]] + visited[e[2]] != 1: continue
			self.tree.append(e[1:])
			self.total_weight += e[0]
			visited[e[1]], visited[e[2]] = True, True
			for e in self.edges:
				try:
					if visited[e[1]] + visited[e[2]] == 1:
						heapq.heappush(p_queue, e)
				except:
					print(e)
					print(visited)
					import sys
					sys.exit(0)


	def print_mst(self):
		""" 結果を出力
		"""
		print('mst: {}'.format(self.tree))
		print('mst size: {}'.format(len(self.tree)))
		print('mst weight: {}'.format(self.total_weight))


if __name__ == '__main__':
	# edges = [(n00, n01, w0), (n10, n11, w1), ...]
	edges = [
		(0, 2, 1),
		(0, 1, 4),
		(0, 5, 3),
		(1, 3, 2),
		(1, 4, 7),
		(4, 3, 5),
		(3, 5, 2),
		(2, 5, 5)]


	# Prim法クラスの作成、実行
	p = Prim(edges)
	p.replace_element()
	print(p)
	p.exec()
	p.print_mst()


	""" docstringの確認
	print("Prim.__doc__: {}".format(Prim.__doc__))
	print("Prim.__init__.__doc__: {}".format(Prim.__init__.__doc__))
	print("Prim.__repr__: {}".format(Prim.__repr__.__doc__))
	print("Prim.replace_element.__doc__: {}".format(Prim.replace_element.__doc__))
	print("Prim.exec.__doc__: {}".format(Prim.exec.__doc__))
	print("Prim.print_mst.__doc__: {}".format(Prim.print_mst.__doc__))
	"""


"""
$ python test_prim.py
status edges: [(1, 0, 2), (4, 0, 1), (3, 0, 5), (2, 1, 3), (7, 1, 4), (5, 4, 3), (2, 3, 5), (5, 2, 5)]
mst: [(0, -1), (0, 2), (0, 5), (3, 5), (1, 3), (4, 3)]
mst size: 6
mst weight: 13

"""