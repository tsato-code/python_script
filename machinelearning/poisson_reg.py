"""
statsmodelsの使用
"""
# ------------------
# モジュールインポート
# ------------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# ------------------
# 定数パラメータ設定
# ------------------
RESP_VAR = "Lottery"
EXPR_VARS = ["Literacy", "Pop1831"]
"""
"dept", "Region", "Department", "Crime_pers", "Crime_prop", "Literacy",
"Donations", "Infants", "Suicides", "MainCity", "Wealth", "Commerce",
"Clergy", "Crime_parents", "Infanticide", "Donation_clergy", "Lottery",
"Desertion", "Instruction", "Prostitutes", "Distance", "Area",
"Pop1831"
"""


# ------------------
# 関数の定義
# ------------------


# ------------------
# メイン処理
# ------------------
def main():
	dat = sm.datasets.get_rdataset("Guerry", "HistData").data
	y = dat[RESP_VAR]
	X = dat[EXPR_VARS]
	# ポアソン回帰
	poisson_reg = smf.GLM(endog=y, exog=X, family=sm.families.Poisson()).fit()
	print(poisson_reg.summary())
	# ポアソン回帰 + elastic net
	frames = []
	for weight in np.arange(0, 10, 0.5).tolist():
		poisson_reg_ela = smf.GLM(endog=y, exog=X, family=sm.families.Poisson()).fit_regularized(
			refit=True,
			method='elastic_net',
			alpha=100.0,
			L1_wt=weight,
			start_params=None)
		frames.append(poisson_reg_ela.params)
		# print(poisson_reg_ela.summary())
	# 描画
	df = pd.DataFrame(frames, columns=EXPR_VARS)
	df.index=np.arange(0, 10, 0.5).tolist()
	fig, ax = plt.subplots(1, 1, figsize=(6, 4))
	ax = df.iloc[:, :].plot(ax=ax)
	ax.set_title('Coefficient')
	plt.show()
		

if __name__=="__main__":
	main()