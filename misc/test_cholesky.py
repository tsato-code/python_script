# ------------------
# モジュールインポート
# ------------------
import numpy as np
import scipy.linalg as la
import time

# ------------------
# 定数パラメータ設定
# ------------------
N = 10**4	# 半正定値行列 AA^T を生成するときのAの行数
M = 10**3	# 半正定値行列 AA^T を生成するときのAの列数


# ------------------
# 関数の定義
# ------------------
def solve_chol(A, b):
	""" Cholesky分解による方法 """
	L = np.linalg.cholesky(A)
	y = la.solve_triangular(L, b, lower=True)		# 前進消去
	x = la.solve_triangular(L.T, y, lower=False)	# 後退代入
	return x


def solve_inv(A, b):
	""" 逆行列による方法 """
	A_inv = np.linalg.inv(A)
	x = np.dot(A_inv, b)
	return x


# ------------------
#  メイン処理
# ------------------
def main():
	A = np.random.random(size=(N, M))
	A = np.dot(A, A.T)
	d = np.random.random(size=N)
	A += np.diag(d)
	b = np.random.random(N)

	# 逆行列による連立方程式の求解計測
	start = time.time()
	x_inv = solve_inv(A, b)
	elapsed_inv = time.time() - start

	# Cholesky分解による連立方程式の求解計測
	start = time.time()
	x_chol = solve_chol(A, b)
	elapsed_chol = time.time() - start

	# 計測結果
	print('Cholesky Time : {:.4f} [s]'.format(elapsed_chol))
	print('Inverse Time  : {:.4f} [s]'.format(elapsed_inv))

	# 解の確認
	print('x_chol: {}'.format(x_chol[:3]))
	print('x_inv : {}'.format(x_inv[:3]))


if __name__ == '__main__':
	main()


"""
$ python test_cholesky.py
Cholesky Time : 5.8474 [s]
Inverse Time  : 15.6282 [s]
x_chol: [-0.44987023 -0.07749488 -0.25726754]
x_inv : [-0.44987023 -0.07749488 -0.25726754]
"""