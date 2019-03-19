import numpy as np
from scipy import stats
np.random.seed(42)
n1 = 40
n2 = 100
# Kolmogorov-Smirnov検定
# KS統計量とp-valueのタプルが出力される
# 帰無仮説：2つの分布に差がない
# 対立仮説：2つの分布に差がないとは言えない
# pvalue>0.05 => 有意水準5%で帰無仮説を棄却、すなわち2つの分布に差がないとは言えない
# pvalue<0.05 => 有意水準5%で帰無仮説を採択
rvs1 = stats.norm.rvs(size=n1, loc=0., scale=1)
rvs2 = stats.norm.rvs(size=n2, loc=0.5, scale=1.5)
ks12 = stats.ks_2samp(rvs1, rvs2)
print(ks12)
rvs3 = stats.norm.rvs(size=n2, loc=0.01, scale=1.0)
ks13 = stats.ks_2samp(rvs1, rvs3)
print(ks13)
rvs4 = stats.norm.rvs(size=n2, loc=0.0, scale=1.0)
ks14 = stats.ks_2samp(rvs1, rvs4)
print(ks14)
rvs5 = stats.uniform.rvs(size=n2, loc=0.0, scale=1.0)
ks15 = stats.ks_2samp(rvs1, rvs5)
print(ks15)
rvs6 = stats.chi2.rvs(df=2, size=n2, loc=0.0, scale=1.0)
ks16 = stats.ks_2samp(rvs1, rvs6)
print(ks16)
"""
> python test_kolmogorov-smirnov.py
Ks_2sampResult(statistic=0.30500000000000005, pvalue=0.007403148130520076)
Ks_2sampResult(statistic=0.21999999999999997, pvalue=0.1085964506911799)
Ks_2sampResult(statistic=0.17000000000000004, pvalue=0.3493367495797508)
Ks_2sampResult(statistic=0.6, pvalue=7.777894687437233e-10)
Ks_2sampResult(statistic=0.625, pvalue=1.2312444899727668e-10)
"""