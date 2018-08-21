# ------------------
# モジュールインポート
# ------------------
from scipy import stats
import numpy as np


# ------------------
# 定数パラメータ設定
# ------------------
SEED = 0
MU1, VAR1, N1 = 1, 10, 50
MU2, VAR2, N2 = 2, 10, 50


# ------------------
# 関数の定義
# ------------------
def welch_ttest(X1, X2, alpha=0.05):
	mu1 = np.mean(X1)
	mu2 = np.mean(X2)
	var1 = np.var(X1, ddof=1)
	var2 = np.var(X2, ddof=1)
	n1 = len(X1)
	n2 = len(X2)
	t = (mu1-mu2)/np.sqrt(var1/n1+var2/n2) # 統計量t
	d = (var1/n1+var2/n2)**2/(var1**2/(n1**2*(n1-1))+var2**2/(n2**2*(n2-1))) # t分布に使う自由度d
	x = stats.t.ppf(1-alpha/2, d) # 自由度dのt分布の棄却域x
	reject_null_hypo = abs(t)>x # Trueなら帰無仮説を棄却、そうでなければ帰無仮説を採択
	return t, x, reject_null_hypo


# ------------------
#  メイン処理
# ------------------
def main():
	# データ生成
	np.random.seed(SEED)
	X1 = stats.norm.rvs(loc=MU1,scale=VAR1,size=N1)
	X2 = stats.norm.rvs(loc=MU2,scale=VAR2,size=N2)

	# scipy実装のウェルチのt検定
	s, p = stats.ttest_ind(X1, X2, equal_var=False)
	print('統計量t={}'.format(s))
	print('p値={}'.format(p)) # 統計量tがt分布の両側裾にいる確率p -> 有意水準alpha>pで帰無仮説を棄却 -> 対立仮説を採択

	# 自前実装のウェルチのt検定
	alpha = 0.1
	t, x, r = welch_ttest(X1, X2, alpha)
	print('統計量t={}'.format(t))
	print('両側棄却域|x|={}'.format(x))
	print('有意水準alpha={}で帰無仮説は棄却{}'.format(alpha, '（対立仮説を採択）' if r else 'できない'))


if __name__ == '__main__':
	main()