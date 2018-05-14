# ====================================== #
# 再帰の深さを確認
# ====================================== #
import sys
print("recursion limit: {}".format(sys.getrecursionlimit()))
sys.setrecursionlimit(11)

f = lambda x: 1 if x==1 else f(x-1)
print(f(9))
print(f(10))


"""
$ python test_recursion.py
recursion limit: 1000
1
RecursionError: maximum recursion depth exceeded in comparison
"""