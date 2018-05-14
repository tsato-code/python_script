# ======================================================= #
# all() の処理速度確認 => できるだけ関数は使わないほうがよいという結論
# ======================================================= #
import random
import time


size = 10000000
eps = 0.0001
arr_list = [[random.random(), random.random(), random.random()] for _ in range(size)]


# 関数定義
check = lambda x: x<eps


# 評価方法1
start = time.time()
[arr[0]<eps and arr[0]<eps and arr[0]<eps for arr in arr_list]
elapsed = time.time() - start
print("{} [sec]".format(elapsed))


# 評価方法2
start = time.time()
[check(arr[0]) and check(arr[1]) and check(arr[2])  for arr in arr_list]
elapsed = time.time() - start
print("{} [sec]".format(elapsed))


# 評価方法3
start = time.time()
[all([i<eps for i in arr]) for arr in arr_list]
elapsed = time.time() - start
print("{} [sec]".format(elapsed))


# 評価方法4
start = time.time()
[all([check(arr[0]), check(arr[1]), check(arr[2])])  for arr in arr_list]
elapsed = time.time() - start
print("{} [sec]".format(elapsed))


"""
$ python -u compare_all02.py
0.8280279636383057 [sec]
1.4199542999267578 [sec]
3.6455235481262207 [sec]
4.211561679840088 [sec]
"""