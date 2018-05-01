# 論文メモ

## 特徴量作成

1. [横山大作，伊藤正彦，豊田正史．ドライブレコーダを利用した運転者ごとの挙動傾向把握の試み．DEIM Forum 2015 D2-3．](http://db-event.jpn.org/deim2015/paper/308.pdf)
	- タスク：ドラレコデータから事故歴ありドライバの判別。
	- データ：ドラレコデータ（GPS軌跡、速度、加速度）、ドライバーの事故歴。
	- モデル：サポートベクターマシン。
	- 特徴：ドライバーの運転安全性の指標（特徴量）を作成。一次元連続分布を離散化し、離散確率分布としてモデル化。確率に対する情報量を用いて、外れ値を強調する特徴量を作成。事故歴ありのドライバを再現率70%、適合率61%の性能で判別。
	- 感想：特徴量の作り方が面白い。
1. [横山大作，豊田正史．事故防止に向けたドライブレコーダデータからの運転挙動分析．DEIM Forum 2016 H8-5．](http://db-event.jpn.org/deim2016/papers/390.pdf)
	- タスク：ドラレコデータから事故歴ありドライバの判別。
	- データ；ドラレコデータ（GPS軌跡、速度、加速度、ブレーキ動作、停止動作、ハンドル動作、右左折動作）、ドライバーの運転経歴データ（運転経歴、事故経歴）、道路データ（道路幅、一方通行、中央分離帯の有無）。
	- モデル：サポートベクトルマシン。
	- 特徴：ドライバーごとの運転動作分布、運転環境などから特徴量を設計。事故歴ありのドライバを最大で、再現率83%、適合率81%の性能で判別。
	- 感想：特徴量の作り方が面白い。
1. [豊田正史，横山大作，伊藤正彦．運転状況を考慮したドライブレコーダデータからの潜在リスク交差点検知手法． DEIM Forum 2017 A5-1](http://db-event.jpn.org/deim2017/papers/372.pdf)
	- タスク：事故発生したことがある交差点を判別。
	- データ：ドラレコデータ、道路数値地図データ、雨量データ。
	- モデル：ロジスティック回帰。
	- 特徴：既存研究では道路形状や環境情報から道路の事故リスクを求めていたが、運転操作データを使った試みが新しい。
	- 感想：特徴量を作るための分析が面白い。事故確率が高い交差点をランキングしたときの結果が気になる。

## Tree Model

1. [R. C. Steorts. Tree Based Methods: Regression Trees. Duke University Lecture Note: Data Mining and Machine Learning 2017.](http://www2.stat.duke.edu/~rcs46/lectures_2017/08-trees/08-tree-regression.pdf)
	- データマイニングと機械学習の講義ノート。
	- 回帰木の概要についてシンプルな説明。
1. [Rebecca C. Steorts. Tree Based Methods: Bagging, Boosting, and
Regression Trees. Duke University Lecture Note: Data Mining and Machine Learning 2017.](http://www2.stat.duke.edu/~rcs46/lectures_2017/08-trees/08-tree-advanced.pdf)
1. [Mihaela van der Schaar. Classification and Regression Trees. Stanford University lecture Note: Statistical Machine Learning.](http://www.stats.ox.ac.uk/~flaxman/HT17_lecture13.pdf)
1. [W. Y. Loh. Classification and Regression Trees. Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 1, 14-23, 2011.](https://onlinelibrary.wiley.com/doi/abs/10.1002/widm.8)
	- 分類木と回帰木についての解説。
	- 各モデルの様々なアルゴリズムを概観、比較実験など。
1.[J. Kazemitabar, A. Amini, A. Bloniarz, and A. S. Talwalkar. Variable Importance using Decision Trees. In Advances in Neural Information Processing Systems, 425--434, 2017.](http://papers.nips.cc/paper/6646-variable-importance-using-decision-trees)
1. [A. Karalic. Linear Regression in Regression Tree Leaves. Proceedings of ECAI-92, 1992.](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.35.2878) 
1. [L. Breiman. Random Forest. Machine Learning 45, 5--32, 2001.](https://link.springer.com/article/10.1023%2FA%3A1010933404324)
1. [A. Liaw and M. Wiener. Classification and Regression by randomForest. R news 2, 18--22, 2002.](https://www.researchgate.net/profile/Andy_Liaw/publication/228451484_Classification_and_Regression_by_RandomForest/links/53fb24cc0cf20a45497047ab/Classification-and-Regression-by-RandomForest.pdf)
