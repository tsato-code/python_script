import numpy as np
import pandas as pd
import time
from numba import jit


df = pd.DataFrame((np.random.random(size=(100000000, 2))), columns=list('ab'))

def calc(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        elapsed = time.time() - start
        print('process time: {}[sec]'.format(elapsed))
    return wrapper


@calc
@jit
def add_jit(a, b):
	a_val = a.values
	b_val = b.values

	c = np.zeros(len(a_val))
	for i in range(len(a_val)):
		c[i] = a_val[i] + b_val[i]
	return c


c = add_jit(df.a, df.b)


"""
$ python test_numba_jit.py
process time: 6.7328290939331055[sec]
"""