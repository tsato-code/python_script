import os
 
dir = os.path.dirname(os.path.abspath(__file__))

for root, dirs, files in os.walk(dir):
	dirs[:] = [d for d in dirs if '.git' not in d] 	# 特定のファイルを除く
	print("root: {}".format(root))
	print("dirs: {}".format(dirs))
	print("files: {}".format(files))
	print('-' * 40)


"""
$ python test_os_walk.py 
root: /Users/username/python_codes
dirs: []
files: ['test_sys_args.py', 'test_multiprocessing.py', 'test_os_walk.py', 'readme.md']
----------------------------------------
"""