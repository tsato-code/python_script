"""
pykalmanのインストール
pip install pykalman
以下のページから観測系列に未観測値を含む場合の図が書ける
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
x = 0.0
transition_mat = np.array([[1, 1], [0, 1]])
transition_cov = 0.001*np.eye(2)


# ------------------
# 関数の定義
# ------------------
def output(kf):	
	# 出力
	# print("kf.initial_state_mean: {}".format(kf.initial_state_mean))
	# print("kf.initial_state_covariance: {}".format(kf.initial_state_covariance))
	# print("kf.transition_matrices: {}".format(kf.transition_matrices))
	# print("transition_offsets: {}".format(kf.transition_offsets))
	# print("transition_covariance: {}".format(kf.transition_covariance))
	print("observation_matrices: {}".format(kf.observation_matrices))
	print("observation_offsets: {}".format(kf.observation_offsets))
	print("observation_covariance: {}".format(kf.observation_covariance))

# ------------------
# メイン処理
# ------------------
def main():
	# 正規分布から適当なサイズの乱数列を生成
	observations = np.random.normal(x, 1, size=50)

	# 適当な推移行列からカルマンフィルタモデル作成
	kf = KalmanFilter(transition_matrices=transition_mat,
	                  transition_covariance=transition_cov)
	# kf = KalmanFilter()

	# 推定
	kf.em(observations, n_iter=5)
	(filtered_state_means, filtered_state_covariances) = kf.filter(observations)
	(smoothed_state_means, smoothed_state_covariances) = kf.smooth(observations)

	# 出力
	output(kf)

	# 更新
	for obs in observations:
		(filtered_state_means, filtered_state_covariances) = kf.filter_update(
			filtered_state_mean=filtered_state_means[-1], filtered_state_covariance=filtered_state_covariances[-1], observation=obs
		)
		output(kf)

	print(observations)
	print(filtered_state_means)
	print(filtered_state_covariances)

	"""
	# 可視化
	plt.figure(figsize=(6,4))
	plt.plot(observations, "-xc", label="observations")
	plt.plot(smoothed_state_means[:, 0], "b", label="smoothed")
	plt.plot(filtered_state_means[:, 0], "r", label="filtered")
	plt.axhline(x, color="k", label="truth value")
	plt.legend()
	plt.show()
	plt.close()
	"""






if __name__=="__main__":
	main()