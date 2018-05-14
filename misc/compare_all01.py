# ======================== #
# all() の挙動確認
# ======================== #
import time


arr = [True]*1000000000


# 評価
start = time.time()
print(all(arr))
elapsed = time.time() - start
print("{} [sec]".format(elapsed))


# リストの先頭をFalseにして評価
arr[0] = False
start = time.time()
print(all(arr))
elapsed = time.time() - start
print("{} [sec]".format(elapsed))


# リストの末尾だけをFalseにして評価
arr[0] = True
arr[-1] = False
start = time.time()
print(all(arr))
elapsed = time.time() - start
print("{} [sec]".format(elapsed))


"""
$ python compare_all01.py
True
4.427915096282959 [sec]
False
0.0 [sec]
False
4.21938157081604 [sec]
"""