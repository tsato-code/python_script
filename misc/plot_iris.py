# ------------------
# ディレクトリ構造
# ------------------
"""
┣ misc/plot_iris.py
┣ data/
┃ ┗ iris.csv
┗ out/
　 ┗ *.png
"""


# ------------------
# モジュールインポート
# ------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os


# ------------------
# 定数パラメータ設定
# ------------------
IN_FILE = '../data/iris.csv'	# 入力データ
OUT_DIR = '../out/'				# 出力先ディレクトリ


# ------------------
# 関数の定義
# ------------------
def make_figure(df):
	# 保存ファイル名の編集
	basename = os.path.basename(IN_FILE)
	basename, _ = os.path.splitext(basename)

	""" 図の生成 """
	make_figure_scatter(df, basename)
	make_figure_boxplot(df, basename)
	make_figure_violinplot(df, basename)
	make_figure_swarmplot(df, basename)
	make_figure_violin_swarmplot(df, basename)
	make_figure_lvplot(df, basename)
	make_figure_kdeplot(df, basename)
	make_figure_kde2dplot(df, basename)


def make_figure_scatter(df, basename):
	""" 散布図 """
	plt.figure()
	sns.pairplot(df, hue='class', palette='husl')

	# 透過なし 、余白なしで保存
	savename = os.path.join(OUT_DIR, basename)
	savename = savename + '_scatter.png'
	plt.savefig(savename, transparent=False, bbox_inches='tight', pad_inches=0)


def make_figure_boxplot(df, basename):
	""" 箱ひげ図 """
	cols = df.columns
	col_size = len(cols)

	# 各特徴量の箱ひげ図を一枚図に描画
	plt.figure(figsize=(8*col_size, 6))
	for i in range(1, col_size):
		plt.subplot(1, col_size, i)
		sns.boxplot(x=df['class'], y=df[cols[i-1]], palette='husl')
	
	# 透過なし、余白なしで保存
	savename = os.path.join(OUT_DIR, basename)
	savename = savename + '_boxplot.png'
	plt.savefig(savename, transparent=False, bbox_inches='tight', pad_inches=0)


def make_figure_violinplot(df, basename):
	""" violinplot """
	cols = df.columns
	col_size = len(cols)

	# 各特徴量のバイオリンを一枚図に描画
	plt.figure(figsize=(8*col_size, 6))
	for i in range(1, col_size):
		plt.subplot(1, col_size, i)
		sns.violinplot(x=df['class'], y=df[cols[i-1]], palette='husl')
	
	# 透過なし、余白なしで保存
	savename = os.path.join(OUT_DIR, basename)
	savename = savename + '_violinplot.png'
	plt.savefig(savename, transparent=False, bbox_inches='tight', pad_inches=0)


def make_figure_swarmplot(df, basename):
	""" swarmplot """
	cols = df.columns
	col_size = len(cols)

	# 各特徴量のswarmを一枚図に描画
	plt.figure(figsize=(8*col_size, 6))
	for i in range(1, col_size):
		plt.subplot(1, col_size, i)
		sns.swarmplot(x=df['class'], y=df[cols[i-1]], palette='husl')
	
	# 透過なし、余白なしで保存
	savename = os.path.join(OUT_DIR, basename)
	savename = savename + '_swarmplot.png'
	plt.savefig(savename, transparent=False, bbox_inches='tight', pad_inches=0)


def make_figure_violin_swarmplot(df, basename):
	""" violinplotとswarmplot """
	cols = df.columns
	col_size = len(cols)

	# 各特徴量のviolinとswarmを一枚図に描画
	plt.figure(figsize=(8*col_size, 6))
	for i in range(1, col_size):
		plt.subplot(1, col_size, i)
		sns.violinplot(x=df['class'], y=df[cols[i-1]], inner=None, color="0.95", linewidth=0.3)
		sns.swarmplot(x=df['class'], y=df[cols[i-1]], palette='husl')
	
	# 透過なし、余白なしで保存
	savename = os.path.join(OUT_DIR, basename)
	savename = savename + '_violin_swarmplot.png'
	plt.savefig(savename, transparent=False, bbox_inches='tight', pad_inches=0)


def make_figure_lvplot(df, basename):
	""" lvplot """
	cols = df.columns
	col_size = len(cols)

	# 各特徴量のlvを一枚図に描画
	plt.figure(figsize=(8*col_size, 6))
	for i in range(1, col_size):
		plt.subplot(1, col_size, i)
		sns.lvplot(x=df['class'], y=df[cols[i-1]], palette='husl')
	
	# 透過なし、余白なしで保存
	savename = os.path.join(OUT_DIR, basename)
	savename = savename + '_lvplot.png'
	plt.savefig(savename, transparent=False, bbox_inches='tight', pad_inches=0)


def make_figure_kdeplot(df, basename):
	""" kdeplot """
	cols = df.columns
	col_size = len(cols)

	categoly = list(set(df['class']))

	# 各特徴量の密度分布を一枚図に描画
	plt.figure(figsize=(8*col_size, 6))
	for i in range(1, col_size):
		plt.subplot(1, col_size, i)
		for c in categoly:
			sns.kdeplot(df[df['class']==c][cols[i-1]], label=c)
	
	# 透過なし、余白なしで保存
	savename = os.path.join(OUT_DIR, basename)
	savename = savename + '_kdeplot.png'
	plt.savefig(savename, transparent=False, bbox_inches='tight', pad_inches=0)


def make_figure_kde2dplot(df, basename):
	""" kde2dplot """
	cols = df.columns
	col_size = len(cols)
	categoly = list(set(df['class']))
	colors = ['Reds', 'Blues', 'Greens']
	c2c = {c:color for c, color in zip(categoly, colors)}

	# 各2軸の特徴量の密度分布を一枚図に描画
	plt.figure(figsize=(16, 12))
	plt.rcParams['font.size'] = 10
	for i in range(1, col_size):
		for j in range(1, col_size):
			plt.subplot(col_size-1, col_size-1, i+(j-1)*(col_size-1))
			for c in categoly:
				x = df[df['class']==c][cols[i-1]]
				y = df[df['class']==c][cols[j-1]]
				sns.kdeplot(x, y, shade=True, shade_lowest=False, cmap=c2c[c])
	
	# 透過なし、余白なしで保存
	savename = os.path.join(OUT_DIR, basename)
	savename = savename + '_kde2dplot.png'
	plt.savefig(savename, transparent=False, bbox_inches='tight', pad_inches=0)


# ------------------
#  メイン処理
# ------------------
def main():
	# データ読み込み
	df = pd.read_csv(IN_FILE, header=0, index_col=None, sep=',')
	
	# 出力先ディレクトリが存在しなければ新たに作成
	if not os.path.exists(OUT_DIR):
		os.makedirs(OUT_DIR)

    # 図の作成
	make_figure(df)


if __name__ == '__main__':
	main()