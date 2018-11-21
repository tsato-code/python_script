"""
pymafのインストール
pip install pymaf
"""
# ------------------
# モジュールインポート
# ------------------
from pymaf import maf
from scipy import stats
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt


# ------------------
# 定数パラメータ設定
# ------------------
START = datetime.datetime(2017, 1, 1)
END = datetime.datetime(2018, 12, 31)
N_DIM = 2


# ------------------
# 関数の定義
# ------------------

# ------------------
# メイン処理
# ------------------
def main():
	# データ読み込み
	prices = web.DataReader('SNE', 'iex', START, END)
	# 描画
	prices_norm = prices.apply(stats.zscore, axis=0)
	prices_norm.plot()
	plt.show()
	# MAF
	mafs = maf(prices)
	first_mafs = np.apply_along_axis(lambda x: (x - np.mean(x)) / np.std(x), arr=mafs[0][:,:N_DIM], axis=0)
	# 描画
	labels = ['MAF' + str(s) for s in range(1,1+N_DIM) ]
	for y_arr, label in zip(first_mafs.T, labels):
		plt.plot(y_arr, label=label)
	plt.legend()
	plt.show()


if __name__=="__main__":
	main()