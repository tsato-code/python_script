import sys

args = sys.argv
for i, arg in enumerate(args):
	print('arg[{}] > {}'.format(i, arg))

"""
$ python test_sys_args.py 1 2 あ 試
arg[0] > test_sys_args.py
arg[1] > 1
arg[2] > 2
arg[3] > あ
arg[4] > 試
"""