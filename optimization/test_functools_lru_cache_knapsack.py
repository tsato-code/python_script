from functools import lru_cache
import numpy  as np


@lru_cache(maxsize=None)
def knapsack_dp(upper_w):
	N = len(value)

	# DP テーブル
	T = np.zeros((1+N, 1+upper_w))

	# 初期化
	for w in range(1+upper_w): T[0, w] = w

	for i in range(N):
		for w in range(1+upper_w):
			if weight[i] <= w:
				T[i+1, w] = max(T[i, w-weight[i]]+value[i], T[i, w])
			else:
				T[i+1, w] = T[i, w]
	return T[-1, -1]


if __name__ == '__main__':
	np.random.seed(10)
	value  = np.random.randint(1, 100, 10**5)
	weight = np.random.randint(1, 5, 10**5)

	import time
	start = time.time()
	opt_val = knapsack_dp(100)
	elapsed  =time.time() - start
	print(opt_val)
	print('{:.4f}[sec]'.format(elapsed))


"""
$ python test_functools_lru_cache_knapsack.py
9757.0
0.9110[sec]
"""