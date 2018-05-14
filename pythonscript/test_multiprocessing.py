from multiprocessing import Pool
from multiprocessing import Process

# 並列処理部分を関数化
# 引数は配列
def func(x=[0, 1, 2]):
    x += [3, 4, 5]
    return x


p = Pool(2)		# コア数指定、-1で全コア
args = [[i, i+1, i+2] for i in range(3)]
res = p.map(func, args)
print(res)

"""
$ python test_multiprocessing.py
[[0, 1, 2, 3, 4, 5], [1, 2, 3, 3, 4, 5], [2, 3, 4, 3, 4, 5]]
"""