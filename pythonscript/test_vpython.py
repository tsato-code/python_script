"""
3D可視化
事前にpip install vpython
"""
# ------------------
# モジュールインポート
# ------------------
from vpython import *
import numpy as np


# ------------------
# 定数パラメータ設定
# ------------------
# 点の数
N =3000
# 3次元の軸の始点
vmin = -0.1
# 3次元の軸の長さ
length = 1.4


# ------------------
#  メイン処理
# ------------------
def main():
	# 乱数生成
	np.random.seed(1)
	p = np.random.rand(N, 3)
	pi = np.sum(np.sqrt(p[:, 0]**2+p[:,1]**2+p[:,2]**2) <= 1)/N*6
	print(pi)
	# 3次元球の内側の点抽出
	inner = p[np.sqrt(p[:,0]**2+p[:,1]**2+p[:,2]**2) <= 1]
	# vpython 初期設定
	scene = canvas(width=800, height=600)
	scene.up = vector(0, 0, 1)
	scene.forward = vector(-1, -1, -1)
	scene.center = vector(0, 0, 0)
	scene.range = 0.9*length
	scene.background = color.white
	# 点のプロット
	cb = color.black
	arrow(pos=vector(vmin, 0, 0), axis=vector(length, 0, 0), shaftwidth=0.002, headwidth=0.05, color=cb)
	arrow(pos=vector(0, vmin, 0), axis=vector(0, length, 0), shaftwidth=0.002, headwidth=0.05, color=cb)
	arrow(pos=vector(0, 0, vmin), axis=vector(0, 0, length), shaftwidth=0.002, headwidth=0.05, color=cb)
	balls = [sphere(pos=vector(*v), radius=0.01, color=color.black) for v in inner]


if __name__=="__main__":
	main()