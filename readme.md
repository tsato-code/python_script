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
	* [jitコンパイラライブラリNumbaのテスト](pythonscript/test_numba_jit.py)
	* [形態素解析器MeCabのテスト](pythonscript/test_mecab.py)
	* [形態素解析器Janomeのテスト](pythonscript/test_janome.py)
	* [係り受け解析器CaboChaのテスト](pythonscript/test_cabocha.py)
	* [自然言語処理ツールStanford CoreNLPのテスト](pythonscript/test_corenlp.py)
	* [マップクライアントライブラリfoliumのテスト（GitHubからは画像が確認できない）](pythonscript/test_folium.ipynb)
* Shell
	* [Windows用バッチファイルのテスト](shellscript/test_bat.bat)
* 最適化関連
	* [Prim法クラス](optimization/test_prim.py)
	* [ナップサック問題に対する動的計画のテスト](optimization/test_functools_lru_cache_knapsack.py)
	* [Rosenbrock関数の描画とニュートン法のテスト](optimization/rosenbrock.ipynb)
	* [pulpによるナップサック問題の求解](optimization/test_pulp.py)
* 統計+機械学習+MCMC
	* [平均情報量(entropy)と相対エントロピー(Kullback-Leibler divergence)](machinelearning/test_ent_kl.py)
	* [動的計画法によるLevenshtein距離](machinelearning/test_functools_lru_cache_levenshtein.py)
	* [pandasのテスト](machinelearning/test_pandas.ipynb)
	* [pandasのDataFrameでcolormapのテスト（GitHubでは背後の画像が確認できない）](machinelearning/test_colormap.ipynb)
	* [scikit-learnのデータセット確認のテスト](machinelearning/sklearn_load_data.ipynb)
	* [scikit-learnの決定木（回帰）のテスト](machinelearning/test_decisiontreeregressor.ipynb)
	* [scikit-learnのランダムフォレスト（分類）のテスト](machinelearning/test_randomforest.ipynb)
	* [scikit-learnのt-SNEのテスト](machinelearning/test_tsne.ipynb)
	* [gensimのLDAのテスト](machinelearning/test_gensim_lda.ipynb)
	* [久保先生のみどり本8章のPython化](machinelearning/kubo8.ipynb)
	* [1次元ホテリング法](machinelearning/ide2_Hotellings_T-squared.ipynb)
	* [カーネル密度推定による外れ値検出](machinelearning/ide3_kernel_density.ipynb)
* 計算幾何
	* [平面上の点を線に射影](computationalgeometry/proj_point_to_line.ipynb)
	* [scipyのspatialを用いたボロノイ図とドロネー図](computationalgemetry/test_scipy_spatial.ipynb)
* データ構造
	* [2分探索木](datastructure/test_binary_search_tree.py)
	* [B-Tree](datastructure/test_b_tree.py)
	* [R-Tree](datastructure/test_rtree.py)
	* [QuadTree](datastructure/test_quadtree.ipynb)
* その他
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
	* [緯度経度を平面座標に変換](misc/test_latlon2yx.py)
