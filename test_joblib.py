from joblib import Parallel, delayed
import random, time


def process(n):
	r = random.random()
	time.sleep(r)
	print('processed: {}'.format(n))
	return n, r


if __name__ == '__main__':
	# ジョブの生成
	jobs = [delayed(process)(i) for i in range(10)]
	# 並列計算
	res = Parallel(n_jobs=-1, verbose=10)(jobs)
	# 標準出力
	[print(r) for r in res]


"""
$ python -u test_joblib.py
processed: 6
processed: 4
processed: 1
[Parallel(n_jobs=-1)]: Done   3 out of  10 | elapsed:    0.7s remaining:    1.8s
processed: 7
processed: 9
[Parallel(n_jobs=-1)]: Done   5 out of  10 | elapsed:    0.9s remaining:    0.9s
processed: 0
processed: 8
[Parallel(n_jobs=-1)]: Done   7 out of  10 | elapsed:    1.0s remaining:    0.4s
processed: 2
processed: 5
processed: 3
[Parallel(n_jobs=-1)]: Done  10 out of  10 | elapsed:    1.3s finished
(0, 0.6443402579820687)
(1, 0.4205599779233783)
(2, 0.7740489705721338)
(3, 0.9951231987103653)
(4, 0.3011106024408826)
(5, 0.8533943893256629)
(6, 0.2305573991545844)
(7, 0.47042683609050073)
(8, 0.42951804052870857)
(9, 0.30460559517767416)
"""