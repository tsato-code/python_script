import sys

args = sys.argv
for i, arg in enumerate(args):
	print('arg[{}] > {}'.format(i, arg))

"""
$ python test_sys.py 6 3 ‚Ù‚° fuga
arg[ 0 ] > test_sys.py
arg[ 1 ] > 6
arg[ 2 ] > 3
arg[ 3 ] > ‚Ù‚°
arg[ 4 ] > fuga
"""
