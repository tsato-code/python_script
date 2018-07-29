import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split

# データセット読み込み
df = pd.read_csv("../data/glass.csv")
X = df.drop('Outlier', axis=1)
y = df['Outlier']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.05, random_state=0)


# k近傍法
num_k = 3
knn = NearestNeighbors(n_neighbors=num_k)
knn.fit(X_train)

# 各点のk近傍までの距離と近傍の点集合のインデックス
dist_k, idx_k = knn.kneighbors(X_test, n_neighbors=num_k)
print('k近傍')
print(dist_k)
print(idx_k)


# 各点のeps近傍までの距離と近傍の点集合のインデックス
dist_eps, idx_eps = knn.radius_neighbors(X_test, radius=0.5)
print('\neps近傍')
print(dist_eps)
print(idx_eps)



"""
$ python test_knn.py
k近傍
[[0.23706539 0.32031235 0.49264592]
 [0.1161895  0.16309506 0.19874607]
 [0.36152455 0.39534795 0.41940434]
 [0.46097722 0.61008196 0.61424751]
 [0.36400549 1.23081274 1.45986301]
 [0.07615773 0.16583124 0.17262677]
 [0.2463737  0.43104524 0.55054518]
 [0.18574176 0.20663978 0.23958297]
 [0.13784049 0.27073973 0.27892651]
 [0.18627936 0.19183326 0.22427661]
 [0.64629715 0.66287254 0.66902915]]
[[ 28 104  90]
 [155 119  57]
 [ 92 174  31]
 [167  69 170]
 [123 130  40]
 [  3 178  31]
 [ 27  67  26]
 [ 31 190 179]
 [128 166  92]
 [190 179  34]
 [ 22 138 121]]

eps近傍
[array([0.32031235, 0.23706539, 0.49264592])
 array([0.35902646, 0.47085029, 0.38236109, 0.34322005, 0.33060551,
       0.40963398, 0.44710178, 0.28722813, 0.39458839, 0.38691084,
       0.43943145, 0.31016125, 0.32817678, 0.4611941 , 0.16309506,
       0.25455844, 0.36851052, 0.26495283, 0.19874607, 0.28896367,
       0.26720778, 0.1161895 , 0.27586228, 0.35341194, 0.47391982])
 array([0.46162756, 0.39534795, 0.47138095, 0.48155997, 0.41940434,
       0.36152455])
 array([0.46097722]) array([0.36400549])
 array([0.43669211, 0.44294469, 0.43794977, 0.4110961 , 0.38078866,
       0.32202484, 0.37376463, 0.28460499, 0.07615773, 0.29189039,
       0.38768544, 0.44598206, 0.48559242, 0.16583124, 0.37282704,
       0.17262677, 0.43794977])
 array([0.2463737 , 0.43104524])
 array([0.49020404, 0.48938737, 0.49889879, 0.33361655, 0.42673177,
       0.38353618, 0.39025633, 0.44777226, 0.47      , 0.23958297,
       0.20663978, 0.28407745, 0.24556058, 0.47180504, 0.35270384,
       0.40607881, 0.49091751, 0.42225585, 0.36796739, 0.4769696 ,
       0.18574176, 0.40902323])
 array([0.4747631 , 0.49396356, 0.39585351, 0.39166312, 0.40224371,
       0.13784049, 0.42906876, 0.27073973, 0.42023803, 0.48631266,
       0.31144823, 0.27892651])
 array([0.45989129, 0.49203658, 0.45814845, 0.47307505, 0.45880279,
       0.22427661, 0.47444705, 0.49799598, 0.44440972, 0.49558047,
       0.28548205, 0.19183326, 0.44542115, 0.18627936, 0.28965497,
       0.26776856, 0.41689327, 0.44888751, 0.4765501 , 0.36810325,
       0.32      , 0.31984371, 0.46443514, 0.36455452])
 array([], dtype=float64)]
[array([104,  28,  90])
 array([ 48,  53,  80,   5,  77, 160, 195, 156,  16,  76,  25, 164, 140,
       169, 119, 136, 180, 113,  57,  32,  51, 155,  35,  42,  26])
 array([128, 174, 108,  43,  31,  92]) array([167]) array([123])
 array([ 17,  39, 134,  34,  94, 179, 182, 190,   3, 128,   6, 166, 174,
       178,  43,  31,  92])
 array([27, 67])
 array([ 53,  62, 101, 134,  77,  34, 195, 140,  94, 179, 190,   3, 128,
         6, 166, 174, 108,  21, 178,  43,  31,  92])
 array([134, 195, 179, 190,   3, 128,   6, 166, 174, 178,  31,  92])
 array([ 39,  62, 101, 117, 134,  34, 168, 176, 195, 100,  94, 179, 182,
       190,   3, 128, 166, 172, 174,  21, 178,  31, 189, 192])
 array([], dtype=int64)]
"""