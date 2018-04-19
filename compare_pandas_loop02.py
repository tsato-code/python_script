import numpy as np
import pandas as pd
import time


df = pd.DataFrame((np.random.random(size=(1000000, 2))), columns=list('ab'))


print('DataFrame + iterrows')
print(type(df))
start = time.time()
[row[0]+row[1] for row in df.iterrows()]
elapsed = time.time() - start
print('{} [sec]\n'.format(elapsed))


print('DataFrame + apply')
print(type(df))
start = time.time()
df.apply(lambda row: row.a+row.b, axis=1)
elapsed = time.time() - start
print('{} [sec]\n'.format(elapsed))


print('Series + map')
print('よい実装が思いつかない\n')


print('ndarray + for')
print(type(df.a.values))
start = time.time()
[x+y for x, y in zip(df.a.values, df.b.values)]
elapsed = time.time() - start
print('{} [sec]\n'.format(elapsed))


"""
$ python compare_pandas_loop02.py
DataFrame + iterrows
<class 'pandas.core.frame.DataFrame'>
75.88811087608337 [sec]

DataFrame + apply
<class 'pandas.core.frame.DataFrame'>
17.910678386688232 [sec]

Series + map
よい実装が思いつかない

ndarray + for
<class 'numpy.ndarray'>
0.17714309692382812 [sec]

"""