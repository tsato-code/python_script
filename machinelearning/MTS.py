# ------------------
# モジュールインポート
# ------------------
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


# ------------------
# 定数パラメータ設定
# ------------------
IN_FILE = "../data/iris.csv"
OUT_DIR = "../out"


# ------------------
# 関数等の定義
# ------------------
class MTS():
	""" MT法のためのクラス """
	def __init__(self):
		""" コンストラクタの定義 """
		self.sc = StandardScaler()

	def fit(self, X_train):
		""" 学習 """
		X_std = self.sc.fit_transform(X_train)
		X_std_corr = np.corrcoef(X_std, rowvar=False)
		# サイズが2以上で逆行列を計算、そうでなければ1
		if X_std_corr.shape!=():
			self.X_std_corr_inv = np.linalg.inv(X_std_corr)
		else:
			self.X_std_corr_inv = 1 

	def predict(self, X_test):
		""" 予測 """
		X_test_std = self.sc.transform(X_test)
		anomaly_score = np.array([np.dot(x, np.dot(self.X_std_corr_inv, x)) for x in X_test_std])
		anomaly_score /= X_test.shape[1]
		return anomaly_score

	def break_even_point(self, a, y_test):
		""" 分岐点精度の計算 """
		# 正常標本精度と異常標本精度の計算
		y_test.reset_index(drop=True, inplace=True) # インデックスリセット
		idx = a.argsort()[::-1] # 降順のインデックス計算
		n_total = len(y_test)
		n_anom = sum(y_test)
		n_norm = n_total - n_anom
		coverage = np.zeros(n_total) # 異常標本精度
		detection = np.zeros(n_total) # 正常標本精度
		for i in range(n_total):
			n_detected_anom = sum(y_test[idx][:i])
			n_detected_norm = n_total - i - sum(y_test[idx][i:])
			coverage[i] = n_detected_anom / n_anom
			detection[i] = n_detected_norm / n_norm
		
		# 分岐点精度の計算
		thresh = 0
		for i, (c_score, d_score) in enumerate(zip(coverage, detection)):
			if c_score >= d_score:
				thresh = i
				break
		break_even_point = a[idx][thresh]
		print(break_even_point, c_score, d_score)
		return (break_even_point, c_score), (coverage, detection)


def initialize():
	""" ディレクトリ初期化 """
	is_dir()


def is_dir(out_dir=OUT_DIR):
	""" ディレクトリの作成 """
	if not os.path.exists(out_dir):
		os.makedirs(out_dir)


def make_figure_anomaly_score(anomaly_score, y_test, out_dir="../out"):
	""" 異常度の画像保存 """
	plt.figure()
	plt.rcParams.update({'font.size': 14})
	plt.xlabel('sample index')
	plt.ylabel('anomaly score')
	plt.plot(np.where(y_test==0)[0], anomaly_score[np.where(y_test==0)[0]], 'o', alpha=.5, ms=2.5)
	plt.plot(np.where(y_test!=0)[0], anomaly_score[np.where(y_test!=0)[0]], 'o', alpha=.5, ms=2.5,
		color='r')
	file_name, ext = os.path.splitext(IN_FILE)
	file_name = os.path.basename(file_name)
	file_name = "{}_anomaly.png".format(file_name)
	out_path = os.path.join(out_dir, file_name)
	plt.savefig(out_path, transparent=False, bbox_inches='tight', pad_inches=0)
	# plt.show()
	print("save for {}".format(out_path))


def make_figure_break_even_point(break_even_point, score, coverage, detection, out_dir="../out"):
	""" 分岐点の画像保存 """
	plt.figure()
	plt.rcParams.update({'font.size': 14})
	plt.xlabel('threshold')
	plt.xscale('log')
	plt.grid(which='major')
	plt.grid(which='minor')
	plt.plot(range(len(coverage)), coverage, label='coverage')
	plt.plot(range(len(detection)), detection, label='detection ratio', color='r')
	plt.legend()
	file_name, ext = os.path.splitext(IN_FILE)
	file_name = os.path.basename(file_name)
	file_name = "{}_bep{:.2f}_score{:.4f}.png".format(file_name, break_even_point, score)
	out_path = os.path.join(out_dir, file_name)
	plt.savefig(out_path, transparent=False, bbox_inches='tight', pad_inches=0)
	# plt.show()
	print("save for {}".format(out_path))


# ------------------
#  メイン処理
# ------------------
def main():
	initialize()
	df = pd.read_csv(IN_FILE, header=0, index_col=None, sep=',')
	df = df.sample(frac=1, random_state=0) # 行シャッフル
	df = df.reset_index(drop=True) # インデックスの更新

	# データセットの作成
	target = 'Iris-virginica'
	target_col = 'class'
	X = df.drop(target_col, axis=1)
	y = (df[target_col]==target).astype(np.int32)
	X_train, X_test, y_train, y_test = train_test_split(
		X, y, test_size=0.33, random_state=47)

	# 学習データから異常データを除去
	X_train = X_train[y_train!=1]

	# MT法による異常度計算
	mts = MTS()
	mts.fit(X_train)
	a = mts.predict(X_test)
	(break_even_point, score), (coverage, detection) = mts.break_even_point(a, y_test)

	# 画像保存
	make_figure_anomaly_score(a, y_test, OUT_DIR)
	make_figure_break_even_point(break_even_point, score, coverage, detection)


if __name__ == '__main__':
	main()