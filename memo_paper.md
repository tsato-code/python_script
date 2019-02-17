# 文献メモ

## 可視化
1. [Maaten, L. V. D., & Hinton, G. (2008). Visualizing data using t-SNE. Journal of machine learning research, 9, 2579--2605.](http://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf)
	- t-SNEの提案。
1. [Shubham BarudwaleWEST NILE- ML+ Data Visualisation + Data Analysis](https://www.kaggle.com/barudwale20/west-nile-ml-data-visualisation-data-analysis)
	- Kaggle のカーネル。
	- 緯度経度のヒートマップ作成。
1. [金月寛彰, 服部宏充. (2015). プローブカーデータを利用したタクシードライバーの個人特性の分析とモデル化. JSAI 2015. 1N4-4.](http://www.ai-gakkai.or.jp/jsai2015/webprogram/2015/pdf/1N4-4.pdf)
	- タスク：タクシーの運転行動を可視化。
	- 手法：独自ビューワによる可視化、ヒートマップ、有限状態遷移機械。
	- 特徴：カウントと閾値による主観評価。タクシーが顧客獲得の際に付け待ち営業か、流し営業か、判定。
	- データ：京都市内のタクシープローブデータ。
	- 感想：泥臭い作業が多そう。

## 都市計算
1. [Altintasi, O., Tuydes-Yaman, H., & Tuncay, K. (2017). Detection of urban traffic patterns from Floating Car Data (FCD). Transportation Research Procedia, 22, 382-391.](file:///C:/Users/tsk_sato/Downloads/Altintasietal.2017TransportationResearchProcedia.pdf)
	- 交通パターンの計算。
1. [Ramezani, M., & Geroliminis, N. (2015). Queue profile estimation in congested urban networks with probe data. Computer‐Aided Civil and Infrastructure Engineering, 30(6), 414-432.](https://infoscience.epfl.ch/record/202147/files/MR_NG_2014.pdf)
	- 混雑予測。
1. [Urban Computing | Microsoft](https://www.microsoft.com/en-us/research/project/urban-computing/)
	- 都市データの解析。主に北京。
	- たとえば、gps trajectoryなど。
1. [Zhang, K., & Xue, G. (2010). A Real-time urban traffic detection algorithm based on spatio-temporal OD matrix in vehicular sensor network. Wireless Sensor Network, 2(09), 668.](http://file.scirp.org/pdf/WSN20100900003_96027105.pdf)
	- ODデータで何かする。
1. [谷直樹, 風間一洋, 榊剛史, 吉田光男. (2015). 位置情報付きツイートから抽出した交通路の評価. JSAI 2015, 1H3-4.](http://www.ai-gakkai.or.jp/jsai2015/webprogram/2015/pdf/1H3-4in.pdf)
	- タスク：ジオタグ付きツイートから公共交通機関の交通路抽出。
	- 手法：Hough変換、独自アルゴリズム。
	- 特徴：独自アルゴリズムで近似直線をつくる。
	- データ：ジオタグ付きツイート。
	- 感想：参考文献にはないが、交通路抽出に関連する文献が気になる。

## ルールベース
1. [芦田優太, 西岡到. (2015). 路側データから生成した交通流モデルによる高速道路の交通状況予測. 研究報告高度交通システムとスマートコミュニティ (ITS), 16, 1--6.](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=146271&item_no=1&page_id=13&block_id=8)
	- タスク：路側データから学習した道路交通流モデルを用いて高速道路における交通状況予測。
	- 手法：ルールベース+重回帰。
	- 特徴：時間帯、曜日、天候状況で分類→交通状況で予測モデル作成。
	- データ：アジア圏の路側データ。
	- 感想：データの出典が不明。関連研究のVARMA（ベクトル自己回帰移動平均モデル）が気になる。

## 解釈可能性
1. [Ribeiro, M. T., Singh, S., & Guestrin, C. (2016, August). Why should i trust you?: Explaining the predictions of any classifier. In Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining (pp. 1135-1144). ACM.](http://www.kdd.org/kdd2016/papers/files/rfp0573-ribeiroA.pdf)
	- LIME (Local Interpretable Model-agnostic Explanations).
	- [Qiita: LIMEで機械学習の予測結果を解釈してみる](https://qiita.com/fufufukakaka/items/d0081cd38251d22ffebf)

## 時系列分析
1. [Aghabozorgi, S., Shirkhorshidi, A. S., & Wah, T. Y. (2015). Time-series clustering–A decade review. Information Systems 53, 16--38.](http://repository.um.edu.my/101412/1/ali-1.pdf)
	- 系列データのクラスタリングサーベイ。
1. [Bacci, S., Pandolfi, S., & Pennoni, F. (2014). A comparison of some criteria for states selection in the latent Markov model for longitudinal data. Advances in Data Analysis and Classification, 8, 125--145.](https://www.researchgate.net/profile/Silvia_Bacci/publication/233815708_A_comparison_of_some_criteria_for_states_selection_in_the_latent_Markovmodel_for_longitudinal_data/links/549042730cf225bf66a827fe/A-comparison-of-some-criteria-for-states-selection-in-the-latent-Markovmodel-for-longitudinal-data.pdf)
1. [Zhang, J., Zheng, Y., & Qi, D. (2017, February). Deep Spatio-Temporal Residual Networks for Citywide Crowd Flows Prediction. In AAAI (pp. 1655-1661).](http://www.aaai.org/ocs/index.php/AAAI/AAAI17/paper/download/14501/13964)
	- タスク：時空間の流入量と流出量の予測。
	- 手法：ST-ResNetという深層学習のネットワークを提案。STはSpatio-Temporalの略だと思われる。
	- 特徴：residual networkと呼ばれるネットワクの枠組みを扱うとともに、時間的な近さ、期間、傾向をそれぞれ扱うようなネットワーク構造を構成。
	- データ：北京のタクシーGPSデータ、ニューヨークのバイクトリップデータ。
	- 感想：ネットワークの構造が、仮説に基づいて構成されているよう。コードはGitHubのluckroy/DeepSTで公開されている。
1. [小川和晃, 田村哲嗣, 速水悟. (2016). 商品レビューにおける時系列情報に着目したクラスタ分析と可視化. JSAI 2016, 1F5-5.](https://kaigi.org/jsai/webprogram/2016/pdf/478.pdf)
	- タスク：商品レビューの時系列的な変化を解析。
	- 手法：k-means++、SOM。
	- 特徴：説明変数の作成に、TF-IDF、word2vecによる単語ベクトル化、時系列情報、属性情報など164次元を利用している。
	- データ：楽天市場「みんなのレビュー、口コミ情報」
	- 感想：結果の評価を主観に頼っているが、それでよいのかどうか。
1. [貞広幸雄. (2013). 時系列空間データの探索的解析手法. オペレーションズ・リサーチ 58, 18--23.](http://www.orsj.or.jp/archive2/or58-01/or58_1_18.pdf)
	- タスク：時系列空間データの局所的類似性抽出。
	- 手法：時系列データに対する幾何的性質を用いた新手法。具体的には、平面にプロットした複数の時系列データからポリゴン形状を抽出し、そのポリゴン情報から分類および可視化を行う。
	- 特徴：時系列データを局所類似性で分類可能らしい。
	- データ：ユタ州ソルトレーク群の時系列空間データ。
	- 感想：提案された分析手法は空間データの性質を使っていないように感じる。
1. [角田孝昭, 吉田光男, 津川翔, 山本幹雄. (2015). 状態空間モデルを用いた検索トレンドとページビューからの自動車販売台数の予測. JSAI 2015, 3C3-3.](https://www.ai-gakkai.or.jp/jsai2015/webprogram/2015/pdf/3C3-3.pdf)
	- タスク：自動車販売台数の予測。
	- 手法：状態空間モデルの解法。
	- 特徴：自動車販売データとweb検索数の関係をモデル化。
	- データ：検索行動数をGoogle Trends、Wikipediaのページ閲覧数、新車販売台数データ。
	- 感想：「状態空間モデルは時系列データの要因分解及び将来予測を可能にする強力な枠組みの一つである」と書かれているのが興味深い。あと、n期先予測は状態方程式と観測方程式から求める観測地分布の期待値とあるが、よくわかっていない。。
1. [中村仁之, 櫻井彰人. (2016). サポートベクター回帰とカルマンフィルタを組み合わせた風速予測. JSAI 2016, 4M1-3.](http://www.ai-gakkai.or.jp/jsai2016/webprogram/2016/pdf/1055.pdf)
	- タスク：風速予測。
	- 手法：サポートネクター回帰、カルマンフィルタ。
	- 特徴：2つのSVRの結合計数をカルマンフィルタで逐次調整。
	- データ：慶応大学八神キャンパス屋上の風車。
	- 感想：時系列データを扱っているので、よく使われる時系列モデル（ARIMAなど）と比較すべき。

## 音響処理
1. [高橋玄他 (2017). DNN-GMMと連結特徴量を用いた音響シーン識別の検討. 日本音響学会講演論文集2017年3月, 135--138.](http://www.tara.tsukuba.ac.jp/~maki/reprint/Yamada/takahashi17-3asj135-138.pdf)
	- タスク：音響シーン識別（どんな場所か、どんな状況か）。
	- 手法：DNN+GMM
	- 特徴：既存研究のDNN-HMMのHMMをGMMで置き換え。
	- データ：DCASE2016 challengeという、環境音認識のワークショップで提供されたデータセット。
	- 感想：アイデアはシンプル。

## 異常検知
1. [Anantharam, P., Thirunarayan, K., Marupudi, S., Sheth, A. P., & Banerjee, T. (2016, February). Understanding City Traffic Dynamics Utilizing Sensor and Textual Observations. In AAAI (pp. 3793-3799).](http://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/download/12047/12162)
	- 線形動的システムの利用。SNSデータの利用。
1. [Chawla, S., Zheng, Y., & Hu, J. (2012). Inferring the root cause in road traffic anomalies. ICDM 2012. 141--150.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.711.7560&rep=rep1&type=pdf)
	- タスク：北京市の交通データから道路リンクの異常を検出、潜在的なOD流を予測。
	- 手法：主成分分析、線形計画法。
	- 特徴：ネットワークフローの問題と異常検知を同時に考えている。
	- データ：北京市タクシーGPS。
	- 感想：ネットワークフローと異常検知の組み合わせが面白い。
1. [Cudney, E. A., Drain, D., Paryani, K., & Sharma, N. (2009). A comparison of the Mahalanobis-Taguchi system to a standard statistical method for defect detection. Journal of Industrial and Systems Engineering, 2, 250--258.](http://www.jise.ir/article_3992_d103181416ac8e3da5438f99d373ef41.pdf)
	- タスク：MT法と統計技法による第一種の過誤、第二種の過誤を比較。
1. [Dasgupta, T. (2009). Integrating the improvement and the control phase of Six Sigma for categorical responses through application of Mahalanobis-Taguchi system (MTS). International Journal of Industrial and Systems Engineering, 4, 615-630.](http://www.stat.harvard.edu/Faculty_Content/dasgupta/IJISE_MTS_Dasgupta.pdf)
	- MTシステムの改善フェーズと制御フェーズの統一的手法を提案。
	- 直交表を用いたSN比による変数選択あり。
1. [Goldstein, M., & Uchida, S. (2016). A comparative evaluation of unsupervised anomaly detection algorithms for multivariate data. PloS one, 11(4), e0152173.](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0152173)
	- 異常検知手法の比較など。
1. [Gupta, M. Gao, Jing. Aggarwal, C., & Han, J. (2013). Outlier Detection for Temporal Data. SDM 2013.](https://archive.siam.org/meetings/sdm13/gupta.pdf)
	- 外れ値検出のスライド資料。
	- 特に、系列データ、ストリームデータ、空間系列データ、ネットワークデータについて。
1. [Kannan, R., Woo, H., Aggarwal, C. C., & Park, H. (2017). Outlier detection for text data. ICDM 2017. 489-497.](https://pdfs.semanticscholar.org/15e4/6987e753a7f01f3d0f3b23e5a948366f94e8.pdf)
	- テキストデータの外れ値検出。
1. [Kim, J., & Grauman, K. (2009). Observe locally, infer globally: a space-time MRF for detecting abnormal activities with incremental updates. In CVPR 2009. 2921--2928E.](http://www.cs.utexas.edu/users/ai-lab/pubs/kim_grauman_cvpr2009.pdf)
1. [Kinoshita, A., Takasu, A., & Adachi, J. (2015). Real-time traffic incident detection using a probabilistic topic model. Information Systems, 54, 169--188.](https://www.sciencedirect.com/science/article/pii/S0306437915001301)
1. [Kumar, S., Sotiris, V., & Pecht, M. (2008). Mahalanobis distance and projection pursuit analysis for health assessment of electronic systems. In Aerospace Conference, 2008 IEEE, 1--9.](https://www.prognostics.umd.edu/calcepapers/08_Sachin_mahabolisDistance_IEEBigSky.pdf)
	- タスク：電子機器の異常診断。
	- 手法：マハラノビス距離と「射影追跡 (projection pursuit)」。
	- 特徴：射影追跡法は、低次元空間にデータを圧縮する方法らしい。
	- データ：ノートPC（ファンの回転速度、CPU温度、マザーボード温度、ビデオカード温度、などなど）。
	- 感想：マハラノビス距離で異常度をみることが妥当かどうかの議論がなされているのがよい。
1. [Laxhammar, R., Falkman, G., & Sviestins, E. (2009). Anomaly detection in sea traffic-a comparison of the gaussian mixture model and the kernel density estimator. In Information Fusion, 2009. 756--763.](http://fusion.isif.org/proceedings/fusion09CD/data/papers/0327.pdf)
	- タスク：海上交通データに対する異常検知手法の比較。
	- 手法：混合正規分布、カーネル密度推定（Parzen Windows method）。
	- 特徴：海運データに適用したことと著者らは主張している。
	- データ： Automatic Identification System (AIS) data. 
	- 感想：前処理を丁寧に書いている。たとえば、時々刻々と採取される船舶位置と速度のデータについて、情報量を損なうことなくサンプリングするなどの工夫がある。
1. [Liu, H., Shah, S., & Jiang, W. (2004). On-line outlier detection and data cleaning. Computers & chemical engineering, 28, 1635--1647.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.605.6319&rep=rep1&type=pdf)
	- 前処理、外れ値検出、時系列データ。
1. [Matsubara, Y., Li, L., Papalexakis, E., Lo, D., Sakurai, Y., & Faloutsos, C. (2013). F-trail: Finding patterns in taxi trajectories. In Pacific-Asia Conference on Knowledge Discovery and Data Mining (pp. 86-98). Springer, Berlin, Heidelberg.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.380.2505&rep=rep1&type=pdf)
	- タクシーの追跡データからデータマイニング。
1. [Pang, L. X., Chawla, S., Liu, W., & Zheng, Y. (2011). On mining anomalous patterns in road traffic streams. ICADMA 2011, 237--251.](https://link.springer.com/chapter/10.1007%2F978-3-642-25856-5_18)
	- タスク：タクシーGPSデータから北京市の恒常的な外れ値と新規出現の外れ値を検出。
	- 手法：尤度比検定。
	- 特徴：upper-bounding strategyとやらを使って限定操作を行い、異常度の高い上位k個の領域を計算している。
	- データ：人工データ、北京市タクシーのGPSデータ。
	- シンプルだがおもしろい。[関連スライド](https://pdfs.semanticscholar.org/db55/8e1bfb8feaae50919a2952979a894669e486.pdf)もある。
1. [Ruff, L., Goernitz, N., Deecke, L., Siddiqui, S. A., Vandermeulen, R., Binder, A., ... & Kloft, M. (2018). Deep One-Class Classification. In International Conference on Machine Learning (pp. 4390-4399).](http://proceedings.mlr.press/v80/ruff18a/ruff18a.pdf)
	- タスク：画像の異常検出。
	- 手法：Deep neural support data description.
	- 特徴：One-class classificationにneural netの利用。
	- データ：MNIST, CIFAR-10.
	- 感想：異常検知×深層学習の中でも主要な文献。
1. [Sunderrajan, A., Viswanathan, V., Cai, W., & Knoll, A. (2016). Traffic State Estimation Using Floating Car Data. Procedia Computer Science, 80, 2008-2018.](http://mediatum.ub.tum.de/doc/1426777/999289.pdf)
	- floating car dataを利用して現在のトラフィック状態を推定。
	- キーワード：traffic state estimation
1. [Yamanishi, K., Takeuchi, J. I., Williams, G., & Milne, P. (2004). On-line unsupervised outlier detection using finite mixtures with discounting learning algorithms. Data Mining and Knowledge Discovery, 8(3), 275--300.](ftp://ftp.cse.buffalo.edu/users/azhang/disc/disc01/cd1/out/papers/kdd/p320-yamanishi.pdf)
1. [Yang, S., Kalpakis, K., & Biem, A. (2013, October). Spatio-temporal coupled bayesian robust principal component analysis for road traffic event detection. In Intelligent Transportation Systems-(ITSC), 2013 16th International IEEE Conference on (pp. 392-398). IEEE.](https://www.researchgate.net/profile/Shiming_Yang2/publication/278034667_main_conf_ITS13/links/557ae52d08ae8d0481931dcb.pdf)
1. [Yokoyama, D. & Toyoda, M. (2016). Do Drivers' Behavior Reflect Their Past Driving Histories? -Large Scale Examination of Vehicle Recorder Data-. In 2016 IEEE International Congress on Big Data, 361--368.](https://pdfs.semanticscholar.org/3451/ff02e000f1f5f45f088ada50e904e8e60001.pdf)
	- タスク：ドラレコデータから事故歴ありドライバの判別。
	- 手法：サポールベクターマシン。
	- 特徴：平均的なドライバーとの違いを表す説明変数を作成。エントロピーやKL-ダイバージェンスを利用。
	- データ：ドライバー経歴、ドラレコデータ、道路情報データ。
	- 感想：KL-ダイバージェンスは調査が必要。
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
1. [豊田正史，横山大作，伊藤正彦 (2017)．運転状況を考慮したドライブレコーダデータからの潜在リスク交差点検知手法． DEIM Forum 2017 A5-1.](http://db-event.jpn.org/deim2017/papers/372.pdf)
	- タスク：事故発生したことがある交差点を判別。
	- 手法：ロジスティック回帰。
	- 特徴：既存研究では道路形状や環境情報から道路の事故リスクを求めていたが、運転操作データを使った試みが新しい。
	- データ：ドラレコデータ、道路数値地図データ、雨量データ。
	- 感想：特徴量を作るための分析が面白い。事故確率が高い交差点をランキングしたときの結果が気になる。
1. [中原孝信, 前川浩基, 羽室行信. (2013). テレビ番組視聴時におけるTwitter投稿からのトピック検知. オペレーションズ・リサーチ 58, 442--448.](http://www.orsj.or.jp/archive2/or58-08/or58_8_442.pdf)
	- タスク：特定のTV番組を視聴中にその番組に関するTwitter投稿をするソーシャルビューイングの内容を要約。
	- 手法：マイクロクラスタリング、Kleinbergのバースト検知手法、ナップサック制約付き最大被覆問題の貪欲解放。
	- 特徴：Tweetの単語共起情報からトピック作成にマイクロクラスタリング利用、Tweetの盛り上がり検出にKleinbergのバースト検知手法、Tweetの要約にナップサック制約付き最大被覆問題の貪欲解法を利用。
	- データ：宇宙兄弟に関するTweet約28万件、TV番組「宇宙兄弟」の台詞。
	- 感想：数理モデルを使いこなしている感じがよい。
1. [村尾和哉, クリストフファンラールホーフェン, 寺尾努, 西尾章治郎. (2010). センサのピークを用いた状況認識手法. 情報処理学会論文誌 51, 1067--1077.](https://www.eti.uni-siegen.de/ubicomp/papers/ess_ipsj2010.pdf)
	- タスク：信号データを圧縮した特徴量の作成。
	- 手法：特徴量の評価のためクラスタリングおよびサポートベクトルマシンを利用。
	- 特徴：これまで、平均値、分散値、最大値および最小値、FFTパワースペクトルが波形データの特徴量として利用されていたが、新たに波形ピーク高さと幅を特徴量として利用。
	- データ：たとえば、人間に取り付けた複数の加速度センサ情報。
	- 感想：複数のデータセットで実験してほしい。加えて、アイデアがシンプルなだけに、似たものが提案されていそうな気がする。。
1. [山本敬介. (2013). 混合分布による道路状態推定. 東京大学大学院情報理工学系研究科修士論文, 2013.](http://repository-old.dl.itc.u-tokyo.ac.jp/dspace/bitstream/2261/54210/1/48116445.pdf)
	- タスク：車両走行情報の圧縮のため、時間、道路区間ごとに混合分布で特徴量を表現。
	- 手法：混合正規分布推定にEMアルゴリズム。
	- 特徴：平均と分散は各道路区間で共通、混合比が道路区間ごとに異なる。KL-divergenceを使って適切な混合数を決定。
	- データ：千代田区内の車両走行データ（速度のみ利用）。
	- 感想：東京大学大学院の手堅い修士論文という感じがする。平均と分散が同じ、混合比が異なるというアイデアは、LDAに由来するらしい。
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

## 画像処理
1. [Rubner, Y., Tomasi, C., & Guibas, L. J. (2000). The earth mover's distance as a metric for image retrieval. International journal of computer vision, 40, 99--121.](http://robotics.stanford.edu/~rubner/papers/rubnerIjcv00.pdf)
	- Earth Mover's Distance.
	- 画像のEMD計算実験、ビンの輸送コストの設定、三角不等式の証明、下界値の導出など。
1. [Boykov, Y. Y., & Jolly, M. P. (2001). Interactive graph cuts for optimal boundary and region segmentation of objects in ND images. ICCV 2001. 105--112.](http://www.csd.uwo.ca/~yuri/Papers/iccv01.pdf)
	- 画像の領域分割に対するグラフカット。

## セイバーメトリクス
1. [和泉志津恵, 小畑経史 (2018). サッカーリーグにおけるチームパフォーマンスの時間的推移の可視化. オペレーションズ・リサーチ 63, 628--634.](http://www.orsj.or.jp/archive2/or63-10/or63_10_628.pdf)
	- タスク：サッカーチームの週ごとパフォーマンスの可視化。
	- 手法：ポアソン回帰、変化係数モデル。
	- 特徴：サッカーの試合の得失点数がポアソン分布。
	- データ：2017年のJ2リーグ。
	- 感想：シンプル。時間以外の共変量を含むモデルが気になる。または位置情報データへの適用例、もしくは状態空間モデルでモデル化。
1. [西内啓 (2018). 2017年J1リーグ戦データから見る攻撃戦術のトレンド. オペレーションズ・リサーチ 63, 621--627.](http://www.orsj.or.jp/archive2/or63-10/or63_10_621.pdf)
	- タスク：サッカー攻撃戦術の分析。
	- 手法：ポアソン回帰のelastic net.
	- 特徴：100個以上の説明変数を作り込み。
	- データ：2017年J1の集計済みデータ。
	- 感想：どのようにデータを集計したのか気になる。人海戦術かどうか。

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

## 次元削減
1. [Cunningham, J. P., & Ghahramani, Z. (2015). Linear dimensionality reduction: Survey, insights, and generalizations. The Journal of Machine Learning Research, 16(1), 2859-2900.](http://www.jmlr.org/papers/volume16/cunningham15a/cunningham15a.pdf)
	- 線形次元削減のサーベイ。
	- 主成分分析、因子分析、多次元尺度法、Fischerの判別分析、正準相関分析、maximum correlation factors, slow feature analysis, sufficient dimension reduction,  undercomplete independent component analysis, 線形回帰、距離尺度の学習など。
1. [Hastie, T., Tibshirani, R., & Tibshirani, R. J. (2017). Extended Comparisons of Best Subset Selection, Forward Stepwise Selection, and the Lasso. arXiv preprint arXiv:1707.08692.](https://arxiv.org/pdf/1707.08692.pdf)
	- 変数選択とLassoの関係を、Lassoの開発者たちが議論。

## 確率・統計モデル
1. [佐野夏樹 (2017). 隠れマルコフモデルによる顧客店舗内行動の推定, オペレーションズ・リサーチ 62, 801--806.](http://www.orsj.or.jp/archive2/or62-12/or62_12_801.pdf)
	- タスク：店舗内の顧客動線のモデル化。
	- 手法：隠れマルコフモデルの定常モデルと非定常モデル。
	- 特徴：隠れ変数に意味付け、Dharらの「ショッピングモーメンタム」の検証。
	- データ：RFIDとPOS。
	- 感想：隠れマルコフモデルの適用例としておもしろい。
1. [永森誠矢, 山下遥, 萩原大陸, 後藤正幸 (2018). 混合回帰に基づく就職ポータルサイトの被エントリ数分析モデルに関する一考察, 情報処理学会論文誌 59, 1273--1285.](http://www.it.mgmt.waseda.ac.jp/results/papers/IPSJ-JNL5904017.pdf)
	- タスク：就職ポータルサイトの被エントリ数分析。
	- 手法：混合回帰モデル、推定はEMアルゴリズム。
	- 特徴：グラフィカルモデルにより、単なる混合回帰モデルに修正を加えている。
	- データ：就職ポータルサイトのデータ。
	- 感想：説明変数4つが機密情報であるとのことで、明らかにされていない。それを使って分析しているので、どのような施策がされるのか、わからない。
1. [山根智之, 菅原光太郎, 西村直樹, 小林健, 吉田佑輔, 高野祐一, 中田和秀 (2016). 時系列モデルによる商品販促効果の分析, オペレーションズ・リサーチ 61, 65--70.](http://www.orsj.or.jp/archive2/or61-2/or61_2_65.pdf)
	- タスク：スーパーにおけるクーポンの販促効果を分析。
	- 手法：状態空間モデル。
	- 特徴：クーポン効果ともともとの購買意欲をわけて考える。購買意欲は3期の自己回帰を仮定している。
	- データ：スーパーの顧客購買履歴。
	- 感想：確率の言葉を使わずに書かれた論文。データから問題設定をする着眼点がおもしろい。

## 最適化
1. [Correa, J. R., Fernandes, C. G., & Wakabayashi, Y. (2010). Approximating a class of combinatorial problems with rational objective function. Mathematical programming, 124, 255--269.](https://www.dii.uchile.cl/~jcorrea/papers/Journals/CFW2010.pdf)
	- 整数制約付き分数関数最小化。
1. [Feldman, J., Malkin, T., Servedio, R. A., Stein, C., & Wainwright, M. J. (2007). LP decoding corrects a constant fraction of errors. IEEE Transactions on Information Theory, 53(1), 82-89.](http://people.csail.mit.edu/jonfeld/pubs/lpexpand_corc_tech.pdf)
	- LPを使う端数誤差修正。
1. [GÓMEZ, A., & PROKOPYEV, O. A. (2018). A mixed-integer fractional optimization approach to best subset selection. Optimization Online, 2018.](http://www.optimization-online.org/DB_FILE/2018/09/6795.pdf)
	- タスク：混合整数分数最適化問題による変数選択。
	- 特徴：変数セットのサイズを固定して何回も解くよりも高速、MISOCPよりも高速。実装楽。
	- 手法：定式化の変形にポリマトロイド。
	- データ：UCI Machine Learning Repositoryと、乱数生成。
	- 感想：ストーリーが追いにくい部分がある。特に、定式化が等価変形なのか、緩和なのか、いずれでもないのか、わかりにくい。
1. [Murty, K. G., & Kabadi, S. N. (1987). Some NP-complete problems in quadratic and nonlinear programming. Mathematical programming, 39(2), 117-129.](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/6740/bam7058.0001.001.pdf?sequence=5&isAllowed=y)
	- 非線形計画とNP完全。

## 木構造モデル
1. [Belov, G., Esler, S., Fernando, D., Le Bodic, P., & Nemhauser, G. L. (2017). Estimating the size of search trees by sampling with domain knowledge. In IJICAI 2017, 473--479.](http://static.ijcai.org/proceedings-2017/0067.pdf)
	- MIP の探索木のサイズを推定。
1. [Breiman, L. (2001). Random Forest. Machine Learning 45, 5--32.](https://link.springer.com/article/10.1023%2FA%3A1010933404324)
1. [Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. In KDD '16 785--794.](https://dl.acm.org/citation.cfm?id=2939785)
1. [Fogarty, J. (2007). Data Structures. Washington University Lecture Slides.](https://courses.cs.washington.edu/courses/cse326/07au/lectures/calendar_au07.htm)
	- k-d木やQuadTreeなど、データ構造の講義スライド。
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
1. [Steorts, R. C. (2017). Data Mining and Machine Learning, Tree Based Methods: Bagging, Boosting, and Regression Trees. Duke University Lecture Slide.](http://www2.stat.duke.edu/~rcs46/lectures_2017/08-trees/08-tree-advanced.pdf)
	- データマイニングと機械学習の講義スライド。
	- Baggin, Boosting, Regression Treesについてボリュームある説明。
	- 木構造の利点のひとつは解釈性であるが、Random Forestのように木がたくさんあると、解釈しにくい。解釈のためのひとつの方法としてvariable importanceを考える。これは回帰であればRSSを用い、分類であればGini indexを使う。

## データ構造
1. [Bentley, J. L. (1975). Multidimensional Binary Search Trees Used for Associative Searching. Communications of the ACM, 18, 509--517.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.160.335&rep=rep1&type=pdf)
	- k-d木の提案。
1. [Bury, M., Schwiegelshohn, C., & Sorella, M. (2016). Efficient Similarity Search in Dynamic Data Streams. arXiv preprint arXiv:1605.03949.](https://arxiv.org/abs/1605.03949)
1. [Charikar, M. S. (2002). Similarity estimation techniques from rounding algorithms. In Proceedings of the thiry-fourth annual ACM symposium on Theory of computing, 380--388. ACM.](http://www.cs.princeton.edu/courses/archive/spring04/cos598B/bib/CharikarEstim.pdf)
1. [Fagin, R., Kumar, R., & Sivakumar, D. (2003, June). Efficient similarity search and classification via rank aggregation. In Proceedings of the 2003 ACM SIGMOD international conference on Management of data, 301-312. ACM.](https://s3.amazonaws.com/academia.edu.documents/34071215/rank-aggregation.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1526142136&Signature=qPX4aYR5Y2B21fmfb8qNts08OwI%3D&response-content-disposition=inline%3B%20filename%3DEfficient_similarity_search_and_classifi.pdf)
1. [Guttman, A. (1984). R-trees: A dynamic index structure for Spatial Searching. In SIGMOD, 47--57.](https://klevas.mif.vu.lt/~algis/DSA/guttman.pdf)
1. [Liu, T., Moore, A. W., & Gray, A. (2006). New algorithms for efficient high-dimensional nonparametric classification. Journal of Machine Learning Research, 7, 1135--1158.](http://www.jmlr.org/papers/volume7/liu06a/liu06a.pdf)
	- ball treeを使った新しいクラスタリング手法。
1. [Khan, M., Ding, Q., & Perrizo, W. (2002). K-Nearest Neighbor Classification on Spatial Data Streams Using P-Trees. In PAKDD 517--528.](https://pdfs.semanticscholar.org/0286/c5fee2dea935c601d55b44ef8cae965bbff7.pdf)
1. [Kingsford. S. Bioinformatics Lectures. Carnegie Mellon University Lecture Slide.](http://kingsfordlab.cbd.cmu.edu/bioinformatics-lectures/)
	- QuadTree, Kd-Treeなど。
1. [Kunze, M. & Weske, M. (2010). Metric Trees for Efficient Similarity Search in Large Process Model Repositories. In International Conference on Business Process Management. 535-546. Springer, Berlin, Heidelberg.](https://link.springer.com/chapter/10.1007/978-3-642-20511-8_49)
1. [Manolopoulos, Y., Nanopoulos, A., Papadopoulos, A. N., Theodoridis, Y. (2005).  R-trees: Theory and Applications. Springer-Verlag London.](http://delab.csd.auth.gr/rtrees/)
	- 空間データ構造R-treeのテキスト。
	- 1章(Introduction)と2章(Dynamic Version of R-trees)はリンク先からダウンロードできる。
1. [Papadias, D., Zhang, J., Mamoulis, N., & Tao, Y. (2003). Query processing in spatial network databases. VLDB 2003, 802--813.](http://repository.ust.hk/ir/bitstream/1783.1-157/1/VLDB03SNDB.pdf)
1. [Sand, P., & Moore, A. W. (2001). Repairing faulty mixture models using density estimation. In ICML 457--464.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.20.7585&rep=rep1&type=pdf)
	- k-d木を使って密度推定。
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
1. [Zhou, K., Hou, Q., Wang, R., & Guo, B. (2008). Real-time kd-tree construction on graphics hardware. ACM Transactions on Graphics, 27, 126.](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2008-52.pdf)
	- k-d木とGPU。
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
