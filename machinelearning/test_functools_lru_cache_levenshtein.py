from functools import lru_cache
import numpy  as np


@lru_cache(maxsize=None)
def levenshtein(s, t):
	size_s = 1 + len(s)
	size_t = 1 + len(t)

	# DP テーブル
	dist = np.zeros((size_s, size_t))

	# 初期化
	dist[:, 0] = range(size_s)
	dist[0, :] = range(size_t)

	for i in range(1, size_s):
		for j in range(1, size_t):
			c = 0 if s[i-1] == t[j-1] else 1
			dist[i, j] = min(dist[i-1, j]+1, dist[i, j-1]+1, dist[i-1, j-1]+c)
	return dist[-1, -1]


if __name__ == '__main__':
	s = 'moment'
	t = 'momentum'
	d = levenshtein(s, t)
	print(d)


"""
$ python test_functools_lru_cache_levenshtein.py
2.0
"""