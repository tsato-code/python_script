import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
	'-arg', '--argument',		# オプション名
	action='store',				# 引数のアクション指定'store_true', 'action_false' など
	nargs='?',					# 複数の引数をリスト化、ほかに '*', '+', '?' など
	type=str,					# 引数型
	choices=['A', 'B', 'C'],	# 引数はリスト内のどれか
	const='A',					# 引数で自動的に10を設定
	default='B',				# 引数がなかったときに自動的に設定
	required=True, 				# 引数必須化
	help='argparseのテスト'
	)

args = parser.parse_args()
print(args)


"""
$ python test_argparse.py -arg C
Namespace(argument='C')
"""