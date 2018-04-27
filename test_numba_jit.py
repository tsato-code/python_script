import numpy as np
import pandas as pd
import time
from numba import jit


df = pd.DataFrame((np.random.random(size=(100000000, 2))), columns=list('ab'))


@jit
def add_jit(a, b):
	a_val = a.values
	b_val = b.values

	c = np.zeros(len(a_val))
	for i in range(len(a_val)):
		c[i] = a_val[i] + b_val[i]
	return c


# add + jit
start = time.time()
c = add_jit(df.a, df.b)
elapsed = time.time() - start
print('{} [sec]'.format(elapsed))


"""
$ python test_numba_jit.py
7.037831544876099 [sec]
"""