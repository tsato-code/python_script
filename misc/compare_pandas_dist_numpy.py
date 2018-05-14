import pandas as pd
import numpy as np
import time
from numba import jit
from tqdm import tqdm


def norm1(x1, y1, x2, y2):
	return np.linalg.norm([x1-x2, y1-y2])


def norm2(x1, y1, x2, y2):
	return np.sqrt((x1-x2)**2+(y1-y2)**2)


def calc_norm1(df):
	a = df.a.values
	b = df.b.values
	c = df.c.values
	d = df.d.values
	rows = df.shape[0]
	e = np.zeros(rows)
	for i in range(rows):
		e[i] = norm1(a[i], b[i], c[i], d[i])


def calc_norm2(df):
	a = df.a.values
	b = df.b.values
	c = df.c.values
	d = df.d.values
	rows = df.shape[0]
	e = np.zeros(rows)
	for i in range(rows):
		e[i] = norm2(a[i], b[i], c[i], d[i])


df = pd.DataFrame([
	[np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand()]
	for _ in range(1000000)], columns=list('abcd'))


# norm1
start = time.time()
calc_norm1(df)
elapsed = time.time() - start
print('norm1: {} [sec]'.format(elapsed))


# norm2
start = time.time()
calc_norm2(df)
elapsed = time.time() - start
print('norm2: {} [sec]'.format(elapsed))


"""
$ python -u calc_pandas_dist_jit.py
norm1: 5.092094421386719 [sec]
norm2: 2.361894369125366 [sec]
"""