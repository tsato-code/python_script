# ------------------
# モジュールインポート
# ------------------
import numpy as np
import matplotlib.pyplot as plt
 

# ------------------
# 定数パラメータ設定
# ------------------
N = 100
OUT_FILE = "../out/contour.png"

# ------------------
#  メイン処理
# ------------------
def main():
	# 乱数生成
	x = np.random.randn(100, 2)
	x[:,1] = 0.4*x[:,0]+x[:,1]

	# 平均と共分散行列の逆行列
	mu = np.mean(x, axis=0)
	s2 = np.cov(x.T)
	s2_inv = np.linalg.inv(s2)

	# メッシュグリッド生成
	x_axis = np.linspace(-3, 3, N)
	y_axis = np.linspace(-3, 3, N)
	X, Y = np.meshgrid(x_axis, y_axis)
	Z = s2_inv[0, 0]*X**2+s2_inv[0,1]*X*Y+s2_inv[1, 1]*Y**2
	
	# プロット 
	plt.xlim(-3, 3)
	plt.ylim(-3, 3)
	plt.contour(X, Y, Z, levels=[0.5*x for x in range(100)])
	plt.scatter(x[:,0], x[:,1], color='r')
	plt.gca().set_aspect('equal')
	plt.savefig(OUT_FILE, transparent=False, bbox_inches='tight', pad_inches=0)


if __name__ == '__main__':
	main()