import numpy as np
import pandas as pd
import time
from numba import jit


df = pd.DataFrame((np.random.random(size=(100000000, 2))), columns=list('ab'))


def add(a, b):
	a_val = a.values
	b_val = b.values

	c = np.zeros(len(a_val))
	for i in range(len(a_val)):
		c[i] = a_val[i] + b_val[i]
	return c


@jit
def add_jit(a, b):
	a_val = a.values
	b_val = b.values

	c = np.zeros(len(a_val))
	for i in range(len(a_val)):
		c[i] = a_val[i] + b_val[i]
	return c


# ndarray + for
start = time.time()
[x+y for x, y in zip(df.a.values, df.b.values)]
elapsed = time.time() - start
print('{} [sec]'.format(elapsed))


# add
start = time.time()
c = add(df.a, df.b)
elapsed = time.time() - start
print('{} [sec]'.format(elapsed))


# add + jit
start = time.time()
c = add_jit(df.a, df.b)
elapsed = time.time() - start
print('{} [sec]'.format(elapsed))


"""
$ python compare_pandas_loop03.py
19.078372478485107 [sec]
28.92742919921875 [sec]
7.193841218948364 [sec]
"""
