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
root: C:\Users\tsk_sato\Documents\python_codes
dirs: ['.ipynb_checkpoints']
files: ['dockerfile', 'git_command_memo.txt', 'kubo8.ipynb', 'readme.md', 'rosenbrock.ipynb', 'test_argparse.py', 'test_bm.py', 'test_class.py', 'test_format.py', 'test_glob.py', 'test_lambda.py', 'test_multiprocessing.py', 'test_os_walk.py', 'test_prim.py', 'test_subprocess.py', 'test_sys_args.py', 'test_tempfile.py', 'test_time.py', 'test_tqdm.py', 'todo.txt']
----------------------------------------
root: C:\Users\tsk_sato\Documents\python_codes\.ipynb_checkpoints
dirs: []
files: ['kubo8-checkpoint.ipynb']
----------------------------------------
"""