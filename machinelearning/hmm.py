
"""
	手元の Windows 10 pro + Anaconda3 環境では以下コマンドで hmmlearn をインストール
	pip install hmmlearn はインストール途中でエラーを吐く
	conda install -c omnia hmmlearn

	fit()を使うと途中でwarningメッセージを吐く
"""
# ------------------
# モジュールインポート
# ------------------
import numpy as np
from hmmlearn import hmm
import warnings
from sklearn.utils import check_random_state
warnings.filterwarnings('ignore', category=DeprecationWarning)


# ------------------
# 定数パラメータ設定
# ------------------
# 隠れ状態の数指定
n_components = 5

# 初期状態の指定
startprob = np.array([0.0, 0.1, 0.8, 0.1, 0.0])

# 推移確率の指定
transmat = np.array([[0.9, 0.1, 0.0, 0.0, 0.0],
                     [0.4, 0.3, 0.3, 0.0, 0.0],
                     [0.1, 0.2, 0.4, 0.3, 0.0],
                     [0.0, 0.1, 0.3, 0.3, 0.3],
                     [0.0, 0.0, 0.3, 0.1, 0.6]])

# 正規分布を仮定して平均と共分散行列指定
means = np.array([[1.0, 1.0],
                  [2.0, 2.0],
                  [3.0, 3.0],
                  [4.0, 4.0],
                  [5.0, 5.0]])

covars = .1 * np.tile(np.identity(2), (5, 1, 1))


# ------------------
# 関数の定義
# ------------------
def next_obs(model, z):
	"""学習済みモデルmodelを用いて前時刻の状態zから(次の状態と次の観測値)を返す"""
	transmat_cdf = np.cumsum(model.transmat_, axis=1)
	random_state = check_random_state(model.random_state)
	next_state = (transmat_cdf[z] > random_state.rand()).argmax()
	next_obs = model._generate_sample_from_state(next_state, random_state)
	print("model.transmat_", model.transmat_)
	print("transmat_cdf", transmat_cdf)
	print("random_state", random_state)
	return (next_state, next_obs)

# ------------------
# メイン処理
# ------------------
def main():
	model = hmm.GaussianHMM(n_components=n_components, covariance_type="full")
	model.startprob_ = startprob
	model.transmat_ = transmat
	model.means_ = means
	model.covars_ = covars

	# 観測値の系列Xと状態の系列Zを生成
	X, Z = model.sample(10)
	print("X\n", X)
	print("Z\n", Z)

	# 評価：パラメータ既知のモデルからXが得られる確率
	prob = np.exp(model.score(X))
	print("evaluation: {}".format(prob))

	# 復号：パラメータ既知のモデルからXを得る隠れ変数列Z
	state = model.predict(X)
	print("decode: {}".format(state))

	# 推定：Xからのモデルパラメータ推定
	X, Z = model.sample(1000)
	remodel = hmm.GaussianHMM(n_components=n_components, covariance_type="full", n_iter=100)
	print("fit")
	remodel.fit(X)
	print("transmat: {}".format(remodel.transmat_))
	print("means: {}".format(remodel.means_))

	# t+1の予測
	next_z, next_x = next_obs(model, state[-1])
	print("next_x: {}".format(next_x))


if __name__ == '__main__':
    main()