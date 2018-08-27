# ------------------
# ディレクトリ構造
# ------------------
"""
┣ machinelearning/sklearn_gmm.py
┣ data/
┃ ┗ iris.csv
┗ out/
"""


# ------------------
# モジュールインポート
# ------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import train_test_split

# ------------------
# 定数パラメータ設定
# ------------------
IN_FILE = '../data/iris.csv'
OUT_FILE = '../out/plot_gmm_X_rand_pred.png'
N_COMPONETS = 4


# ------------------
# 関数の定義
# ------------------
def make_figure(X, y, out_file):
	plt.figure()
	for i in range(N_COMPONETS):
		Xi, yi = X[y==i], y[y==i]
		plt.plot(Xi[:, 0], Xi[:, 1], 'o')
	plt.savefig(out_file, transparent=False, bbox_inches='tight', pad_inches=0)


# ------------------
#  メイン処理
# ------------------
def main():
	# ファイル読み込み
	df = pd.read_csv(IN_FILE, header=0, index_col=None, sep=',')

	# 前処理
	df = df.sample(frac=1) # シャッフル
	X = df.drop('class', axis=1) # クラスラベル除去
	y = df['class'] # クラスラベル
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0) # データセット分割

	# 学習
	gmm = GaussianMixture(n_components=N_COMPONETS, verbose=0, max_iter=1000, random_state=0) # モデル生成
	print(gmm.get_params()) # パラメータ群書き込み
	gmm.fit(X_train) # 学習

	# 予測
	X_test_pred = gmm.predict(X_test) # 分類クラスの予測
	print(X_test_pred)

	X_test_pred_proba = gmm.predict_proba(X_test) # 各サンプルの所属確率
	print(X_test_pred_proba)

	# 混合正規分布からランダム生成
	X_rand, y_rand = gmm.sample(50) # 混合正規分布からランダムに10個のサンプルを生成

	# 画像保存
	make_figure(X_rand, y_rand, OUT_FILE)


if __name__ == '__main__':
	main()