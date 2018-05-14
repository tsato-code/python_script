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
	* [sysモジュールによるコマンドライン引数のテスト](pythonscript/test_sys_args.py)
	* [tempfileモジュールによる一時ファイルと一時ディレクトリのテスト](pythonscript/test_tempfile.py)
	* [timeモジュールによる時間を扱う関数のテスト](pythonscript/test_time.py)
	* [tqdmモジュールによるプログレスバーのテスト](pythonscript/test_tqdm.py)
	* [yamlモジュールによるYAML読み込みのテスト](pythonscript/test_yaml.py)
	* [jitコンパイラライブラリNumbaのテスト](pythonscript/test_numba_jit.py)
	* [形態素解析エンジンMeCabのテスト](pythonscript/test_mecab.py)
	* [係り受け解析エンジンCaboChaのテスト](pythonscript/test_cabocha.py)
	* [自然言語処理ツールStanford CoreNLPのテスト](pythonscript/test_corenlp.py)
	* [マップクライアントライブラリfoliumのテスト（GitHubからは画像が確認できない）](pythonscript/test_folium.ipynb)
* Shell
	* [Windows用バッチファイルのテスト](shellscript/test_bat.bat)
* 最適化関連
	* [Prim法クラス](optimization/test_prim.py)
	* [Rosenbrock関数の描画とニュートン法のテスト](optimization/rosenbrock.ipynb)
* 統計+機械学習+MCMC
	* [平均情報量(entropy)と相対エントロピー(Kullback-Leibler divergence)](machinelearning/test_ent_kl.py)
	* [pandasコマンドのテスト](machinelearning/test_pandas.ipynb)
	* [scikit-learnのデータセット確認のテスト](machinelearning/sklearn_load_data.ipynb)
	* [scikit-learnの決定木（回帰）のテスト](machinelearning/test_decisiontreeregressor.ipynb)
	* [scikit-learnのランダムフォレスト（分類）のテスト](machinelearning/test_randomforest.ipynb)
	* [gensimのLDAのテスト](machinelearning/test_gensim_lda.ipynb)
	* [久保先生のみどり本8章のPython化](machinelearning/kubo8.ipynb)
* データ構造
	* [QuadTree](datastructure/test_quadtree.ipynb)
	* [R-Tree](datastructure/test_rtree.py)
* その他
	* [再帰深さ上限の確認](misc/test_recursion.py)
	* [論理演算の処理速度確認](misc/compare_logical_operator.py)
	* [組み込み関数allの処理速度確認（その1）](misc/compare_all01.py)
	* [組み込み関数allの処理速度確認（その2）](misc/compare_all02.py)
	* [pandasのDataFrameの列に対するloop処理速度比較（その1）](misc/compare_pandas_loop01.py)
	* [pandasのDataFrameの列に対するloop処理速度比較（その2）](misc/compare_pandas_loop02.py)
	* [pandasのDataFrameの列に対するloop処理速度比較（その3）](misc/compare_pandas_loop03.py)
	* [pandasのDataFrameの列に対する距離計算](misc/calc_pandas_dist.py)
	* [pandasのDataFrameの列に対する距離計算の処理速度比較（その1）](misc/compare_pandas_var_use.py)
	* [pandasのDataFrameの列に対する距離計算の処理速度比較（その2）](misc/compare_pandas_dist_numpy.py)
	* [平面上の点を線に射影するコード](misc/proj_point_to_line.ipynb)
