# スクリプト集

* Python
	* [無名関数のテスト](pythonscript/test_lambda.py)
	* [文字列フォーマットを利用した出力テスト](pythonscript/test_format.py)
	* [クラスの定義とクラスのテスト](pythonscript/test_class.py)
	* [クラスモジュールの呼出しテスト](pythonscript/test_call_class.py)
	* [デコレータのテスト](pythonscript/test_decorator.ipynb)
	* [例外処理のテスト](pythonscript/test_assert.py)
	* [argparseモジュールによるコマンドラインオプションとヘルプのテスト](pythonscript/test_argparse.py)
	* [globモジュールによるファイル取得のテスト](pythonscript/test_glob.py)
	* [multiprocessingモジュールによる並列処理のテスト](pythonscript/test_multiprocessing.py)
	* [joblibモジュールによる並列処理のテスト](pythonscript/test_joblib.py)
	* [osモジュールによるディレクトリとファイルの取得テスト](pythonscript/test_os_walk.py)
	* [reモジュールによる正規表現のテスト](pythonscript/test_re.py)
	* [sysモジュールによるコマンドライン引数のテスト](pythonscript/test_sys_args.py)
	* [tempfileモジュールによる一時ファイルと一時ディレクトリのテスト](pythonscript/test_tempfile.py)
	* [timeモジュールによる時間を扱う関数のテスト](pythonscript/test_time.py)
	* [datetimeモジュールによる日付から曜日取得のテスト](pythonscript/test_datetime_day_of_week.py)
	* [tqdmモジュールによるプログレスバーのテスト](pythonscript/test_tqdm.py)
	* [line_profilerモジュールによるプロファイリングのテスト](pythonscript/test_line_profiler.py)
	* [yamlモジュールによるYAML読み込みのテスト](pythonscript/test_yaml.py)
	* [scipyモジュールによるmatデータの変換](pythonscript/mat_to_csv.py)
	* [jitコンパイラライブラリNumbaのテスト](pythonscript/test_numba_jit.py)
	* [日本語形態素解析器MeCabのテスト](pythonscript/test_mecab.py)
	* [日本語形態素解析器Janomeのテスト](pythonscript/test_janome.py)
	* [英語形態素解析器nltkのテスト](pythonscript/test_nltk.py)
	* [係り受け解析器CaboChaのテスト](pythonscript/test_cabocha.py)
	* [自然言語処理ツールStanford CoreNLPのテスト](pythonscript/test_corenlp.py)
	* [マップクライアントライブラリfoliumのテスト（GitHubからは画像が確認できない）](pythonscript/test_folium.ipynb)
	* [LINE_notifyのテスト](pythonscript/line_send.py)
	* [メール送信のテスト](pythonscript/mail_send.py)
* Shell
	* [Windows用バッチファイルのテスト](shellscript/test_bat.bat)
* QGIS3関連
	* [QGIS3操作メモ](memo_QGIS3.md)
* 最適化関連
	* [Prim法クラス](optimization/test_prim.py)
	* [ナップサック問題に対する動的計画のテスト](optimization/test_functools_lru_cache_knapsack.py)
	* [Rosenbrock関数の描画とニュートン法のテスト](optimization/rosenbrock.ipynb)
	* [pulpによるナップサック問題の求解](optimization/test_pulp.py)
* 統計+機械学習
	* [平均情報量(entropy)と相対エントロピー(Kullback-Leibler divergence)](machinelearning/test_ent_kl.py)
	* [ウェルチのt検定](machinelearning/welchs_ttest.py)
	* [動的計画法によるLevenshtein距離](machinelearning/test_functools_lru_cache_levenshtein.py)
	* [直交表の生成](machinelearning/make_orthogonal_array.py)
	* [pandasのテスト](machinelearning/test_pandas.ipynb)
	* [pandasのDataFrameでcolormap（GitHubでは背後の画像が確認できない）](machinelearning/test_colormap.ipynb)
	* [scikit-learnのデータセット確認](machinelearning/sklearn_load_data.ipynb)
	* [scikit-learnの分類用データ生成](machinelearning/test_make_classification.ipynb)
	* [scikit-learnの変数選択](machinelearning/sklearn_feature_selection.py)
	* [scikit-learnのk-means](machinelearning/sklearn_kmeans.ipynb)
	* [scikit-learnの決定木（回帰）](machinelearning/test_decisiontreeregressor.ipynb)
	* [scikit-learnのランダムフォレスト（分類）](machinelearning/test_randomforest.ipynb)
	* [scikit-learnの混合正規分布の推定1（正規分布の合成データ）](machinelearning/test_gmm1.ipynb)
	* [scikit-learnの混合正規分布の推定2（分類用データセット）](machinelearning/test_gmm2.ipynb)
	* [scikit-learnの混合正規分布の推定3 (iris)](machinelearning/sklearn_gmm.py)
	* [scikit-learnの多次元尺度法 (digits)](machinelearning/sklearn_mds.ipynb)
	* [scikit-learnの線形判別分析 (digits)](machinelearning/sklearn_lda.ipynb)
	* [scikit-learnのk近傍法](machinelearning/test_knn.py)
	* [scikit-learnのt-SNE](machinelearning/test_tsne.ipynb)
	* [hmmlearnの隠れマルコフモデル](machinelearning/hmm.py)
	* [statsmodelsのポアソン回帰とelastic net](machinelearning/poisson_reg.py)
	* [statsmodelsの自己相関係数](machinelearning/note_acf.ipynb)
	* [PyMC3による線形回帰のMCMC](machinelearning/pymc3_linear_reg.ipynb)
	* [gensimのLDAのテスト](machinelearning/test_gensim_lda.ipynb)
	* [lightgbmのテスト](machinelearning/test_lgbm.py)
	* [久保先生のみどり本8章のPython化](machinelearning/kubo8.ipynb)
	* [1次元ホテリング法](machinelearning/ide2_Hotellings_T-squared.ipynb)
	* [avocadoの探索的データ解析](machinelearning/note_avocado.ipynb)
	* [avocadoの隠れマルコフモデル](machinelearning/avocado_hmm.ipynb)
	* MT法 (online news popularlity) [Mahalanobis距離](machinelearning/MTS.py), [項目選択](machinelearning/orthogonal_array.py)
	* MT法の交差検証 ([SkillCraft1](machinelearning/MTS_SkillCraft1.ipynb), [OnlineNewsPopularity](machinelearning/MTS_OnlineNewsPopularity.ipynb))
	* [混合正規分布による外れ値検出 (iris, breast cancer, brest cancer coimbra, digits, winequality)](machinelearning/note_gmm_anom.ipynb)
	* [局所外れ値度 (Davis)](machinelearning/note_local_outlier_factor.ipynb)
	* [カーネル密度推定による外れ値検出 (iris, online news popularity)](machinelearning/note_kde.ipynb)
	* [winequalityの異常検知](machinelearning/note_wine.ipynb)
	* [Road Accident Deaths in US Statesの異常検知](machinelearning/note_road.ipynb)
	* [Kalman Filter](machinelearning/kalman_filter.py)
	* [ローカルモデル](machinelearning/local_level_model.ipynb)
* 計算幾何
	* [平面上の点を線に射影](computationalgeometry/proj_point_to_line.ipynb)
	* [scipyのspatialを用いたボロノイ図とドロネー図](computationalgeometry/test_scipy_spatial.ipynb)
* 乱択アルゴリズム
	* [選択アルゴリズム（k 番目の要素の選択）](randomizedalgorithm/selection_algorithm.py)
* データ構造
	* [2分探索木](datastructure/test_binary_search_tree.py)
	* [B-Tree](datastructure/test_b_tree.py)
	* [k-d tree](datastructure/test_kd_tree.py)
	* [R-Tree](datastructure/test_rtree.py)
	* [QuadTree](datastructure/test_quadtree.ipynb)
* その他
	* [自作ログ関数](misc/my_logging.py)
	* [再帰深さ上限の確認](misc/test_recursion.py)
	* [論理演算の処理速度確認](misc/compare_logical_operator.py)
	* [pandasのDataFrame複数列に対するソート](misc/test_df_sort.ipynb)
	* [組み込み関数allの処理速度確認(1): allがリスト内要素をどの順で評価しているか](misc/compare_all01.py)
	* [組み込み関数allの処理速度確認(2): allと自作関数にかかる時間](misc/compare_all02.py)
	* [pandasのDataFrame列に対するloop(1): iterrows, apply, map, ndarray型変換](misc/compare_pandas_loop01.py)
	* [pandasのDataFrame列に対するloop(2): 2列の演算](misc/compare_pandas_loop02.py)
	* [pandasのDataFrame列に対するloop(3): JITコンパイラとの比較](misc/compare_pandas_loop03.py)
	* [pandasのDataFrame列に対する距離計算(1): 距離関数の定義](misc/calc_pandas_dist.py)
	* [pandasのDataFrame列に対する距離計算(2): 変数に値を保存しながら計算したときの処理時間](misc/compare_pandas_var_use.py)
	* [pandasのDataFrame列に対する距離計算(3): numpyのnorm関数の処理時間](misc/compare_pandas_dist_numpy.py)
	* [連立方程式の求解を比較 (逆行列とCholesky分解)](misc/test_cholesky.py)
	* [一般化固有値問題の計算](misc/gen_eig_prob.py)
	* [緯度経度を平面座標に変換](misc/test_latlon2yx.py)
	* [MT法スライド用画像](misc/plot_slide_MTS.ipynb)
	* [次元削減スライド用画像](misc/plot_slide_dimension_reduction.ipynb)
	* [還元スライド用画像](misc/plot_slide_reduction.ipynb)
	* [matplotlibオブジェクトを関数の引数にする](misc/plot_func.ipynb)
	* [複数画像を1枚の画像に収める](misc/plot_subplot.ipynb)
	* [irisデータで複数の画像を生成して画像を保存](misc/plot_iris.py)
	* contourで等高線 ([note](misc/plot_contour.ipynb), [script](misc/plot_contour.py))
