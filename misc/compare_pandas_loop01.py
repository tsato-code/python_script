import numpy as np
import pandas as pd
import time


df = pd.DataFrame((np.random.random(size=(1000000, 1))), columns=list('a'))


print('DataFrame + iterrows')
print(type(df))
start = time.time()
[row[0]+1 for row in df.iterrows()]
elapsed = time.time() - start
print('{} [sec]\n'.format(elapsed))


print('DataFrame + apply')
print(type(df))
start = time.time()
df.apply(lambda row: row.a+1, axis=1)
elapsed = time.time() - start
print('{} [sec]\n'.format(elapsed))


print('Series + map')
print(type(df.a))
start = time.time()
df.a.map(lambda x: x+1)
elapsed = time.time() - start
print('{} [sec]\n'.format(elapsed))


print('ndarray + for')
print(type(df.a.values))
start = time.time()
[x+1 for x in df.a.values]
elapsed = time.time() - start
print('{} [sec]\n'.format(elapsed))


"""
$ python compare_pandas_loop.py
DataFrame + iterrows
<class 'pandas.core.frame.DataFrame'>
11.248955011367798 [sec]

DataFrame + apply
<class 'pandas.core.frame.DataFrame'>
11.257949113845825 [sec]

Series + map
<class 'pandas.core.series.Series'>
0.2271573543548584 [sec]

ndarray + for
<class 'numpy.ndarray'>
0.27217578887939453 [sec]

"""