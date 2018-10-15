"""
pykalmanのインストール
pip install pykalman
"""
# ------------------
# モジュールインポート
# ------------------
import numpy as np
from matplotlib import pylab as plt
from pykalman import KalmanFilter


# ------------------
# 定数パラメータ設定
# ------------------
x = -0.37727
transition_mat = np.array([[1, 1], [0, 1]])
transition_cov = 0.0000001*np.eye(2)
# ------------------
# 関数の定義
# ------------------


# ------------------
# メイン処理
# ------------------
def main():
	# 正規分布から適当なサイズの乱数列を生成
	observations = np.random.normal(x, 1, size=50)

	# 適当な推移行列からカルマンフィルタモデル作成
	# kf = KalmanFilter(transition_matrices=transition_mat,
	#                   transition_covariance=transition_cov)
	kf = KalmanFilter()

	# 推定
	kf.em(observations,n_iter=20)
	(filtered_state_means, filtered_state_covariances) = kf.filter(observations)
	(smoothed_state_means, smoothed_state_covariances) = kf.smooth(observations)

	# 可視化
	plt.figure(figsize=(6,4))
	plt.plot(observations, "-xc", label="observations")
	plt.plot(smoothed_state_means[:, 0], "b", label="smoothed")
	plt.plot(filtered_state_means[:, 0], "r", label="filtered")
	plt.axhline(x, color="k", label="truth value")
	plt.legend()
	plt.show()
	plt.close()



if __name__=="__main__":
	main()