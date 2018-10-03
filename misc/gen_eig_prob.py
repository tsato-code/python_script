
"""
	一般化固有値問題 Ax=λBx の固有値と固有ベクトルを計算
	以下は対称行列 A, B を生成して計算
	対称とは限らない一般化固有値問題の関数 eig(A, B) を使うと謎の normalization がされる
	補足：Bが正則なら B_inv Ax=λx の固有値問題
"""
# ------------------
# モジュールインポート
# ------------------
import numpy as np
import scipy.linalg as la
import time


# ------------------
# 定数パラメータ設定
# ------------------
# 行列 A, B のサイズ
N_SIZE = 2


# ------------------
# メイン処理
# ------------------
def main():
	# 対称行列の生成
	A = np.random.random(size=(N_SIZE, N_SIZE))
	A = np.dot(A, A.T)
	B = np.random.random(size=(N_SIZE, N_SIZE))
	B = np.dot(B, B.T)
	# B = np.eye(N_SIZE)

	# 行列の一般化固有値問題を計算
	print("一般化固有値問題の固有値と固有ベクトルを計算")
	start = time.time()
	eig_vals, eig_vecs = la.eig(A, B)
	elapsed = time.time() - start
	print("elapsed: {:.2f} [sec]".format(elapsed))

	# 検算
	print(np.allclose(A @ eig_vecs - B @ eig_vecs @ np.diag(eig_vals), np.zeros((N_SIZE, N_SIZE))))
	print(eig_vals[:3])
	print(eig_vecs[:3, :3])
	
	# 直交行列？
	L = np.linalg.cholesky(B)
	LTx = L.T @ eig_vecs
	print(LTx.T @ LTx)


	# 対称行列の一般化固有値問題を計算
	print("一般化固有値問題のAとBが対称行列として計算")
	start = time.time()
	eig_vals, eig_vecs = la.eigh(A, B, type=1)
	elapsed = time.time() - start
	print("elapsed: {:.2f} [sec]".format(elapsed))

	# 検算
	print(np.allclose(A @ eig_vecs - B @ eig_vecs @ np.diag(eig_vals), np.zeros((N_SIZE, N_SIZE))))
	print(eig_vals[:3])
	print(eig_vecs[:3, :3])

	# 直交行列？
	# Ax=λBx, B=LL^T
	# => Linv A L^-T L^T x = λL^T x
	# 求めた固有ベクトル x から L^T x を毛計算すれば直交              
	L = np.linalg.cholesky(B)
	LTx = L.T @ eig_vecs
	print(LTx.T @ LTx)


if __name__ == '__main__':
    main()