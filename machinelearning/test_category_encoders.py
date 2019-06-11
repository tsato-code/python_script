"""
conda install -c conda-forge category_encoders -y
"""
# ------------------
# モジュールインポート
# ------------------
import category_encoders as ce
import pandas as pd


# ------------------
# 定数パラメータ設定
# ------------------
INPUT_FILE = "../data/mushroom.csv"


# ------------------
#  自作関数
# ------------------



# ------------------
#  メイン処理
# ------------------
def main():
	df = pd.read_csv(INPUT_FILE, header=None, encoding="utf-8")
	print(df.head())
	print(df.describe())
	# 列指定
	list_cols = [0]
	# OneHotEncode
	# 分散0をdrop、fit後適用時の未知カテゴリを無視
	ce_ohe = ce.one_hot.OneHotEncoder(cols=list_cols, drop_invariant=True, handle_unknown="ignore")
	df_ce_onehot = ce_ohe.fit_transform(df)
	print(df_ce_onehot.head(5))
	# Helmert contrast coding
	ce_he = ce.helmert.HelmertEncoder(cols=list_cols, drop_invariant=True, handle_unknown="ignore")
	df_ce_helmert = ce_he.fit_transform(df)
	print(df_ce_helmert.head(5))
	# BaseNEncoder
	# 単に2進数表現に変換している可能性
	ce_bne = ce.basen.BaseNEncoder(cols=list_cols, drop_invariant=True, handle_unknown="ignore")
	df_ce_basen = ce_bne.fit_transform(df)
	print(df_ce_basen.head(5))



if __name__=="__main__":
	main()