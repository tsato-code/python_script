# ------------------
# モジュールインポート
# ------------------
from sklearn.feature_selection import VarianceThreshold


# ------------------
# 定数パラメータ設定
# ------------------
X = [
	[0,0,0,1],
	[0,0,1,0],
	[1,1,0,0],
	[0,0,1,1],
	[0,0,1,0],
	[0,0,1,1]
]


# ------------------
#  メイン処理
# ------------------
def main():
	""" 分散が小さい変数を削除 """
	sel = VarianceThreshold(.8 *(1-.8))
	X_sel = sel.fit_transform(X)
	print("特徴量の分散\n{}".format(sel.variances_))
	print("分散の閾値で特徴選択した結果\n{}".format(X_sel))


if __name__ == '__main__':
	main()



"""
$ python sklearn_feature_selecion.py
特徴量の分散
[0.13888889 0.13888889 0.22222222 0.25      ]
変数選択の結果
[[0 1]
 [1 0]
 [0 0]
 [1 1]
 [1 0]
 [1 1]]
"""