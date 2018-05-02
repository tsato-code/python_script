# 論文メモ

## 特徴量作成

1. [横山大作，伊藤正彦，豊田正史 (2015)．ドライブレコーダを利用した運転者ごとの挙動傾向把握の試み．DEIM Forum 2015 D2-3．](http://db-event.jpn.org/deim2015/paper/308.pdf)
	- タスク：ドラレコデータから事故歴ありドライバの判別。
	- データ：ドラレコデータ（GPS軌跡、速度、加速度）、ドライバーの事故歴。
	- モデル：サポートベクターマシン。
	- 特徴：ドライバーの運転安全性の指標（特徴量）を作成。一次元連続分布を離散化し、離散確率分布としてモデル化。確率に対する情報量を用いて、外れ値を強調する特徴量を作成。事故歴ありのドライバを再現率70%、適合率61%の性能で判別。
	- 感想：特徴量の作り方が面白い。
1. [横山大作，豊田正史 (2016)．事故防止に向けたドライブレコーダデータからの運転挙動分析．DEIM Forum 2016 H8-5．](http://db-event.jpn.org/deim2016/papers/390.pdf)
	- タスク：ドラレコデータから事故歴ありドライバの判別。
	- データ；ドラレコデータ（GPS軌跡、速度、加速度、ブレーキ動作、停止動作、ハンドル動作、右左折動作）、ドライバーの運転経歴データ（運転経歴、事故経歴）、道路データ（道路幅、一方通行、中央分離帯の有無）。
	- モデル：サポートベクトルマシン。
	- 特徴：ドライバーごとの運転動作分布、運転環境などから特徴量を設計。事故歴ありのドライバを最大で、再現率83%、適合率81%の性能で判別。
	- 感想：特徴量の作り方が面白い。
1. [豊田正史，横山大作，伊藤正彦 (2017)．運転状況を考慮したドライブレコーダデータからの潜在リスク交差点検知手法． DEIM Forum 2017 A5-1](http://db-event.jpn.org/deim2017/papers/372.pdf)
	- タスク：事故発生したことがある交差点を判別。
	- データ：ドラレコデータ、道路数値地図データ、雨量データ。
	- モデル：ロジスティック回帰。
	- 特徴：既存研究では道路形状や環境情報から道路の事故リスクを求めていたが、運転操作データを使った試みが新しい。
	- 感想：特徴量を作るための分析が面白い。事故確率が高い交差点をランキングしたときの結果が気になる。
1. [貞広幸雄. (2013). 時系列空間データの探索的解析手法. オペレーションズ・リサーチ 58, 18--23.](http://www.orsj.or.jp/archive2/or58-01/or58_1_18.pdf)
1. [村尾和哉, クリストフファンラールホーフェン, 寺尾努, 西尾章治郎. (2010). センサのピーク地を用いた状況認識手法. 情報処理学会論文誌 51, 1067--1077.](https://www.eti.uni-siegen.de/ubicomp/papers/ess_ipsj2010.pdf)

## Tree Model

1. [Steorts, R. C. (2017). Tree Based Methods: Regression Trees. Duke University Lecture Note: Data Mining and Machine Learning.](http://www2.stat.duke.edu/~rcs46/lectures_2017/08-trees/08-tree-regression.pdf)
	- データマイニングと機械学習の講義ノート。
	- 回帰木の概要についてシンプルな説明。
1. [Steorts, R. C. (2017). Tree Based Methods: Bagging, Boosting, and
Regression Trees. Duke University Lecture Note: Data Mining and Machine Learning.](http://www2.stat.duke.edu/~rcs46/lectures_2017/08-trees/08-tree-advanced.pdf)
1. [Schaar, M. van der (2017). Classification and Regression Trees. Stanford University lecture Note: Statistical Machine Learning.](http://www.stats.ox.ac.uk/~flaxman/HT17_lecture13.pdf)
1. [Loh, W. Y. (2011). Classification and Regression Trees. Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 1, 14-23.](https://onlinelibrary.wiley.com/doi/abs/10.1002/widm.8)
	- 分類木と回帰木についての解説。
	- 各モデルの様々なアルゴリズムを概観、比較実験など。
1. [Kazemitabar, J., Amini, A., Bloniarz, A. and Talwalkar, A. S. (2017). Variable Importance using Decision Trees. In Advances in Neural Information Processing Systems, 425--434.](http://papers.nips.cc/paper/6646-variable-importance-using-decision-trees)
1. [Karalic, A. (1992). Linear Regression in Regression Tree Leaves. Proceedings of ECAI-92.](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.35.2878) 
1. [Breiman, L. (2001). Random Forest. Machine Learning 45, 5--32.](https://link.springer.com/article/10.1023%2FA%3A1010933404324)
1. [Liaw, A. and Wiener, M. (2002). Classification and Regression by randomForest. R news 2, 18--22.](https://www.researchgate.net/profile/Andy_Liaw/publication/228451484_Classification_and_Regression_by_RandomForest/links/53fb24cc0cf20a45497047ab/Classification-and-Regression-by-RandomForest.pdf)

## Indexing

1. [劉健全, 陳漢雄, 北側博之. (2012). 特化したR木空間索引を用いた効率的な逆最遠望検索. DEIM Forum 2012 D8-4.](http://db-event.jpn.org/deim2012/proceedings/final-pdf/d8-4.pdf)
1. [塚原拓人, 薫于洋, 陳漢雄, 古瀬一隆 (2017). 集約k近傍の効率的な検索方法. DEIM Forum 2017 C8-2.](http://db-event.jpn.org/deim2017/papers/155.pdf)
1. [岩崎雅二郎 (2011). 木構造型インデックスを用いた近似k最近傍グラフによる近傍検索. 情報処理学会論文誌 52, 817--828.](https://ci.nii.ac.jp/naid/110008507921/)
1. [Yianilos, P. N. (1993). Data Structures and Algorithms for Nearest Neighbor Search in General Metric Spaces. in SODA 93, 311--321.](http://pnylab.com/papers/vptree/vptree.pdf)