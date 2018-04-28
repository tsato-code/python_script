# スクリプト集

* py-collection
	* [無名関数のテスト](./test_lambda.py)
	* [クラスの定義とクラスのテスト](./test_class.py)
	* [クラスモジュールの呼出しテスト](./test_call_class.py)
	* [コマンドラインオプションとヘルプのテスト](./test_argparse.py)
	* [例外処理のテスト](./test_assert.py)
	* [文字列フォーマットを利用した出力テスト](./test_format.py)
	* [ファイル取得のテスト](./test_glob.py)
	* [並列処理モジュールmultiprocessingのテスト](test_multiprocessing.py)
	* [並列処理モジュールjoblibのテスト](./test_joblib.py)
	* [ディレクトリとファイルの取得テスト](./test_os_walk.py)
	* [コマンドライン引数のテスト](./test_sys_args.py)
	* [一時ファイルと一時ディレクトリのテスト](./test_tempfile.py)
	* [時間を扱う関数のテスト](./test_time.py)
	* [プログレスバーのテスト](./test_tqdm.py)
	* [デコレータのテスト](./test_decorate.ipynb)
	* [jitコンパイラのテスト](./test_numba_jit.py)
	* [形態素解析エンジンMeCabのテスト](./test_mecab.py)
	* [自然言語処理ツールStanford CoreNLPのテスト](./test_corenlp.py)
	* [マップクライアントライブラリfoliumのテスト（GitHubからは画像が確認できない）](./test_folium.ipynb)
* shell-collection
	* [Windows用バッチファイルのテスト](./test_bat.bat)
* 最適化関連
	* [Prim法のテスト](./test_prim.py)
	* [Rosenbrock関数の描画とニュートン法のテスト](./rosenbrock.ipynb)
* 統計+機械学習+MCMC
	* [データ分析ライブラリpandasのテスト](./test_pandas.ipynb)
	* [機械学習ライブラリscikit-learnのデータセット](./sklearn_load_data.ipynb)
	* [久保先生のみどり本8章の勉強用pythonスクリプト](./kubo8.ipynb)
* その他
	* [pandasのDataFrameの列に対するloop処理速度比較テスト（その1）](./compare_pandas_loop01.py)
	* [pandasのDataFrameの列に対するloop処理速度比較テスト（その2）](./compare_pandas_loop02.py)
	* [pandasのDataFrameの列に対するloop処理速度比較テスト（その3）](./compare_pandas_loop03.py)
	* [pandasのDataFrameの列に対する距離計算](./calc_pandas_dist.py)
	* [pandasのDataFrameの列に対する距離計算に変数を用意したときとそうでないときの処理速比較テスト](./compare_pandas_var_use.py)
	* [pandasのDataFrameの列に対する距離計算にnumpyの関数を使ったときとそうでないときの処理速度比較テスト](./compare_pandas_dist_numpy.py)
	* [平面上の点を線に射影するコード](./proj_point_to_line.ipynb)
* [予定]
	* test_subprocess.py
		* call, check_call, check_output, Popenの違いなど
