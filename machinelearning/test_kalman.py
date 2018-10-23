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
x = 0.0
transition_mat = np.array([[1, 1], [0, 1]])
transition_cov = 0.001*np.eye(2)


# ------------------
# 関数の定義
# ------------------
def output(kf):	
	# 出力
	print("kf.initial_state_mean: {}".format(kf.initial_state_mean))
	print("kf.initial_state_covariance: {}".format(kf.initial_state_covariance))
	print("kf.transition_matrices: {}".format(kf.transition_matrices))
	print("transition_offsets: {}".format(kf.transition_offsets))
	print("transition_covariance: {}".format(kf.transition_covariance))
	print("observation_matrices: {}".format(kf.observation_matrices))
	print("observation_offsets: {}".format(kf.observation_offsets))
	print("observation_covariance: {}".format(kf.observation_covariance))
	print("==")


# ------------------
# メイン処理
# ------------------
def main():
	kf = KalmanFilter(transition_matrices=[[1, 1], [0, 1]], observation_matrices=[[0.1, 0.5], [-0.3, 0.0]])
	
	measurements = np.asarray([[1,1], [1,0], [1,0], [0.5, 0.5]])  # 3 observations
	filtered_state_means = [[-1, -1]]
	filtered_state_covariances = [[[1,1],[1,1]]]

	# 観測値列の各時刻の状態を推定
	# (smoothed_state_means, smoothed_state_covariances) = kf.smooth(measurements)


	for t in range(1, len(measurements)):
		# (smoothed_state_means, smoothed_state_covariances) = kf.smooth(measurements[:t])
		(filtered_state_mean, filtered_state_covariance) = \
			kf.filter_update(filtered_state_means[t-1], filtered_state_covariances[t-1], measurements[t])
		filtered_state_means.append(filtered_state_mean)
		filtered_state_covariances.append(filtered_state_covariance)
		
		# 出力
		# print("filtered_state_means: {}".format(filtered_state_means))
		output(kf)

	# print("measurements: {}".format(measurements))
	# print("filtered_state_means: {}".format(filtered_state_means))
	# print("filtered_state_covariances: {}".format(filtered_state_covariances))

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