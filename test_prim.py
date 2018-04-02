import heapq

def prim(edges, r=0):
	nodes = set([n for e in edges for n in e])
	visited = [False for n in nodes]
	total_weight = 0
	tree, p_queue = [], []
	r = 0
	visited[r] = True
	heapq.heappush(p_queue, (0, r, -1))

	while p_queue != []:
		e = heapq.heappop(p_queue)
		if visited[e[1]] + visited[e[2]] != 1: continue
		tree.append(e[1:])
		total_weight += e[0]
		visited[e[1]], visited[e[2]] = True, True
		for e in edges:
			try:
				if visited[e[1]] + visited[e[2]] == 1:
					heapq.heappush(p_queue, e)
			except:
				print(e)
				print(visited)
				import sys
				sys.exit(0)

	print('mst: {}'.format(tree))
	print('mst size: {}'.format(len(tree)))
	print('mst weight: {}'.format(total_weight))


edges = [
	(0,2,1),
	(0,1,4),
	(0,5,3),
	(1,3,2),
	(1,4,7),
	(4,3,5),
	(3,5,2),
	(2,5,5)]

edges = [(e[2], e[0], e[1]) for e in edges]
r = edges[0][1]

print(edges)
print('root: {}'.format(r))
prim(edges, r)


"""
$ python test_prim.py
[(1, 0, 2), (4, 0, 1), (3, 0, 5), (2, 1, 3), (7, 1, 4), (5, 4, 3), (2, 3, 5), (5, 2, 5)]
root: 0
mst: [(0, -1), (0, 2), (0, 5), (3, 5), (1, 3), (4, 3)]
mst size: 6
mst weight: 13
"""