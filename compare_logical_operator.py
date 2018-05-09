# ======================================================= #
# 論理演算に & を使うのは妥当か確認 => 結論は「大差ない」
# ======================================================= #
import random
import time


logi_list = [[random.random()<0.5, random.random()<0.5] for _ in range(10**8)]


# and 演算子
start = time.time()
[logi[0] and logi[1] for logi in logi_list]
elapsed = time.time() - start
print('{} [sec]'.format(elapsed))


# & 演算子
start = time.time()
[logi[0] & logi[1] for logi in logi_list]
elapsed = time.time() - start
print('{} [sec]'.format(elapsed))


"""
python compare_logical_operator.py
7.422046661376953 [sec]
7.991998672485352 [sec]
"""