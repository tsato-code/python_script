# 文献メモ

## 可視化
1. [Maaten, L. V. D., & Hinton, G. (2008). Visualizing data using t-SNE. Journal of machine learning research, 9, 2579--2605.](http://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf)
	- t-SNE.

## 特徴量設計
1. [Chawla, S., Zheng, Y., & Hu, J. (2012). Inferring the root cause in road traffic anomalies. ICDM 2012. 141--150.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.711.7560&rep=rep1&type=pdf)
	- タスク：北京市の交通データから道路リンクの異常を検出、潜在的なOD流を予測。
	- 手法：主成分分析、線形計画法。
	- 特徴：ネットワークフローの問題と異常検知を同時に考えている。
	- データ：北京市タクシーGPS。
	- 感想：ネットワークフローと異常検知の組み合わせが面白い。
1. [Yokoyama, D. & Toyoda, M. (2016). Do Drivers' Behavior Reflect Their Past Driving Histories? -Large Scale Examination of Vehicle Recorder Data-. In 2016 IEEE International Congress on Big Data, 361--368.](https://pdfs.semanticscholar.org/3451/ff02e000f1f5f45f088ada50e904e8e60001.pdf)
	- タスク：ドラレコデータから事故歴ありドライバの判別。
	- 手法：サポールベクターマシン。
	- 特徴：平均的なドライバーとの違いを表す説明変数を作成。エントロピーやKL-ダイバージェンスを利用。
	- データ：ドライバー経歴、ドラレコデータ、道路情報データ。
	- 感想：KL-ダイバージェンスは調査が必要。
1. [芦田優太, 西岡到. (2015). 路側データから生成した交通流モデルによる高速道路の交通状況予測. 研究報告高度交通システムとスマートコミュニティ (ITS), 16, 1--6.](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=146271&item_no=1&page_id=13&block_id=8)
	- タスク：路側データから学習した道路交通流モデルを用いて高速道路における交通状況予測。
	- 手法：ルールベース+重回帰。
	- 特徴：時間帯、曜日、天候状況で分類→交通状況で予測モデル作成。
	- データ：アジア圏の路側データ。
	- 感想：データの出典が不明。関連研究のVARMA（ベクトル自己回帰移動平均モデル）が気になる。
1. [小川和晃, 田村哲嗣, 速水悟. (2016). 商品レビューにおける時系列情報に着目したクラスタ分析と可視化. JSAI 2016, 1F5-5.](https://kaigi.org/jsai/webprogram/2016/pdf/478.pdf)
	- タスク：商品レビューの時系列的な変化を解析。
	- 手法：k-means++、SOM。
	- 特徴：説明変数の作成に、TF-IDF、word2vecによる単語ベクトル化、時系列情報、属性情報など164次元を利用している。
	- データ：楽天市場「みんなのレビュー、口コミ情報」
	- 感想：結果の評価を主観に頼っているが、それでよいのかどうか。
1. [豊田正史，横山大作，伊藤正彦 (2017)．運転状況を考慮したドライブレコーダデータからの潜在リスク交差点検知手法． DEIM Forum 2017 A5-1.](http://db-event.jpn.org/deim2017/papers/372.pdf)
	- タスク：事故発生したことがある交差点を判別。
	- 手法：ロジスティック回帰。
	- 特徴：既存研究では道路形状や環境情報から道路の事故リスクを求めていたが、運転操作データを使った試みが新しい。
	- データ：ドラレコデータ、道路数値地図データ、雨量データ。
	- 感想：特徴量を作るための分析が面白い。事故確率が高い交差点をランキングしたときの結果が気になる。
1. [横山大作，伊藤正彦，豊田正史 (2015)．ドライブレコーダを利用した運転者ごとの挙動傾向把握の試み．DEIM Forum 2015 D2-3.](http://db-event.jpn.org/deim2015/paper/308.pdf)
	- タスク：ドラレコデータから事故歴ありドライバの判別。
	- 手法：サポートベクターマシン。
	- 特徴：ドライバーの運転安全性の指標（特徴量）を作成。一次元連続分布を離散化し、離散確率分布としてモデル化。確率に対する情報量を用いて、外れ値を強調する特徴量を作成。事故歴ありのドライバを再現率70%、適合率61%の性能で判別。
	- データ：ドラレコデータ（GPS軌跡、速度、加速度）、ドライバーの事故歴。
	- 感想：特徴量の作り方が面白い。
1. [横山大作，豊田正史 (2016)．事故防止に向けたドライブレコーダデータからの運転挙動分析．DEIM Forum 2016 H8-5.](http://db-event.jpn.org/deim2016/papers/390.pdf)
	- タスク：ドラレコデータから事故歴ありドライバの判別。
	- 手法：サポートベクトルマシン。
	- 特徴：ドライバーごとの運転動作分布、運転環境などから特徴量を設計。事故歴ありのドライバを最大で、再現率83%、適合率81%の性能で判別。
	- データ：ドラレコデータ（GPS軌跡、速度、加速度、ブレーキ動作、停止動作、ハンドル動作、右左折動作）、ドライバーの運転経歴データ（運転経歴、事故経歴）、道路データ（道路幅、一方通行、中央分離帯の有無）。
	- 感想：特徴量の作り方が面白い。
1. [村尾和哉, クリストフファンラールホーフェン, 寺尾努, 西尾章治郎. (2010). センサのピークを用いた状況認識手法. 情報処理学会論文誌 51, 1067--1077.](https://www.eti.uni-siegen.de/ubicomp/papers/ess_ipsj2010.pdf)
	- タスク：信号データを圧縮した特徴量の作成。
	- 手法：特徴量の評価のためクラスタリングおよびサポートベクトルマシンを利用。
	- 特徴：これまで、平均値、分散値、最大値および最小値、FFTパワースペクトルが波形データの特徴量として利用されていたが、新たに波形ピーク高さと幅を特徴量として利用。
	- データ：たとえば、人間に取り付けた複数の加速度センサ情報。
	- 感想：複数のデータセットで実験してほしい。加えて、アイデアがシンプルなだけに、似たものが提案されていそうな気がする。。

## 時系列分析
1. [貞広幸雄. (2013). 時系列空間データの探索的解析手法. オペレーションズ・リサーチ 58, 18--23.](http://www.orsj.or.jp/archive2/or58-01/or58_1_18.pdf)
	- タスク：時系列空間データの局所的類似性抽出。
	- 手法：時系列データに対する幾何的性質を用いた新手法。具体的には、平面にプロットした複数の時系列データからポリゴン形状を抽出し、そのポリゴン情報から分類および可視化を行う。
	- 特徴：時系列データを局所類似性で分類可能らしい。
	- データ：ユタ州ソルトレーク群の時系列空間データ。
	- 感想：提案された分析手法は空間データの性質を使っていないように感じる。
1. [Bacci, S., Pandolfi, S., & Pennoni, F. (2014). A comparison of some criteria for states selection in the latent Markov model for longitudinal data. Advances in Data Analysis and Classification, 8, 125--145.](https://www.researchgate.net/profile/Silvia_Bacci/publication/233815708_A_comparison_of_some_criteria_for_states_selection_in_the_latent_Markovmodel_for_longitudinal_data/links/549042730cf225bf66a827fe/A-comparison-of-some-criteria-for-states-selection-in-the-latent-Markovmodel-for-longitudinal-data.pdf)

## 異常検知
1. [Gupta, M. Gao, Jing. Aggarwal, C. & Han, J. (2013). Outlier Detection for Temporal Data. SDM 2013.](https://archive.siam.org/meetings/sdm13/gupta.pdf)
	- 外れ値検出のスライド資料。
	- 特に、系列データ、ストリームデータ、空間系列データ、ネットワークデータについて。
1. [Kinoshita, A., Takasu, A., & Adachi, J. (2015). Real-time traffic incident detection using a probabilistic topic model. Information Systems, 54, 169--188.](https://www.sciencedirect.com/science/article/pii/S0306437915001301)
1. [Pang, L. X., Chawla, S., Liu, W., & Zheng, Y. (2011). On mining anomalous patterns in road traffic streams. ICADMA 2011, 237--251.](https://link.springer.com/chapter/10.1007%2F978-3-642-25856-5_18)
	- タスク：タクシーGPSデータから北京市の恒常的な外れ値と新規出現の外れ値を検出。
	- 手法：尤度比検定。
	- 特徴：upper-bounding strategyとやらを使って限定操作を行い、異常度の高い上位k個の領域を計算している。
	- データ：人工データ、北京市タクシーのGPSデータ。
	- シンプルだがおもしろい。[関連スライド](https://pdfs.semanticscholar.org/db55/8e1bfb8feaae50919a2952979a894669e486.pdf)もある。
1. [切通恵介, 泉谷知範. (2017). 機械学習を用いた工場機器の故障予測. DEIM Forum 2017 H2-1.](http://db-event.jpn.org/deim2017/papers/200.pdf)
	- タスク：センサーデータから工場機器の故障予測。
	- 手法：ロジスティック回帰、SVM、ニューラルネット。
	- 特徴：異常検知タスクの正常データを適当にサンプリングして、各サンプル数で精度比較している。
	- データ：24種のセンサーデータ、説明変数の次元は240～2880。
	- 感想：取得したデータをそのまま使うのではなく、クラスごとのサンプル数偏りにアプローチしている点が面白い。
1. [高橋佑介, 横本大輔, 宇津呂武仁, 吉岡真治, 河田容英, 神門典子, 福原知宏, 中川裕志, 清田陽司. (2012). 時系列トピックモデルにおけるバーストの同定. DEIM Forum 2012 F5-5.](http://db-event.jpn.org/deim2012/proceedings/final-pdf/f5-5.pdf)
	- タスク：時系列ニュース記事の情報収集。
	- トピックモデルDTM (Dynamic Topic Model)、Kleinbergのバースト検知。
	- キーワード単位ではなく、トピック単位のバースト検知をしている。
	- データ：新聞3社のニュースサイト27000記事。
	- 感想：使っている手法は既存のものでシンプルなアプローチに見える。組み合わせが面白い。
1. [坪内孝太, 下坂正倫, 小西達也, 丸山三喜也, 山下達雄. (2017). 乗換案内データを用いた未来の混雑予測の研究. JSAI 2017, 4I1-4in1.](https://kaigi.org/jsai/webprogram/2017/pdf/1107.pdf)
	- タスク：位置に関する予定情報から異常予測。
	- 手法：ARのようなもの、対数線形ランクポアソン回帰による都市動態推定手法。
	- 特徴：通常時と予測値の乖離度で異常を定義している。
	- データ：Yahoo! Japan経路検索ログ、2016年12月のコミケ。
	- 感想：「人の流れ」について「平常時と異常時」の考え方を導入しているところが面白い。
1. [中原孝信, 前川浩基, 羽室行信. (2013). テレビ番組視聴時におけるTwitter投稿からのトピック検知. オペレーションズ・リサーチ 58, 442--448.](http://www.orsj.or.jp/archive2/or58-08/or58_8_442.pdf)
	- タスク：特定のTV番組を視聴中にその番組に関するTwitter投稿をするソーシャルビューイングの内容を要約。
	- 手法：マイクロクラスタリング、Kleinbergのバースト検知手法、ナップサック制約付き最大被覆問題の貪欲解放。
	- 特徴：Tweetの単語共起情報からトピック作成にマイクロクラスタリング利用、Tweetの盛り上がり検出にKleinbergのバースト検知手法、Tweetの要約にナップサック制約付き最大被覆問題の貪欲解法を利用。
	- データ：宇宙兄弟に関するTweet約28万件、TV番組「宇宙兄弟」の台詞。
	- 感想：数理モデルを使いこなしている感じがよい。
1. [山本敬介. (2013). 混合分布による道路状態推定. 東京大学大学院情報理工学系研究科修士論文, 2013.](http://repository-old.dl.itc.u-tokyo.ac.jp/dspace/bitstream/2261/54210/1/48116445.pdf)

## 画像処理
1. [Rubner, Y., Tomasi, C., & Guibas, L. J. (2000). The earth mover's distance as a metric for image retrieval. International journal of computer vision, 40, 99--121.](http://robotics.stanford.edu/~rubner/papers/rubnerIjcv00.pdf)
	- Earth Mover's Distance.
	- 画像のEMD計算実験、ビンの輸送コストの設定、三角不等式の証明、下界値の導出など。
1. [Boykov, Y. Y., & Jolly, M. P. (2001). Interactive graph cuts for optimal boundary and region segmentation of objects in ND images. ICCV 2001. 105--112.](http://www.csd.uwo.ca/~yuri/Papers/iccv01.pdf)
	- 画像の領域分割に対するグラフカット。

## 微分方程式モデル
1. [中桐裕子, 栗田治. (2002). 狂牛病の微分方程式モデル. オペレーションズ・リサーチ 40, 666--674.](http://orsj.or.jp/~archive/pdf/bul/Vol.47_10_666.pdf)
	- タスク：「流行」に関する数理モデル構築。
	- 手法：微分方程式。
	- 特徴：解釈の例が豊富。
	- データ：畜産統計データ。
	- 感想：豊富な例のもと、微分方程式モデルが理解しやすいのかもしれない。
1. [中桐裕子, 栗田治. (2004). 社会的なブームの微分方程式モデル. 日本オペレーションズ・リサーチ学会和文論文誌 47, 83--105.](http://www.orsj.or.jp/~archive/pdf/j_mag/Vol.47_J_083.pdf)
	- タスク：社会的な流行をモデル化して、その特性を把握。
	- 手法：微分方程式モデル。
	- 特徴：流行に関して4つの状態を定義し、各状態の顧客数の関数を微分方程式で記述。
	- データ：1変量データ。即席めん消費データ、焼酎消費データ、J1の平均観客動員数データ、ビリヤード参加人口データ、犬種別頭数データ、特定単語が新聞記事中に出現する数。
	- 感想：微分方程式のモデル表現力と解析が気になる。実は、これよりもモデル表現力が高く、解析しやすいモデル枠組みが存在するのではないだろうか。

## 木構造モデル
1. [Breiman, L. (2001). Random Forest. Machine Learning 45, 5--32.](https://link.springer.com/article/10.1023%2FA%3A1010933404324)
1. [Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. In KDD '16 785--794.](https://dl.acm.org/citation.cfm?id=2939785)
1. [Karalic, A. (1992). Linear Regression in Regression Tree Leaves. Proceedings of ECAI-92.](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.35.2878) 
	- タスク：回帰。
	- 手法：回帰木。
	- 特徴：既存の回帰木は、葉の領域に入る訓練データの目的変数の平均値を葉の値としていた。提案手法は、葉で線形回帰を行う。local linear regressionというらしい。
	- データ：6つのデータセット。
	- 感想：昔の論文は読みにくい。
1. [Kazemitabar, J., Amini, A., Bloniarz, A. & Talwalkar, A. S. (2017). Variable Importance using Decision Trees. In NIPS 2017, 425--434.](http://papers.nips.cc/paper/6646-variable-importance-using-decision-trees)
1. [Loh, W. Y. (2011). Classification & Regression Trees. Wiley Interdisciplinary Reviews: Data Mining & Knowledge Discovery, 1, 14-23.](https://onlinelibrary.wiley.com/doi/abs/10.1002/widm.8)
	- 分類木と回帰木についての解説記事。
	- 各モデルの様々なアルゴリズムを概観、比較実験など。
1. [Schaar, M. van der (2017). Statistical Machine Learning, Classification and Regression Trees. University of Oxford Lecture Note.](http://www.stats.ox.ac.uk/~flaxman/HT17_lecture13.pdf)
	- 統計的機械学習の講義スライド。
	- 分類木と回帰木の詳しい計算手続きが、分枝の計算例とともに掲載されている。
1. [Steorts, R. C. (2017). Data Mining and Machine Learning, Tree Based Methods: Regression Trees. Duke University Lecture Slide.](http://www2.stat.duke.edu/~rcs46/lectures_2017/08-trees/08-tree-regression.pdf)
	- データマイニングと機械学習の講義スライド。
	- 回帰木の概要についてシンプルな説明。
1. [Steorts, R. C. (2017). Data Mining and Machine Learning, Tree Based Methods: Bagging, Boosting, and
Regression Trees. Duke University Lecture Slide.](http://www2.stat.duke.edu/~rcs46/lectures_2017/08-trees/08-tree-advanced.pdf)
	- データマイニングと機械学習の講義スライド。
	- Baggin, Boosting, Regression Treesについてボリュームある説明。
	- 木構造の利点のひとつは解釈性であるが、Random Forestのように木がたくさんあると、解釈しにくい。解釈のためのひとつの方法としてvariable importanceを考える。これは回帰であればRSSを用い、分類であればGini indexを使う。

## データ構造
1. [Bury, M., Schwiegelshohn, C., & Sorella, M. (2016). Efficient Similarity Search in Dynamic Data Streams. arXiv preprint arXiv:1605.03949.](https://arxiv.org/abs/1605.03949)
1. [Charikar, M. S. (2002). Similarity estimation techniques from rounding algorithms. In Proceedings of the thiry-fourth annual ACM symposium on Theory of computing, 380--388. ACM.](http://www.cs.princeton.edu/courses/archive/spring04/cos598B/bib/CharikarEstim.pdf)
1. [Fagin, R., Kumar, R., & Sivakumar, D. (2003, June). Efficient similarity search and classification via rank aggregation. In Proceedings of the 2003 ACM SIGMOD international conference on Management of data, 301-312. ACM.](https://s3.amazonaws.com/academia.edu.documents/34071215/rank-aggregation.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1526142136&Signature=qPX4aYR5Y2B21fmfb8qNts08OwI%3D&response-content-disposition=inline%3B%20filename%3DEfficient_similarity_search_and_classifi.pdf)
1. [Guttman, A. (1984). R-trees: A dynamic index structure for Spatial Searching. In SIGMOD, 47--57.](https://klevas.mif.vu.lt/~algis/DSA/guttman.pdf)
1. [Khan, M., Ding, Q., & Perrizo, W. (2002). K-Nearest Neighbor Classification on Spatial Data Streams Using P-Trees. In PAKDD 517--528.](https://pdfs.semanticscholar.org/0286/c5fee2dea935c601d55b44ef8cae965bbff7.pdf)
1. [Kingsford. S. Bioinformatics Lectures. Carnegie Mellon University Lecture Slide.](http://kingsfordlab.cbd.cmu.edu/bioinformatics-lectures/)
	- QuadTree, Kd-Treeなど。
1. [Kunze, M. & Weske, M. (2010). Metric Trees for Efficient Similarity Search in Large Process Model Repositories. In International Conference on Business Process Management. 535-546. Springer, Berlin, Heidelberg.](https://link.springer.com/chapter/10.1007/978-3-642-20511-8_49)
1. [Manolopoulos, Y., Nanopoulos, A., Papadopoulos, A. N., Theodoridis, Y. (2005).  R-trees: Theory and Applications. Springer-Verlag London.](http://delab.csd.auth.gr/rtrees/)
	- 空間データ構造R-treeのテキスト。
	- 1章(Introduction)と2章(Dynamic Version of R-trees)はリンク先からダウンロードできる。
1. [Papadias, D., Zhang, J., Mamoulis, N., & Tao, Y. (2003). Query processing in spatial network databases. VLDB 2003, 802--813.](http://repository.ust.hk/ir/bitstream/1783.1-157/1/VLDB03SNDB.pdf)
1. [Shi, J., Mamoulis, N., Wu, D., & Cheung, D. W. (2014). Density-based place clustering in geo-social networks. SIGMOD 2014, 99--110.](https://i.cs.hku.hk/~nikos/sigmod14.pdf)
1. [Toma. L. (2016). Algorithms in GIS. Bowdoin College Lecture Slide.](http://www.bowdoin.edu/~ltoma/teaching/cs3225-GIS/fall16/syllabus.html)
	- Quad Treeなど。
1. [Turney, P. D., & Pantel, P. (2010). From frequency to meaning: Vector space models of semantics. Journal of artificial intelligence research, 37, 141--188.](https://www.jair.org/index.php/jair/article/view/10640)
1. [Van Der Maaten, L. (2014). Accelerating t-SNE using tree-based algorithms. Journal of machine learning research, 15, 3221--3245.](http://www.jmlr.org/papers/volume15/vandermaaten14a/vandermaaten14a.pdf)
	- t-SNEの高速化のために、微分するときの距離を近似する方法として四分木を利用している。
1. [Yianilos, P. N. (1993). Data Structures and Algorithms for Nearest Neighbor Search in General Metric Spaces. In SODA 93, 311--321.](http://pnylab.com/papers/vptree/vptree.pdf)
1. [Yao, Y. (2017). Advanced Techniques for High Dimensional Data, The R-tree. University of Queensland Lecture Slide.](http://www.cse.cuhk.edu.hk/~taoyf/course/infs4205/www/index.html)
	- 高次元データに対するテクニック集。
	- R-Treeの擬似コードがある。
1. [岩崎雅二郎 (2011). 木構造型インデックスを用いた近似k最近傍グラフによる近傍検索. 情報処理学会論文誌 52, 817--828.](https://ci.nii.ac.jp/naid/110008507921/)
	- タスク：空間データのk近傍の索引化。
	- 手法：既存の空間データ構造ANNを改善したもの。
	- 特徴：木構造を利用。
	- データ：一様分布データ、画像特徴量。
	- 感想：条件1が成立する状況が不明。参考文献に上げられているVLDB Journalを要確認。
1. [塚原拓人, 薫于洋, 陳漢雄, 古瀬一隆 (2017). 集約k近傍の効率的な検索方法. DEIM Forum 2017 C8-2.](http://db-event.jpn.org/deim2017/papers/155.pdf)
	- タスク：集約k近傍検索。
	- 手法：タスクの特殊ケースを扱うデータ構造を拡張したもの。
	- 特徴：距離関数の性質を使って枝刈り、凸包+クラスタリングなどの幾何的性質を使ってクエリの前処理。
	- データ：北アメリカの人工集落の緯度経度など。
	- 感想：いかに枝刈りするか、無駄な計算をしないような前処理など、随所に工夫がありおもしろい。実験結果がそれほどよく見えないのが残念。
1. [劉健全, 陳漢雄, 北川博之. (2012). 特化したR木空間索引を用いた効率的な逆最遠望検索. DEIM Forum 2012 D8-4.](http://db-event.jpn.org/deim2012/proceedings/final-pdf/d8-4.pdf)
