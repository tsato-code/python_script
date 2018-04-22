import pandas as pd
import numpy as np
import time
from tqdm import tqdm


def dist(x0, y0):
    return pd.Series([True if np.linalg.norm([x0-x, y0-y])<0.1 else False for x, y in zip(dfB.x.values, dfB.y.values)])


dfA = pd.DataFrame([[np.random.rand(), np.random.rand()] for _ in range(10)], columns=list('xy'))
dfB = pd.DataFrame([[np.random.rand(), np.random.rand()] for _ in range(100000)], columns=list('xy'))


start = time.time()
dfC = pd.DataFrame([dist(x0, y0) for x0, y0 in zip(dfA.x.values, tqdm(dfA.y.values, leave=False))])
elapsed = time.time() - start


print('\n{} [sec]'.format(elapsed))
print(dfC.head())


"""
$ python calc_pandas_dist.py
 90%|████████████████████████████████████████████████████████████████████████████▌        | 9/10 [00:04<00:00,  2.00it/s]
6.008254289627075 [sec]
"""