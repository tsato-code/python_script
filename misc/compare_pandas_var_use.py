import pandas as pd
import numpy as np
from tqdm import tqdm
import time


def var_use(x1, y1, x2, y2):
	a = [x1, y1]
	b = [x1, y2]
	tmp = np.linalg.norm([a[0]-b[0], a[1]-b[1]])
	return tmp


def var_unuse(x1, y1, x2, y2):
	return np.linalg.norm([x1-x2, y1-y2])


df = pd.DataFrame([
	[np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand()]
	for _ in range(1000000)], columns=list('abcd'))


start = time.time()
[var_use(*abcd) for abcd in df.values]
elapsed = time.time() - start
print('var_use: {} [sec]'.format(elapsed))


start = time.time()
[var_unuse(*abcd) for abcd in df.values]
elapsed = time.time() - start
print('var_unuse {} [sec]'.format(elapsed))



"""
$ python compare_pandas_var_use.py 
var_use: 19.51082706451416 [sec]
var_unuse 17.54906415939331 [sec]
"""